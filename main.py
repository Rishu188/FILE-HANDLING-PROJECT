from pathlib import Path
import os

def read_files_and_folders():
    # Display all files and folders from current directory (recursively)
    path = Path('')  
    items = list(path.rglob('*'))  
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def create_file():
    # Create a file with user input (only if it doesn’t already exist)
    try:
        read_files_and_folders()
        name = input("Please enter your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file? ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists.")
    except Exception as err:
        print(f"An error occurred: {err}")


def read_file():
    # Open and read the contents of a file
    try:
        read_files_and_folders()
        name = input("Which file do you want to read? ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print("\n--- FILE CONTENT START ---")
                print(data)
                print("--- FILE CONTENT END ---\n")
            print("Read successfully.")
        else:
            print("The file does not exist.")
    except Exception as err:
        print(f"An error occurred: {err}")


def update_file():
    # Update a file: rename / overwrite / append
    try:
        read_files_and_folders()
        name = input("Which file do you want to update? ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 to rename the file.")
            print("Press 2 to overwrite the file content.")
            print("Press 3 to append content to the file.")

            res = int(input("Enter your choice: "))

            if res == 1:
                new_name = input("Enter the new file name: ")
                p2 = Path(new_name)
                p.rename(p2)
                print("File renamed successfully.")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter new content to overwrite the file: ")
                    fs.write(data)
                print("File overwritten successfully.")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Enter content to append: ")
                    fs.write(" " + data)
                print("Content appended successfully.")
            else:
                print("Invalid option selected.")

        else:
            print("The file does not exist.")
    except Exception as err:
        print(f"An error occurred: {err}")


def delete_file():
    # Remove a file permanently if it exists
    try:
        read_files_and_folders()
        name = input("Which file do you want to delete? ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("File removed successfully.")
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An error occurred: {err}")


# ------ MAIN PROGRAM ---------
print("File Management System")
print("Press 1 to create a file")
print("Press 2 to read a file")
print("Press 3 to update a file")
print("Press 4 to delete a file")

try:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_file()
    elif choice == 2:
        read_file()
    elif choice == 3:
        update_file()
    elif choice == 4:
        delete_file()
    else:
        print("Invalid choice. Please select between 1-4.")
except ValueError:
    print("Invalid input. Please enter a number.")
