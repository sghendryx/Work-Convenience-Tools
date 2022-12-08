This script opens the human files in your locally cloned identity repo from a list of
names/emails in a CSV (names.txt).

In order to get it to work on your machine, you need to replace this file
path every time it occurs:

/Users/solveighendryx/GitHub/infrastructure-it-terraform-okta-identity/users_and_groups/humans/{name}.tf

With a file path to your locally stored human file, but replace the name with {name}.
The {name} bit will be replaced by the names generated from your CSV.

Once you've made that edit, you run:
python3 mass_user_info_get.py

and follow the instructions!