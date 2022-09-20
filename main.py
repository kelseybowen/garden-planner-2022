import json
from utils import *
import garden

with open("plant_data.json", "r") as plant_data:
    data = json.load(plant_data)


def menu():
    print("Welcome to the garden planner. \nType 't' to get today's date as number.\nType 'c' to check for to do items."
        "\nType 'g' to get info about a plant.\nType 'p' to record a plant as planted.\nType 'a' to add a new plant."
        "\nType 'u' to update an entry.\nType 'e' to exit.\n")
    choice = input("Enter your choice: ").lower()
    if choice == 'c':
        check_dates()
    elif choice == 'g':
        get_plant_info()
    elif choice == 'p':
        plant = input("Which plant was planted? ").title()
        day_planted = input("What day was it planted (mm/dd/yyyy)? ")
        planted(plant, day_planted)
    elif choice == 'a':
        add_new_plant()
    elif choice == 'u':
        update_data()
    elif choice == 't':
        print(f"Today is Day {today_int()}\n")
        menu()
    elif choice == 'e':
        pass
    else:
        print("Invalid entry.")
        menu()


def check_dates():
    """Checks sow dates of all plants and prints ones which are ready to be planted."""
    for plant in data:
        if data[plant]["Start sow"] == 0:
            print(f"No dates given for {plant}.")
        elif int(data[plant]["Start sow"]) <= today_int():
            if data[plant]["Day planted"] != 0:
                pass
            else:
                print(f"It's time to plant {plant}.")
        elif int(data[plant]["Start sow"]) - abs(today_int()) <= 7 and data[plant]["Day planted"] == 0:
            print(f"It's almost time to plant {plant}.")
    print("\n")
    menu()


def add_new_plant():
    """Adds new plant to plant_data"""
    new_plant = input("Enter plant name: ").capitalize()
    method = input("Enter method of planting (direct sow or seedlings): ").lower()
    location = input("Enter location in garden: ").capitalize()
    plants_per_sq = int(input("Enter number of plants per square foot: "))
    start_sow = int(date_to_int(input("Enter start date of sowing for this plant (mm/dd/yyyy): ")))
    end_sow = int(date_to_int(input("Enter end date of sowing for this plant (mm/dd/yyyy): ")))
    planted_yet = input("Has this plant been planted? ").lower()
    harvest = int(input("Enter number of days from planting until harvest: "))
    if planted_yet == 'yes':
        day_planted = int(date_to_int(input("Enter the date planted (mm/dd/yyyy): ")))
        plot_empty = day_planted + harvest
    else:
        plot_empty = 0
        day_planted = 0

    data[f"{new_plant}"] = new_plant_dict(method, location, plants_per_sq, start_sow, end_sow, day_planted, harvest, plot_empty)

    with open("plant_data.json", "w") as write_file:
        json.dump(data, write_file)

    print("Plant info has been recorded.\n")

    menu()


def new_plant_dict(method, location, plants_per_sq, start_sow, end_sow, planted_date_int, harvest, plot_empty):
    new_plant = {
        "Method": method,
        "Location": location,
        "Plants per square": plants_per_sq,
        "Start sow": start_sow,
        "End sow": end_sow,
        "Day planted": planted_date_int,
        "Max time to harvest": harvest,
        "Day plot empty": plot_empty,
    }
    return new_plant


def get_plant_info():
    plants = []
    for item in data:
        plants.append(item)
    print(plants)
    plant = input("Which plant would you like info on? ").capitalize()
    if plant not in data:
        print("Invalid entry.")
        get_plant_info()
    # items = []
    # for item in data["Test"]:
    #     items.append(item)
    # print(items)
    info = input("What info would you like? ").capitalize()
    if info == "Start sow" or info == "End sow" or info == "Day planted" or info == "Ready":
        if data[plant][info] != 0:
            decode_date(data[plant][info])
    elif info not in data[plant]:
        print("Invalid entry.")
        get_plant_info()
    else:
        print(data[plant][info])

    print("\n")
    menu()


def planted(plant: str, day_planted):
    """Takes in plant, takes user input of date a plant was planted, converts to day # out of 365,
    adds to plant_data record. """
    with open('plant_data.json') as file:
        data = json.load(file)
    conv_plant_date = date_to_int(day_planted)
    data[plant]["Day planted"] = int(conv_plant_date)

    data[plant]["Day plot empty"] = int(data[plant]["Day planted"]) + int(data[plant]["Harvest"])

    with open('plant_data.json', 'w') as file:
        json.dump(data, file)

    print("\n")
    menu()


def update_data():
    """Updates plant_data.json"""
    with open('plant_data.json') as file:
        data = json.load(file)

    plant_choice = input("Which plant would you like to update? ").capitalize()
    print(data[plant_choice])
    item_choice = input("Which item would you like to update? ").capitalize()
    updated_data = input("Enter new value: ")
    data[plant_choice][item_choice] = updated_data

    with open('plant_data.json', 'w') as file:
        json.dump(data, file)

    print("Data has been updated.\n")
    menu()

menu()
# print(today_int())




