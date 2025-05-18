Project keywords: Python Django, Machine Learning, Chatterbot

This application provides a HTML front-end with Django backend for training a Python Chatterbot. The user can input training data to the chatbot by typing it into a textarea element or from a pre-built text file.

READING DATA FROM A TEXT FILE

The HTML UI has a file selector that uploads the selected file to the root folder of the application. The file contents are then looped over using a for loop and stored in a Python list. The list is passed as a parameter to the chatterbot's ListTrainer class.