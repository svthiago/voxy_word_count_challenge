# Voxy Challenge

## Word Count App

This application counts words in a text. It's assumes the premise that all the words must be separated by whitespace. The processing removes all numbers and special characters. Only regex r'[a-zA-Z]+' groups of characters separated by whitespace are considered a word. Here's an example:
<br>
<br>
![alt text](images/1.png)
<br>
<br>
![alt text](images/2.png)
<br>
<br>

### TODO List:
<br>

1. Install pre-commit hooks
2. Dockerize the application
3. Implement test cases with pytest
4. Better looking user interface using React and MaterialUI

5. Implement a better description of the error when the text input is only whitespaces:

![alt text](images/3.png)

<br>

### Install the project

1. Create a virtual environment<br>
`python3 -m venv env`

2. Activate the virtual environment<br>
`source env/bin/activate`

3. Install the requirements<br>
`pip install -r requirements.txt`

4. Go to the project folder and run the server<br>
`cd project/`\
`python manage.py runserver`

5. Access http://127.0.0.1:8000/words_app/ on your browser
