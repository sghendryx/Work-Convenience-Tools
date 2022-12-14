import csv
import os

human_files = []
users_not_found = []
user_emails = []

print("")
print("CSV full file path (You can drag and drop the file into Terminal from your Downloads folder):")
print("")
file_path = input()
file_path = file_path.replace(" ", "")

# Opens CSV, and looks for the value '@redcanary.com'. If it finds it, it adds that value
# to our human_files variable.
mycsv = csv.reader(open(f'{file_path}'))
for row in mycsv:
   text = row[1]
   for x in row:
    if '@redcanary.com' in x:
        user_emails.append(x)

# This is just some data clean-up to work with our human files.
for email in user_emails:
    email = email.replace("@redcanary.com", "")
    email = email.replace(" ", "")
    human_files.append(email)

def count_role_occurrences(list_to_use, role_from_list):
    count = 0
    for ele in list_to_use:
        if (ele == role_from_list):
            count = count + 1
    return count

# Converts a list into a dictionary,
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}

    #and then that dictionary into a human-readable CSV.
    with open('my_file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in res_dct.items():
            writer.writerow(row)

role_list = []
def print_user_role(name):

    # Finds the user's human file, opens it, and finds the title index.
    file = open(os.path.expanduser('~') + (f"/GitHub/infrastructure-it-terraform-okta-identity/users_and_groups/humans/{name}.tf"))
    title_index = 24
    content = file.readlines()

    # Adds their role to a list of roles, and cleans up the data.
    role_list.append(content[title_index])
    clean_role_list = []
    for data in role_list:
        data = data.replace("title", "")
        data = data.replace("  ", "")
        data = data.replace("=", "")
        data = data.replace('"', '')
        clean_role_list.append(data)
    
    # The set() function finds all of the unique occurences of the role in the role_list. It's
    # return is an object, though.
    unique_titles_obj = set(clean_role_list)
    # So, this turns that object back into a list for us to continue working with.
    unique_titles = list(unique_titles_obj)

    # Now we need to count how many times every unique_title occurs in the role_list.
    counted_roles = []
    for title in unique_titles:
        count = 0
        for x in clean_role_list:
            if (x == title):
                count = count + 1

        # Add the role and how many times it occurs in the list to the counted_roles array.
        counted_roles.append(title)
        counted_roles.append(count)

    Convert(counted_roles)

for name in human_files:
    if os.path.exists(os.path.expanduser('~') + (f"/GitHub/infrastructure-it-terraform-okta-identity/users_and_groups/humans/{name}.tf")) == True:
        print_user_role(name)
    else:
        users_not_found.append(name)

# Opens the CSV we just generated.
out_path = './my_file.csv'
os.system(f"open {out_path}")
