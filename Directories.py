import os


def main():

    path = os.getcwd()

    print("Current working directory: " + path)

    while True:

        directory = input("Pleas enter the directory that you would like to save a file too: ")

        try:
            os.chdir(directory)
            print("Current working directory: " + os.getcwd())
            break
        except FileNotFoundError:
            print("Directory " + directory + " does not exist.")

    while True:

        file = input("Please enter the file name that you would like to create: ")

        try:
            newfile = open(file, "x")
            break
        except FileExistsError:
            overwrite = input("File " + file + " already exists. Would you like to overwrite this file?")
            if overwrite == "yes":
                newfile = open(file, "w")
                break
            else:
                continue

    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    phone = input("Please enter your phone number: ")

    newfile.write("Name: " + name + ", Address: " + address + ", Phone Number: " + phone)

    newfile.close()

    print("The following is the contents of your new file. Please ensure it is correct.")

    with open(file, "r") as f:
        contents = f.read()

        print(contents)


main()
