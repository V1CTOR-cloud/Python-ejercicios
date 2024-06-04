y=input('Dime una palabra: ').lower()
if y==y[::-1]: # compara un string | number con su anterior si son iguales
  print('Es un Palíndromo')
else:
  print('No es un Palíndromo')