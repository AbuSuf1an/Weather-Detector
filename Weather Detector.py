import requests
from geopy.geocoders import Nominatim
from geopy import distance
geolocator = Nominatim(user_agent="geoapiExercises")
apiKey = "568113d28b55f36705bce9a75bf63a6f"
baseURL = "http://api.openweathermap.org/data/2.5/weather?"
query = "r"
def run():
    if(query=="s"):
        cityName = input("For which location would you like to know the weather?\n>")
        city1 = cityName
        data = requests.get("https://ipinfo.io/json")
        data = data.json()
        city2 = data["city"]
        l1 = geolocator.geocode(city1)
        l2 = geolocator.geocode(city2)
        location1 = (l1.latitude, l1.longitude)
        location2 = (l2.latitude, l2.longitude)
    else:
        data = requests.get("https://ipinfo.io/json")
        data = data.json()
        cityName = data["city"]
    fullURL = baseURL + "appid=" + apiKey + "&q=" + cityName
    response = requests.get(fullURL)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        currentTemperature = y["temp"]
        weatherDescription = z[0]["description"]
        celcius = currentTemperature-273
        degree_sign = u"\N{DEGREE SIGN}"
        print("Looking up current for the wether for " + cityName)
        print("It is currently " + '{:.2f}'.format(celcius) + degree_sign + " and we have " + str(weatherDescription) + "\n")
        if(query=='s'):
            print("You are " +str(round(distance.distance(location1, location2).km, 2)),  "km away from that location.")
    else:
        print("City not found!")
run()
while(query!="q"):
    query = input("What do you want to do next? (r)efresh, (s)earch for location, (c)urrent location or (q)uit\n>")
    if(query!="q"):
        run()
    else:
        print("Quitting. Goodbye.\n")

#Problems: emoji, distance, my location not exact