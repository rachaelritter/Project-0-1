AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")
    
def printVehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

def main():
    while True: 
        menu()
        number = input()
        if number == "1":  
            printVehicles()
        elif number == "2":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
            
if __name__ == "__main__":
    main()