# This is a variation on the mass_user_info_get that takes a list of everyone at the company, takes all of their roles
# from their respective human files and adds them to a list, turns that list into a string, and then counts the role
# you specify with an input. This is useful in cases where we're setting up a new service, and we need to know how much it's gunna cost
# if we assign it to a certain role. If there's 18 Software Engineers, that's going to be 18 licenses.

import csv
import os.path

user_list = []
human_files = []
title_indexes = []

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

# Instructions telling the user how to interact with the script.
print("")
print("Enter the name of the role you would like to know the user count for and press 'Enter'. "
      "(Note: Your input must be exactly how it appears in the human file. Capitalization matters!)")
print("")

# This takes all of the names and opens their respective file in your cloned identity repo, finds the title index, and adds that title index
# to the empty array title_indexes.
for name in user_list:
    if os.path.exists(f'/Users/solveighendryx/GitHub/infrastructure-it-terraform-okta-identity/users_and_groups/humans/{name}.tf') == True:
        file = open(f'/Users/solveighendryx/GitHub/infrastructure-it-terraform-okta-identity/users_and_groups/humans/{name}.tf')
        title_index = 24
        content = file.readlines()
        title_indexes.append(content[title_index])

# This turns our list of objects into a string so that we can count the role we're looking for.
title_indexes = str(title_indexes)

# This prints the number of the number of the specified role by counting it within title_indexes.
print(title_indexes.count('"{}"'.format(input())))
print("")
