import sys
   
for line in sys.stdin:

    User = line.split(":")
    if User[0].startswith('#'):
        print(User[0].replace('#', '') + " is skipped because it starts with a hashtag (is commented out)\n")
        break
    print("The user " + User[0] + " has a password of " + User[1] + " and has userid " + User[2] + " and groupid " + User[3].replace('\n',''))
print("End of User Data")
