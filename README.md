# Objective
To understand the use of DVC and git for project version control.

# Dataset
The National Centers for Environmental Information (NCEI) maintains an extensive archive of environmental data, including oceanic, atmospheric, and geophysical data. The NCEI archives over 229 terabytes of data each month from over 130 observing platforms.
The NCEI also provides archive services for much of the data collected by NOAA scientists, observing systems, and research initiatives. The NCEI manages a comprehensive collection of environmental information from various periods, observing systems, scientific disciplines, and geographic locations.

# Task
* Pull the `n_loc` number of files from the ncei data website.
* The files contain columns with aggregates of monthly averages; use this as the *ground truth* data.
* Compute the monthly averages using the *hourly* data available in the files.
* Compute R2 scores for the columns for each file.

# Setup
The `dvc stage add` commands are present in `comments.txt`. 
Run them individually to add stages and create the `dvc.yaml` file. 
If any variable names are changed or the code is changed, refer to the `comments.txt` file and make corresponding changes before running them.

# Information about the files
* The python file `download.py` downloads the `n_locs` number of files to a folder named `ncei_data`.
* The python file `prepare.py` file creates the **ground truth** (GT) data.
* The python file `process.py` file creates the calculated data.
* The python file `evaluate.py` file computed the R2 scores for the columns for each CSV file.
* The output `R2results.csv` file has the index as the number of the CSV file (if 1, then 1st file in the *ncei_data* folder).
 
