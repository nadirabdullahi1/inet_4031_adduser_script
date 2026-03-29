#!/usr/bin/python3

# INET4031
#Nadir Abdullahi
# 3/29/2026
# Date Last Modified

#this is importing os, re, and sys into the file these will help with system level commands, regular expressions, and reading input
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        #  checking if the line starts with a pound this symbol is used to mark comment lines in the file
        match = re.match("^#",line)

        #- this splits each line into seperate values using the : so we can extract username, passwords 
        fields = line.strip().split(':')

        #  this line is checking to see if the  line is a comment or does not have 5 fields, if either are true it gets skipped 
        if match or len(fields) != 5:
            continue

        # - these lines assign values from the input file to variables such as username,password, etc
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # - this splits the group field into multipple groups using commas so the user can be added  to multiple groups 
        groups = fields[4].split(',')

        #- this prints a statement to show which user account i sbeing created 
        print("==> Creating account for %s..." % (username))
        # - this creates the linux commmand that will be used to add a new user with no password  and assign them thier name 
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print(cmd)
        os.system(cmd)

        #prints a message showing password has beeen set for the user 
        print("==> Setting the password for %s..." % (username))
        #this creates a command that sets the users passsword using echo and passwd.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)


        #print(cmd)
        os.system(cmd)

        for group in groups:
            #this checks if the group is not empty  and if valid assigns the user to that group 
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
