# inet_4031_adduser_script

## Description
This Python script automates creating users and assigning them to groups on a Linux system using an input file.

## How to Run

Make executable:
chmod +x create-users.py

Dry run:
./create-users.py < create-users.input

Run for real:
sudo ./create-users.py < create-users.input

## Verification

grep user0 /etc/passwd  
grep user0 /etc/group
