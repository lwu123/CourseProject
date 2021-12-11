# CS 410 Course Project
## Part of Speech Identifier
###### Motivation: 

The goal of this project is to use text mining methods to build a service that will help students, who are new to learning English, have an easier time learning part of speech.

Link to the presentation: 
https://drive.google.com/file/d/1Z_gNB8-uix0675qX3x5wjdQBvPIP2k06/view?usp=sharing

The technologies used are:
spacy - pretrained data
Flask
HTML

## How does it work?
Users can enter a word they'd like to look up as shown below:


![image](https://user-images.githubusercontent.com/89817271/145689627-16cb610f-1d97-496a-bd04-c4225aaa3fdc.png)


After hitting the submit button, result will be posted with the part of speech correctly identified.


![image](https://user-images.githubusercontent.com/89817271/145689838-2a77865a-97df-448d-bdba-4968697278d4.png)

To test this out the user must pip install all the neccessary spacy and flask modules using:

pip install Flask
pip install -U spacy
python -m spacy download en_core_web_sm

For more information on the installation of spacy, use this link:

https://spacy.io/usage

###### What is spacy?

spacy is an open source library for natural language processing. It has features such as pos tagging, dependency parsing and is written in Python.

###### What is flask?

Flask is a web framework written in python. With flask, we can use it to set up development servers.

# Components of This Project and How it works:

User's input is captured from an HTML form. Next that data is sent to a function that makes use of the spacy pos tagging model. The information is then rendered back to the user.

