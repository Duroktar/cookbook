import pywapi
#   See if it will rain tonight
weather = pywapi.get_weather_from_weather_com('CAXX9765')  # gets weather
chance = weather["forecasts"][0]["night"]["chance_precip"]
hum = weather["forecasts"][0]["night"]["humidity"]



print chance
print hum
x = int(chance)
y = int(hum)
if x > 50 and y > 50:
    print 'Yes'
else:
    print 'no'