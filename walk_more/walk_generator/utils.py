import googlemaps
import random
import math
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def generate_random_location(origin, radius):
    # Get the API key from the environment variable
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    gmaps = googlemaps.Client(key=api_key)

    # Get the latitude and longitude of the origin
    geocode_result = gmaps.geocode(origin)
    if not geocode_result:
        raise ValueError(f"Could not find the location: {origin}")

    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]

    # Generate random offsets within the radius
    dx = random.uniform(-radius, radius)
    dy = random.uniform(-radius, radius)

    # Calculate the new latitude and longitude
    new_lat = lat + dy / 111111
    new_lng = lng + dx / (111111 * math.cos(lat * math.pi / 180))

    # Reverse geocode the new coordinates to get the destination address
    destination = gmaps.reverse_geocode((new_lat, new_lng))[0]["formatted_address"]

    return destination


def generate_walking_route(origin, destination):
    # Get the API key from the environment variable
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    gmaps = googlemaps.Client(key=api_key)

    # Calculate the walking route
    directions_result = gmaps.directions(origin, 
                                         destination,
                                         mode="walking")

    if not directions_result:
        print(f"No walking route found from {origin} to {destination}")
        return None

    # Extract the walking route steps and distance
    steps = directions_result[0]['legs'][0]['steps']
    distance = directions_result[0]['legs'][0]['distance']['text']

    return steps, distance

# # Example usage
# radius = 10000  # Radius in meters

# origin = "2 Green Ln, Malvern, PA, 19355"  # Replace with your specific address

# try:
#     destination = generate_random_location(origin, radius)
#     route_result = generate_walking_route(origin, destination)

#     if route_result:
#         route_steps, distance = route_result
#         print(f"Walking destination: {destination}")
#         print(f"Distance: {distance}")
#         print("Route steps:")
#         for step in route_steps:
#             print(step['html_instructions'])
# except ValueError as e:
#     print(f"Error: {str(e)}")