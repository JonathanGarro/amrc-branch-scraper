# American Red Cross Branch Location Scraper

The American Red Cross has a vast real estate footprint across the country. As these locations can change over time, it can be difficult to maintain up-to-date list of these locations and their contact information. 

This scraping tool leverages the BeautifulSoup Python library to loop over a list of pages on the [American Red Cross](www.redcross.org) webpage that records each location per region and saves the output to a local CSV. 

## (Optional) Geocoding

In addition to looping over the pages to grab addresses, this script optionally allows you to geocode them as well. When setting the configuration for `geocoding` to `True`, the script will also send the addresses it finds to the Google Maps API to get the latitude and longitude for each. See **Usage > (Optional) Generate Google Maps API key** below.

## Usage

### Create virtual environment

Create a new directory and activate a virtual environment with `python3 -m venv venv`. Activate the virtual environment with `source venv/bin/activate`. 

### Install requirements

With the virtual environment activated, run `pip install -r requirements.txt` to install dependencies.

### (Optional) Generate Google Maps API key

Head to the [Google Maps Developer portal](https://developers.google.com/maps) and create a new project. Save the API key that is generated in a local file in the same directory as this project inside a file called `.env`. Make sure you label the value in the `.env` file as "GOOGLE_MAPS", put the key inside quotes, and don't include any spaces. For example: `GOOGLE_MAPS='pp91YrT54SyDl1asdf84JJJ73sdf1M'`

### Run the script

If you added a Google Maps API key, leave the `geocoding` value on line 9 set to `True`. Otherwise, change it to `False`.

Run the script with `python3 amrc_branch_scraper.py`. The script will take a few minutes to finish, and should generate a new CSV file inside your directory.