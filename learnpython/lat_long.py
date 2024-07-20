import requests
import pandas as pd

def get_lat_long(api_key, address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            return None, None
    else:
        return None, None

# Load addresses from a CSV file
addresses = pd.read_csv('addresses.csv')  # Ensure your CSV file has a column named 'Address'

# API key for Google Maps Geocoding API
api_key = 'YOUR_API_KEY_HERE'

# Create lists to store the results
latitudes = []
longitudes = []

# Loop through each address and get the coordinates
for address in addresses['Address']:
    lat, lng = get_lat_long(api_key, address)
    latitudes.append(lat)
    longitudes.append(lng)

# Add the coordinates to the DataFrame
addresses['Latitude'] = latitudes
addresses['Longitude'] = longitudes

# Save the results to a new CSV file
addresses.to_csv('addresses_with_coordinates.csv', index=False)
