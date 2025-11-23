def tablespoons_to_teaspoons(tablespoons):
    return tablespoons*3
def cups_to_grams(cups,conversion_rate):
    return cups*conversion_rate
def meters_to_feet(meters):
    return meters*4
def kilograms_to_pounds(kilograms):
    return kilograms*2
def celsius_to_farenheit(celsius):
    return celsius*(9/5)+32

def converter():
    print("welcome to the unit converter")
    while True:
        print("1. convert tablespoons to teaspoons")
        print("2. convert cups to grams")
        print("3. convert meters to feet")
        print("4. convert kilograms to pounds")
        print("5. convert celsius to farenheit")
        print("6. exit the game")
        choice = int(input("enter your choice from 1 to 6 "))
        if choice == 1:
            tablespoons = int(input("enter the amount of tablespoons "))
            result = tablespoons_to_teaspoons(tablespoons)
            print(result,"teaspoons required ")
        elif choice == 2:
            cups = int(input("enter the amount of cups "))
            conversion_rate = int(input("enter the grams per cup required for the recipie "))
            result = cups_to_grams(cups, conversion_rate)
            print(result,"grams required ")
        elif choice == 3:
            meters = int(input("enter the amount of meters "))
            result = meters_to_feet(meters)
            print(result,"feet required ")
        elif choice == 4:
            kilograms = int(input("enter the amount of kilograms "))
            result = kilograms_to_pounds(kilograms)
            print(result,"pounds required ")
        elif choice == 5:
            celsius = int(input("enter the amount of celsius "))
            result = celsius_to_farenheit(celsius)
            print(result,"farenheit required ")
        elif choice == 6:
            print("thank you for using the converter see you next time")
            break
        else:
            print("incorrect choice enter a valid number ")

converter()


            
        
        
        



