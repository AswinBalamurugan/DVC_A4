import os, re, random, requests
import yaml
import pandas as pd
params_global = yaml.safe_load(open('params.yaml'))['global']
params = yaml.safe_load(open('params.yaml'))['download']

################################################ Variables ################################################

YYYY = params_global['YYYY']
download_dir = params_global['download_dir']
filter_cols = params_global['filter_cols']

html_filename = params['html_filename']
n_locs = params['n_locs']
base_url = params['base_url']
seed_value = params['seed']

random.seed(seed_value)

################################################ FETCH PAGE ################################################
# Fetch page and save to a file
fetch_command = f'curl -s -o {html_filename} {base_url}'
os.system(fetch_command)

################################################ GET ALL FILENAMES ################################################
# Define function to extract CSV filenames
def extract_csv_names(html_path):
    """Extracts CSV filenames from the provided HTML file path."""

    with open(html_path, 'r') as file:
        html_content = file.read()

    # Extract text within quotation marks for anchor tags with href ending in '.csv'
    csv_filenames = re.findall(r'<a href="([^"]+\.csv)">', html_content)
    
    return csv_filenames

# Extract CSV filenames from the saved HTML
csv_names = extract_csv_names(html_filename)

################################################ DOWNLOAD REQUIRED FILES ################################################

def fetch_data_files(base_url, download_dir, csv_file_names, num_files, monthly_cols):
    """Fetches individual data files from the base URL."""
    i = 1
    csv_file_names = [name for name in csv_file_names if name.endswith('.csv')]
    while num_files:

        # csv_names = random.sample(csv_file_names, 10) # Uncomment this line for automated file search
        csv_names = ['72506794720.csv','99999963871.csv'] # This line is only to speed up the process
        
        os.makedirs(download_dir, exist_ok=True)  # Create directory if it doesn't exist
        for filename in csv_names:
            download_path = os.path.join(download_dir, filename)
            url = f"{base_url}{filename}"
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise exception for non-200 status codes

            # Open the download file in write binary mode
            with open(download_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

        # Check if the condition holds for the downloaded file
        for filename in csv_names:
            download_path = os.path.join(download_dir, filename)
            df = pd.read_csv(download_path, low_memory=False)  # Read the downloaded CSV file into DataFrame
            full_of_nan = df[monthly_cols].isnull().all().all()
            if (not full_of_nan) and num_files:
                num_files -= 1
            else:
                os.remove(download_path)  # Remove the file if condition is not met
        
        print(f'Samples from batch {i} done! Found {2-num_files} file(s).')
        i += 1

    if num_files != 0:
        print('Change the year and retry!!')

# Fetch individual data files
fetch_data_files(base_url, download_dir, csv_names, n_locs, filter_cols)
os.remove(html_filename)