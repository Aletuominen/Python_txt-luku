import re

# Script for handling word lists with .txt files
# Aleksi Tuominen

def main():

    while True:

        with open("sanat.txt", "r") as file:

            command = raw_input("Enter command: ")
            command = command.lower()

            if command == "exit":
                file.close()
                return
            elif command == "list":
                for rivi in file:
                    rivi = rivi.rstrip()
                    print(rivi)

            elif command == "add":

                file.close()
                file = open("sanat.txt", "a")
                newline = raw_input("Enter line to add: ")
                newline = newline.lower()

                if re.search('[a-z]+', newline) and len(newline) >= 3:
                    newline += "\n"
                    file.write(newline)
                else:
                    print("Line must be at least 3 characters long and contain letters a-z")
                file.close()

            elif command == "remove":

                file.close()
                file = open("sanat.txt", "r+")
                line_to_remove = raw_input("Enter line to remove: ") + "\n"

                lines = file.readlines()
                file.seek(0)
                if line_to_remove in lines:
                    for line in lines:

                        if line != line_to_remove:
                            file.write(line)
                    file.truncate()
                else:
                    print("Line doesn't exist!")

                file.close()

            else:
                print("Invalid command!")

main()