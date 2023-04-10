#problem 1
def colour(n):
if (380<=n<450):
return ('Violet')
elif (450<=n<495):
return ('Blue')
elif (495<=n<570):
return ('Green')
elif (570<=n<590):
return ('Yellow')
elif (590<=n<620):
return ('Orange')
elif (620<=n<=750):
return ('Red')
else:
return ('Inappropriate Value: Wavelength of visible light ranges from 380
to 750 nm only')
n=int(input('Enter wavelength :- '))
print(colour(n))