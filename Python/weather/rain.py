import pywapi

weather = pywapi.get_weather_from_weather_com('CAXX0151')

rain = weather["current_conditions"]["humidity"]

print rain


# CAXX0151