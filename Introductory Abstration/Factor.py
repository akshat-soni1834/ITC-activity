'''
Complete the Exercises - Representing Abstraction Through Code 
In programming, we deal with two kinds of elements: functions and data. 
Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 
By the concept of abstraction create functions representing abstracting principles through function 
Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)
Note: Naming Convention Files: Crate files based on the purpose of the exercise eg: If calculating factor then use function_factor.py  Submission Guidelines: File Upload (Notepad File, Python File, Console Output Pasted) 
'''

import math

def calculate_wind_chill_factor(wind_speed, temperature):
    # formula to calculate wind chill factor
    factor = 35.74 + 0.6215*temperature - 35.75*math.pow(wind_speed, 0.16) + 0.4275*temperature*math.pow(wind_speed, 0.16)

    return f"The wind chill factor is {factor} degrees Fahrenheit."