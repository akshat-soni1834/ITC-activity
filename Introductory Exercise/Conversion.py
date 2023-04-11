num = float(input("Enter a number: "))
unit = input("Enter the unit of measurement for the number: ")
target_unit = input("Enter the unit of measurement to convert to: ")

if unit == "feet":
    factor = 0.3048
elif unit == "miles":
    factor = 1609.34
elif unit == "inches":
    factor = 0.0254
converted_num = num * factor
print(num, unit, "is equal to", converted_num, target_unit)