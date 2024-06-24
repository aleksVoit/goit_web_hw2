# My Project

# This is a description of my project.

# This folder contain Dockerfile which generate docker image

docker build . -t assistant:0.0.6  

# to run the image with volume use 

docker run -v /assistant/assistant/data:/assistant/data assistant:0.0.6

# to run image terminal use 

docker run -it assistant:0.0.6 /bin/bash


# This folder contain assistant application

# to install use 

pip install .

# application has entry point 'assistant'
#  to run application use command in terminal

assistant

# to work with assistant use next commands

# to add a new contact
Add
# to find a contact
Search
# to edit a contact
Edit
# to load a file
Load
# to remove a contact
Remove
# to save a contact
Save
# find contacts which have birthdays this week
Congratulate 
# to view all contacts
View
# to close assistant
Close

