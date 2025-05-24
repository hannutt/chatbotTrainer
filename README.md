Project keywords: Python Django, Machine Learning, Chatterbot, File-Handling

This application provides a HTML front-end with Django backend for training a Python Chatterbot. The user can input training data to the chatbot by typing it into a textarea element or from a pre-built text file.

READING DATA FROM A TEXT FILE

The HTML UI has a file selector that uploads the selected file to the root folder of the application. The file contents are then looped over using a for loop and stored in a Python list. The list is passed as a parameter to the chatterbot's ListTrainer class.

READING DATA FROM A PDF FILE

PDF files are read using the PyPDF library. After reading the PDF file, the file data is processed in the same way as in the text file option.

TRANSLATING TRAINING DATA INTO ANOTHER LANGUAGE

For example, a user can create a chatbot that speaks Spanish, even if the user does not know how to write Spanish. The application uses the LibreTranslate API to translate training data from the original language to the desired language. The translation is done using a JavaScript function that sends the original text to the LibreTranslate API using the Fetch method and ultimately receives the translated result. The translated result is placed in a textarea element, which the user can send to the chatterbot as training material by clicking the button element.

USING LOGIC ADAPTERS

The application also allows you to simply chat with the chatbot. If desired, the user can choose which logic adapters they want to use to help with the conversation. The logic adapters are listed on the html page and can be selected by clicking on the checkbox element of the desired adapter.