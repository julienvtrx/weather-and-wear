import requests




#gets the coordinates of the city so that the user only needs to type the name of the city he is interested in
def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=de&format=json"
    response = requests.get(url)
    data_coord = response.json()
    return data_coord

#isolates the lat and lon of the city from get_coordinates while doing a safety check if no city was found
def iso_lat_lon(data_coord):
    if "results" in data_coord and len(data_coord["results"]) > 0:
        lat = data_coord["results"][0]["latitude"]
        lon = data_coord["results"][0]["longitude"]
        return lat, lon  
    else:
        print(f"city not found")
        return None, None

#gets the weather of the city with the lat and long it gets from lat_lon
def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data_weather = response.json()
    return data_weather



#isolates actual temp from get_weather
def iso_temp(data_weather):
    if "current_weather" in data_weather:
        temp = data_weather["current_weather"]["temperature"]
        return temp 
    return None
    
#isolates actual windspeed from get_weather
def iso_wind(data_weather):
    if "current_weather" in data_weather:
        wind = data_weather["current_weather"]["windspeed"]
        return wind  
    return None


#isolates actual rain from get_weather #######doesnt work as it is not given bei the api will need to get it from another one ##will work on it later some day
def iso_rain(data_weather):
    if "results" in data_weather and len(data_weather["results"]) > 0:
        rain = data_weather["results"][0]["rain"]
        return rain  


    
#recommands what to wear based on the actual temp, wind and rain of the city
def clothing_recommands(temp, wind, rain):
    pass




def main():
    #input for the city
    city = input("name of the city: ")


        #gets the data
    coord = get_coordinates(city)
    lat, lon = iso_lat_lon(coord)
    if lat is None: 
        return
    weather = get_weather(lat, lon)




    #isolates the data into what it needs
    temp = iso_temp(weather)
    wind = iso_wind(weather)
    #rain = iso_rain(weather)


    #test
    print(f"\n--- weather in {city} ---")
    print(f"temp: {temp} °C")
    print(f"windspeed: {wind} km/h")


if __name__ == "__main__":
    main()