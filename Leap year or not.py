# to check year is lear year or not
year = int(input("Enter your year: "))
if(year % 4==0):
  if(year % 100==0):
    if(year % 400==0):
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")