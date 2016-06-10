import pywapi

weather = pywapi.get_weather_from_weather_com('CAXX0151')

rain = weather["current_conditions"]["humidity"]
moon = weather["current_conditions"]["moon_phase"]["text"]
stablepressure = weather["current_conditions"]["barometer"]["direction"]
pressure = weather["current_conditions"]["barometer"]["reading"]
print "Weather pressure and moons script. By: traBpUkciP"
print "================================================="
print "Moon phase: {}".format(moon)
print "Pressure {} at {}pu.".format(stablepressure, pressure)



# CAXX0151