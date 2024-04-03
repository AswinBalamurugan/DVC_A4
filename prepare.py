import os
import yaml
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Variables 
params_global = yaml.safe_load(open('params.yaml'))['global']
params = yaml.safe_load(open('params.yaml'))['prepare']

download_dir = params_global['download_dir']
hourly_cols = params_global['hourly_cols']
GT_cols = params_global['filter_cols']

GT_to_hourly = {gt:hourly for gt,hourly in zip(GT_cols,hourly_cols)}
gt_dir = os.path.join(*params['gt_dir'])

os.makedirs(gt_dir, exist_ok=True)
# Get list of CSV files in the directory
csv_files = [file for file in os.listdir(download_dir) if file.endswith('.csv')]
dfs = []

for i,filename in enumerate(csv_files):
    download_path = os.path.join(download_dir, filename)
    df = pd.read_csv(download_path, low_memory=False)  # Read the downloaded CSV file into DataFrame
    
    df['Month'] = df['DATE'].apply( lambda x: int(x.split('-')[1]) )  
    df.drop('DATE',axis=1,inplace=True)

    # The below code filters out the columns which contain the monthly average data for ground truth
    GT_df = df[['Month']+GT_cols].groupby('Month').tail(1).dropna(axis=1,thresh=1).reset_index(drop=True)
    GT_df.to_csv( os.path.join(gt_dir, f'gtcsv_{i+1}.csv') ,index=False)

