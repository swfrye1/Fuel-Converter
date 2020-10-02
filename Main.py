from Fuel_Converter import run_Fuel_Conversion

selection = float(input("Please choose your program:\n\t1:Fuel efficiency converter \n\t2:Distance converter \n\t3:Data size converter "))

if selection == 1:
    run_Fuel_Conversion()
    #exec(open('Fuel_Converter.py').read())

if selection == 2:
    exec(open('Distance_Converter.py').read())

if selection == 3:
    exec(open('Data_Size_Converter.py').read())

exec(open('Main.py').read())