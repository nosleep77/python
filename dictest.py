

user1 = {
  "dirs": ["/var/dir1", "/var/dir2"],
  "max_age" : 5, # in days. alert if files are > and name those files.
  "max_files" : 1000, # raise alert if this is => num of files
  "max_size" : 100, # in GB. alert if any dirs are over this size
}

user2 = {
  "dirs": ["/var/dir1", "/var/dir2"],
  "max_age" : 5, # in days. alert if files are > and name those files.
  "max_files" : 1000, # raise alert if this is => num of files
  "max_size" : 100, # in GB. alert if any dirs are over this size
}

print(user1)
print(user2)

list1= []

list1.append(user1)
list1.append(user2)

print(list1)

print(list1[0]["max_files"])