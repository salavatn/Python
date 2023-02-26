
print("Hello, check options:")

file = open("database4.txt", "a")
file.close()

while True:
    print("\n1. Read Document")
    print("2. Add record")
    print("3. Exit")

    option = int(input("\nSelect option number: "))

    if option == 1:
        with open("database4.txt", "r") as file:
            content = file.read()
            print(content)

    elif option == 2:
        while True:
            print("\nPlease add new records")
            user_firstname = input("First Name:\t")
            user_lastname = input("Last Name:\t")
            user_address = input("Address:\t")

            contact_list = f"{user_firstname, user_lastname, user_address}\n"

            with open("database4.txt", "a") as file:
                file.write(contact_list)

            msg = input("Great! Do want add additional record? (yes/no):\t")
            if msg == "yes":
                continue
            else:
                break

    elif option == 3:
        break

print("Goodbye!")

# Do want add additional record? (yes/no): yes
#
# Please add new records
# Name: Salavat
# Last Name: Nigmatullin
# Address: Turkey/Samsun
#
# Do want add additional record? (yes/no): no
#
# Check options:
# 1. Read document
# 2. Add record
# 3. Exit
#
# Select option number (1, 2, 3): 3
# - Goodbye
