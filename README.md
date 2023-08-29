# American Red Cross Branch Location Scraper

The American Red Cross has a vast real estate footprint across the country. As these locations can change over time, it can be difficult to maintain up-to-date list of these locations and their contact information. 

This scraping tool leverages the BeautifulSoup Python library to loop over a list of pages on the [American Red Cross](www.redcross.org) webpage that records each location per region and saves the output to a local CSV. 

## Geocoding

In addition to looping over the pages to grab addresses, this script optionally allows you to geocode them as well. When setting the configuration for `geocoding` to `True`, the script will also send the addresses it finds to the Google Maps API to get the latitude and longitude for each. Note that this requires you to create a local `.env` file and put your Google Maps API key inside it. Make sure you label the value in the `.env` file as "GOOGLE_MAPS", put the key inside quotes, and don't include any spaces. For example: `GOOGLE_MAPS='pp91YrT54SyDl1asdf84JJJ73sdf1M'` 