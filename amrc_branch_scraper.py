import requests
from bs4 import BeautifulSoup
import csv
import googlemaps
from dotenv import load_dotenv
import os

# set to false if you don't want to set up geocoding, which requires a Google Maps API key
geocoding = True

list_urls = []
csv_file_path = 'amrc_location_urls.csv'
with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        list_urls.extend(row)

print("Beginning web scraping\n------------------\n")

output = []
for url in list_urls:
    print(url)    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # all divs with class="location-card"
        location_cards = soup.find_all('div', class_='location-card')
        
        for card in location_cards:
            temp_dict = {}
            
            # location name
            h5_element = card.find('h5')
            if h5_element:
                temp_dict['name'] = h5_element.text
                
            # street info
            street_elements = card.find_all('street')
            for street in street_elements:
                temp_dict['street'] = street.text
            
            # city info
            city_elements = card.find_all('city')
            for city in city_elements:
                temp_dict['city'] = city.text
                
            # phone info
            phone_element = card.find('a', class_='card-phone')
            if phone_element:
                temp_dict['phone'] = phone_element.text
                
            output.append(temp_dict)
    else:
        print(f"Couldn't find that branch page. Status code: {response.status_code}")

if geocoding == True:
    # add your google maps key to a local .env file with key labeled: GOOGLE_MAPS
    load_dotenv()
    google_maps_key = os.environ.get('GOOGLE_MAPS')
    gmaps = googlemaps.Client(key=google_maps_key)
    
    print("Beginning geocoding process\n------------------\n")
    
    for place in output: 
        joined_address = place['street'] + ' ' + place['city']
        
        temp_dict = {}
        
        geocode_result = gmaps.geocode(joined_address)
        try:
            place['lat'] = geocode_result[0]['geometry']['location']['lat']
            place['lng'] = geocode_result[0]['geometry']['location']['lng']
        except IndexError:
            place['lat'] = 0
            place['lng'] = 0

keys = output[0].keys()
a_file = open("amrc_branch_locations.csv", "w")
dict_writer = csv.DictWriter(a_file, keys)
dict_writer.writeheader()
dict_writer.writerows(output)
a_file.close()