import sys
# import clipboard
import json

SAVED_DATA = "clipboard.json"
# from click import command


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        # clipboard.copy(input("Enter a value: "))
        data[key] = input("Enter what is It:")
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            print(data[key])
        else:
            print("Key not found")
    elif command == "list":
        print(data)
    else:
        print("unknown command")
else:
    print("Please pass exactly one command")
