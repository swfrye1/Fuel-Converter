try:
    Miles = float(input("Please enter your distance in miles "))
except ValueError:
    print ("This is not a number")

conversion=1.609

Kilometers = (Miles * conversion)
print("Your distance in Kilometers is:")
print(round(Kilometers, 2))