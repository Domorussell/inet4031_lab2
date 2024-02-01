f = open("/home/noah7/lab2_part1_code/fileprocessor.input", "r")
for x in f:

    User = x.split(":")
    if User[0].startswith('#'):
        print(User[0].replace('#', '') + " is skipped because it starts with a hashtag (is commented out)\n")
        break
    print("The user " + User[0] + " has a password of " + User[1] + " and has userid " + User[2] + " and groupid " + User[3].replace('\n',''))
print("End of User Data")

