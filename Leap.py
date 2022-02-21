Year = int(input("Enter Year..."))
 
leap_year = Year % 4
Century = Year % 100
leap_century = Year % 400

print(leap_year)
print(Century)
print(leap_century)
if Century == 0 : 
    print("Leap Year")
elif leap_year == 0 and Century != 0 :
    print("Year is a leap year")
else:
    print ("Year is not a leap year")