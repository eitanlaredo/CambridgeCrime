from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Define the address
address = "1600 Amphitheatre Parkway, Mountain View, CA"

# Get the location
location = geolocator.geocode(address)

# Print the latitude and longitude
if location:
    print(f"Address: {address}")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
else:
    print("Address not found")
