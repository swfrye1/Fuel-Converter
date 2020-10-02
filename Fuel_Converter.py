#This section queries the user for MPG
def run_Fuel_Conversion():
    try:
        MPG = float(input("Please enter your fuel efficiency in MPG "))
    except ValueError:
        print ("This is not a number")

    #This section converts MPG to KPL and returns the result

    conversion = 0.4251
    KPL = (MPG * conversion)
    print("Your fuel efficiency in KPL is:")
    print(round(KPL, 2))