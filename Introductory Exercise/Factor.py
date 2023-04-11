import math

wind_speed = float(input("Enter the wind speed in miles per hour: "))
temperature = float(input("Enter the temperature in degrees Fahrenheit: "))

factor = 35.74 + 0.6215*temperature - 35.75*math.pow(wind_speed, 0.16) + 0.4275*temperature*math.pow(wind_speed, 0.16)

print("The wind chill factor is", factor, "degrees Fahrenheit.")