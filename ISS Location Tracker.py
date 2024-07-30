import folium
import requests

def main():
    # Retrieve latitude and longitude of the ISS
    latitude, longitude = iss_location()
    
    # Display the ISS on a map with the retrieved coordinates
    display_iss(latitude, longitude)
    
    # Print the current location of the ISS
    print(f"Current location of ISS is Latitude: {latitude} and Longitude: {longitude}")

    people_on_iss, people_list = iss_crew()
    print(f"Currently number of people on International Space Station: {people_on_iss}")
    print("List of Astronauts on International Space Station: ")
    for person in people_list:
        print(f'- {person}')

def iss_location():
    # Request current location data of the ISS from the API
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    position = data['iss_position']
    latitude = float(position['latitude'])
    longitude = float(position['longitude'])
    
    return latitude, longitude

def display_iss(latitude, longitude):
    # Create a map centered at the ISS location
    iss_map = folium.Map(location=(latitude, longitude), zoom_start=4)
    
    # Add a marker on the map for the ISS location
    folium.Marker(
        [latitude, longitude], tooltip='International Space Station', icon=folium.Icon(color='green')
    ).add_to(iss_map)
    
    # Save the map as an HTML file
    html_file = "ISS_Location_Tracker.html"
    iss_map.save(html_file)

def iss_crew():
    crew_info = requests.get("http://api.open-notify.org/astros.json")
    crew_data=crew_info.json()
    people = crew_data['people']

    # Count people when craft is == ISS
    people_on_iss = sum(1 for person in people if person ['craft'] == 'ISS')

    # List of people currently on the ISS
    people_list = [person['name'] for person in people if person['craft'] == 'ISS']

    return people_on_iss, people_list

# call the main function
if __name__ =="__main__":
    main()

