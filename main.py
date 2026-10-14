import requests



##########################################################################################
#moduls to get data from the APIs
##########################################################################################



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
        print("city not found")
        return None, None

#gets the weather of the city with the lat and long it gets from lat_lon
def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data_weather = response.json()
    return data_weather



##########################################################################################
#moduls that isolates the needed data that it gets from the APIs
##########################################################################################



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



##########################################################################################
#actual interesting moduls that you can change to your needs for example you want to wear a t-shirt starting at =>15 degrees celsius
##########################################################################################



#use of windchill function to get the felt temp
def windchill(temp, wind):
    if temp <= 10 and wind > 4.8:
        #windchill function
        effective_temp = 13.12 + (0.6215 * temp) - (11.37 * (wind ** 0.16)) + (0.3965 * temp * (wind ** 0.16))
    else:
        #over 10degrees celsius or over 4.8km/h windspeed, the windchill function has no purpose
        effective_temp = temp
    return effective_temp    


#recommands what to wear based on the actual effective temp, wind of the city
def clothing_recommands(effective_temp):
    if effective_temp >= 18:
        return "t-shirt weather"
    
    elif 15 <= effective_temp < 18:
        return "light sweater (cotton/merino wool) over a t-shirt"
    
    elif 10 <= effective_temp < 15:
        return "thick sweater (hoodie/fleece) + potentially a transitional jacket"

    else:  # Unter 10 Grad
        return "thick wool sweater in layers + warm winter jacket"



##########################################################################################
#main modul that combines the other moduls to actually be useful
##########################################################################################



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


    #uses the data for propositions
    effective_temp = windchill(temp, wind)
    recom = clothing_recommands(effective_temp)



    #output to user
    print(f"\n--- weather in {city} ---")
    print(f"temp: {temp} °C")
    print(f"effective temp: {effective_temp} °C")
    print(f"windspeed: {wind} km/h")
    print(f"you should wear: {recom}")


##########################################################################################
#to import in another project
##########################################################################################
if __name__ == "__main__":
    main()