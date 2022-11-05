import csv
import os.path

user_list = []
human_files = []
users_not_found = []
file_path = #Insert the path of any human file here, but change the user's name to {name}.

# Reads a CSV list of either First and Last names or e-mails (it can detect which one it is-- it can also be a mixture of both), and adds them to the user_list variable in a first.last format:
with open('names.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=' ')
    for row in file:
        if any("@redcanary.com") == True:
            row = ('.'.join(row))
            row = row.replace("@redcanary.com", "")
            row = row.replace(",", "")
            row = row.replace(" ", "")
            user_list.append(row)

        else:
            row = ('.'.join(row))
            row = row.replace(",", "")
            row = row.replace(" ", "")
            user_list.append(row)

# Lower-cases our list of name and assigns them to the human_files variable:
for user in user_list:
    lowercase = user.lower()
    human_files.append(lowercase)

# Convenience functions to define what information we want it to report. It finds the index and prints it from the specified human file.

# Prints the current status of an employee: do they still work here?
def print_user_status(name):
    file = open(f'{file_path}')

    user_status_index = 3
    first_name_index = 8
    last_name_index = 9

    content = file.readlines()

    print(content[first_name_index] + content[last_name_index] + content[user_status_index])

# Prints all information about a User's role and their manager.
def print_user_information(name):
    file = open(f'{file_path}')

    first_name_index = 8
    last_name_index = 9
    division_index = 21
    department_index = 22
    cost_center_index = 23
    title_index = 24
    user_manager_index = 26

    content = file.readlines()

    print(content[first_name_index] +
          content[last_name_index] +
          content[division_index] +
          content[department_index] +
          content[cost_center_index] +
          content[title_index] +
          content[user_manager_index])

# This is just some friendly user interface that allows the user to choose which information they would like to
# return. There's an if/else, too, where if the program doesn't find an associated human file for the name it's
# looking for, it takes that name and adds it to a "user's not found" list, and prints that list in the end for us to
# review.

print("Hello! What information would you like? Role Information or User Status?")
print("Type your answer and hit 'Enter'.")
answer = input()
if answer == "Role Information" or answer == "role information":
    for name in human_files:
        if os.path.exists(f'{file_path}') == True:
            print_user_information(name)

        else:
            users_not_found.append(name)
            print(users_not_found)

elif answer == "User Status" or answer == "user status":
    for name in human_files:
        if os.path.exists(f'{file_path}') == True:
            print_user_status(name)

        else:
            users_not_found.append(name)

else:
    print("I didn't understand that. Try again?")

print("The following is a list of users not found in the humans file.")
print("Check for spelling, and also discrepancies like 'Ben' vs 'Benjamin'.")
print("")
print(users_not_found)
print("")
