import os

old_name = input("Enter current file name:")
new_name = input("Enter new file name:")

os.rename(old_name, new_name)

print("File renamed successfully")