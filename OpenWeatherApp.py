#api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={your api key}
#d3f8192e5f827795c239865973932858
# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
def GetCurrentWeather():
    # Enter your API key here
    api_key = "d3f8192e5f827795c239865973932858"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Give city name

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "?zip=23666,us&appid=d3f8192e5f827795c239865973932858"

# get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    #print(x)
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found


    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]

    # store the value of "weather"
    # key in variable z
    #z = x["feels_like"]
    wind = x["wind"]
    wind_speed =wind["speed"]
    weather = x["weather"]
    description = str(weather[0]["description"])

    return("The current temperature is " +str(int((float(current_temperature)-273.15)*9/5+32))  +
      ". The humidity (in percentage) is " +
                str(current_humidiy)+ ".  and the wind speed is "+str(wind_speed) + ".   Today it will be " + description)


def GetHourlyForecast():
    # Enter your API key here
    api_key = "d3f8192e5f827795c239865973932858"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/forecast?zip=94040,us&appid=d3f8192e5f827795c239865973932858"

# get method of requests module
    # return response object
    response = requests.get(base_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    return x
