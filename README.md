   # International Space Station Tracker
    #### Video Demo:  https://www.youtube.com/watch?v=sZhDbbOPxc4
    #### Description: International Space Station Tracker code. This project/code aims to pull live API data for the International Space Station (ISS) location and currently lists the names and numbers of astronauts and cosmonauts on the ISS. The goal is to show the ISS's location on a map while listing the names of the astronauts in the terminal space.

    The main function serves as the primary action point, providing variables to the executable functions named iss_location, display_iss, and iss_crew. These variables are then executed to determine the current location of the ISS. If the craft name matches "ISS", the code imports the current latitude and longitude and displays this information on a map created with the Folium package. Additionally, the code retrieves live data on the names of the crew members currently on the ISS, listing and counting them. This project allows users to visually track the ISS and stay updated on its crew in real-time.

    Functions and what they do
    iss_location -> The iss_location function pulls data from the API available at "http://api.open-notify.org/iss-now.json". The data retrieved from this API is then defined in a dictionary with key and value pairs. The ISS position data is obtained as latitude and longitude, ensuring that this data is in floating-point numbers (including both positive and negative values, with digits before and after the decimal point). This data is displayed in the terminal when the code is executed and also feeds into the display_iss function to show the ISS's location on the map.

    display_iss ->  The display_iss function creates a map using the Folium package, which offers robust functionality for mapping out locations and placing markers. The map includes a marker and an explanation bubble over the ISS's location data. The zoom_start parameter is set to 4, providing a good balance between viewing the ISS's specific location and the overall world map. An icon is added with the code icon=folium.Icon(color='green'), where green is used to mark the exact location of the ISS.
    Once the map is created, it is saved as an HTML file that can be viewed through a browser on a PC or Mac. The HTML file is named "ISS_Location_Tracker.html".

    iss_crew
    The iss_crew function pulls data from "http://api.open-notify.org/astros.json". The data is then added to a dictionary as key and value pairs, where the key is "people" and the value is the data provided by the JSON response. This function also summarizes the crew currently stationed on the ISS. The code sum(1 for person in people if person['craft'] == 'ISS') is used to count the number of crew members on the ISS.

    A list of crew members is created with the code [person['name'] for person in people if person['craft'] == 'ISS'], which gathers the names of all individuals currently on the ISS. All findings are returned to the main function with the statement return people_on_iss, people_list.

    Detailed steps of the code

    Main Function Execution: The main function initializes the process and passes control to the other functions. It serves as the central hub where data is collected and processed.

    Fetching ISS Location: The iss_location function contacts the API, retrieves the current location data of the ISS, and formats this data for further use. It ensures the latitude and longitude are in the correct format and ready for mapping.

    Displaying ISS Location on the Map: The display_iss function uses the latitude and longitude data to plot the ISS's position on a Folium map. It includes a marker with an explanatory bubble to give more context about the ISS's location.

    Retrieving Crew Data: The iss_crew function fetches the current list of astronauts and cosmonauts aboard the ISS. It processes this data into a dictionary and creates a list of names, which is then returned to the main function.

    Output and Visualization: The results, including the map and the list of crew members, are displayed to the user. The map is saved as an HTML file, and the crew list is shown in the terminal.

    By following these steps, the project provides a comprehensive tool for tracking the ISS in real-time and staying updated on its crew members. The use of APIs and the Folium package allows for a dynamic and interactive way to engage with the data.

