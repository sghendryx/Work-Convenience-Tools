# I was running into an issue at work where I needed to look up the role, or the user's employee status (active/inactive) on several users at once,
# but there was no convenient way in which to do that. We store our users in a repo in something my company calls a human file. At the end
# of the file path, it has a name in a first.last format. I'd have to go into each file by searching, copying the info I wanted, and keep track
# of it in a separate spreadsheet. It was pretty tedious and time consuming.
#
# This code takes a list of Firstname Lastnames or emails in a CSV format, removes any unnecessary characters (white space, commas, @mycompanydomain.com)
# in order to turn it into the first.last format, and then subsitutes that variable in the file path to know which file I want it to open.
#
# It opens the human file, reads the file line by line, prints the lines(information) that I need it to, and returns it in a human friendly format.
# Any name it doesn't find a file for, it adds it to a separate list and prints it at the bottom for me to look at to see if there was a typo or
# anything like that.
#
# The most common tasks I use this for would be setting up RBAC (needing to know the consistencies between roles/departments), or doing an audit.
# The script asks you if you'd like their employee status or their role information, and returns the specified info for you. Pretty cool!

import csv
import os.path

user_list = []
human_files = []
users_not_found = []

# Reads a CSV list of either First and Last names or e-mails (it can detect which one it is-- it can also be a mixture of both),
# and adds them to the user_list variable in a first.last format:
with open('names.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=' ')
    for row in file:
        row = ('.'.join(row))
        row = row.replace("@redcanary.com", "")
        row = row.replace(",", "")
        row = row.replace(" ", "")
        user_list.append(row)

# Lower-cases our list of names and assigns them to the human_files variable:
for user in user_list:
    lowercase = user.lower()
    human_files.append(lowercase)

# Convenience functions to define what information we want it to report. It finds the index and prints it from the specified human file.

# Prints the current status of an employee: do they still work here?
def print_user_status(name):
    file = open(f' #insert file path to your human file, but replace the human file name with {name} ')

    user_status_index = 3
    first_name_index = 8
    last_name_index = 9

    content = file.readlines()

    print(content[first_name_index] +
          content[last_name_index] + 
          content[user_status_index])

# Prints all information about a User's role and their manager.
def print_user_information(name):
    file = open(f' #insert file path to your human file, but replace the human file name with {name} ')

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
        if os.path.exists(f' #insert file path to your human file, but replace the human file name with {name} ') == True:
            print_user_information(name)

        else:
            users_not_found.append(name)

elif answer == "User Status" or answer == "user status":
    for name in human_files:
        if os.path.exists(f' #insert file path to your human file, but replace the human file name with {name} ') == True:
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
