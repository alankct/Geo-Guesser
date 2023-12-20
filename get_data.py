# Script to scrape together images from various countries
# Should store images in folders where each folder is a country
import os
import requests
import pandas as pd
import pycountry

# Map country to number of images to get - 39985 total
job_info = {
    "Albania": 150,
    "Andorra": 50,
    "Austria": 500,
    "Belarus": 10,
    "Belgium": 400,
    "Bulgaria": 350,
    "Croatia": 250,
    "Czechia": 400,
    "Denmark": 650,
    "Estonia": 150,
    "Finland": 800,
    "Germany": 1000,
    "Greece": 400,
    "Hungary": 400,
    "Iceland": 250,
    "Ireland": 350,
    "Italy": 1200,
    "Latvia": 200,
    "Lithuania": 250,
    "Luxembourg": 150,
    "Malta": 100,
    "Montenegro": 200,
    "Netherlands": 400,
    "Norway": 700,
    "Poland": 800,
    "Portugal": 400,
    "Romania": 500,
    "Russia": 200,
    "Serbia": 300,
    "Slovakia": 300,
    "Slovenia": 250,
    "Spain": 1200,
    "Sweden": 800,
    "Switzerland": 300,
    "Ukraine": 350,
    "Argetina": 1000,
    "Bolivia": 300,
    "Canada": 2400,
    "Chile": 750,
    "Colombia": 900,
    "Costa Rica": 10,
    "Dominican Republic": 100,
    "Ecuador": 400,
    "Guatemala": 300,
    "Mexico": 1800,
    "Peru": 800,
    "Uruguay": 300,
    "Venezuela": 400,
    "Botswana": 300,
    "Egypt": 5,
    "Eswatini": 300,
    "Ghana": 500,
    "Kenya": 950,
    "Lesotho": 300,
    "Madagascar": 10,
    "Nigeria": 500,
    "Senegal": 450,
    "South Africa": 1900,
    "Tunisia": 350,
    "Uganda": 150,
    "Bangladesh": 250,
    "Bhutan": 50,
    "Cambodia": 400,
    "India": 50,
    "Indonesia": 900,
    "Israel": 400,
    "Jordan": 350,
    "Kyrgyzstan": 250,
    "Malaysia": 1200,
    "Mongolia": 100,
    "Philippines": 750,
    "Singapore": 50,
    "South Korea": 850,
    "Sri Lanka": 400,
    "Taiwan": 800,
    "Thailand": 1200,
    "Turkey": 1000,
    "Vietnam": 400,
    "New Zealand": 700
}
token = "xxxxxxxx"


def get_iso_code(country_name):
    try:
        country = pycountry.countries.get(name=country_name)
        if country:
            return country.alpha_2
        else:
            print(f"Country '{country_name}' not found.")
            return None
    except Exception as e:
        print(f"Error getting ISO code for '{country_name}': {e}")
        return None

def get_images_for_country(country, num_images, coords):

    # Make folder for country if it doesn't exist in data folder
    if not os.path.exists(f"data/{country}"):
        os.mkdir(f"data/{country}")

    # Get images for country
    count = 0
    while count < num_images:

        # Get location for valid street view location
        # Get next row for coords where iso_code matches country
        try:
            iso = get_iso_code(country).lower()
            print(f"Iso code: {iso} for {country}")
            row = coords[coords["iso_code"] == iso].iloc[count]
        except Exception as e:
            print(f"Not enough valid locations for: {country} -  {e}")
            break

        # Get latitude, longitude, and heading
        lat, long, heading = row["latitude"], row["longitude"], row["heading"]

        # Get image
        location = f"{lat},{long}"
        url = f"https://maps.googleapis.com/maps/api/streetview?size=640x640&location={location}&heading={heading}&key={token}"
        try:
            image = requests.get(url).content
        except Exception as e:
            print(f"Error getting image for {country}: {e}")
            continue
        
        # Save image to folder
        with open(f"data/{country}/{count}.jpg", "wb") as f:
            f.write(image)
        count += 1


def get_images(job_info):
    for country, num_images in job_info.items():
        print("Getting images for: " + country)

        # Get valid street view coordinates
        coords = pd.read_csv("streetview_results.csv")

        # Get images for each country
        get_images_for_country(country, num_images, coords)
        print("Done getting images for: " + country)


if __name__ == "__main__":
    get_images(job_info)


