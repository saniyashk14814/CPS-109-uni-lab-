temp=float(input("Enter the temperature: "))
unit = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ").strip().upper()
if unit == 'C':
  if temp >= 100:
    print("Water is gaseous")
  elif temp <= 0:
    print("Water is solid")
  else:
    print("Water is liquid")
elif unit == 'F':
  temp_celsius = (temp - 32) * 5 / 9
  if temp_celsius >= 100:
    print("Water is gaseous")
  elif temp_celsius <= 0:
    print("Water is solid")
  else:
    print("Water is liquid")
else:
  print("Invalid input! Please enter 'C' for Celsius or 'F' for Fahrenheit.")