# Objective
To understand the use of DVC and git for version control of projects.

# Dataset
he National Centers for Environmental Information (NCEI) maintains a large archive of environmental data that includes oceanic, atmospheric, and geophysical data. The NCEI archives over 229 terabytes of data each month from over 130 observing platforms.
The NCEI also provides archive services for much of the data collected by NOAA scientists, observing systems, and research initiatives. The NCEI manages a comprehensive collection of environmental information from a broad range of time periods, observing systems, scientific disciplines, and geographic locations.

# Task
* Pull `n_loc` number of files from the ncei data website.
* The files contain columns with aggreagates of monthly averages; use this as the *ground truth* data.
* Compute the montly averages using the *hourly* data available in the files.
* Compute R2 scores for the columns for each file.

# Setup
The `dvc stage add` commands are present in `comments.txt`. 
Run these one by one to add stages and create the `dvc.yaml` file. 
If any variable names are changed or the code is changed, refer the `comments.txt` file and make corresponding changes before running them

# Information about the files
