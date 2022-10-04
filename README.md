
# A1school

This is a simple quiz appplication with a built in dvelopment environment for writing and previewing HTML, CSS and JavaScript codes. 


## Installation and Setup

1. Download or clone the app and open the folder in the cli
2. Create a virtual environment using: 


```bash
  python<version> -m venv <virtual-environment-name>
```
3. Activate virtual environment using:
* for Mac 
 ```bash
  source env/bin/activate
```
* for windows
```bash
  env/Scripts/activate.bat //In CMD
  env/Scripts/Activate.ps1 //In Powershel
```
4. Once the virtual environment is activated, install dependencies using `pip`:
```python
  pip install -r requirements.txt
```
5. Create a `.env` file using the `.env.example` file to fill out the required environment variables.
6. Start the web server using `python manage.py runserver` command. The app will be served at http://localhost:8000/
7. Go to http://localhost:8000/ in your browser to use the app.

## Features
- quiz 
  - User need to register and activate account to be able to take any quiz
  - There are 3 major categories for the quiz - HTML, CSS and JavaScript and each categories have 3 levels - Beginner, Intermediate and Advanced
  - The result of the test and answers are shown in the end when the user submits. This result is also stored in the database.

- Development environment
  - User can write HTML, CSS and JavaScript code and preview in the preview window

- User
  - The user can take test, view results, write on the Development environment, edit profile and change password.
  
- Admin
  - Create new user and quizzes
  - Update user information and quizzes
  - Delete user and quizzes 



## Demo

![Development environment](https://github.com/Dclassicgenius/A1school/blob/master/screenshots/react-app%20gif.gif)
![Home page](https://github.com/Dclassicgenius/A1school/blob/master/screenshots/Screenshot%202022-10-04%20at%2013.32.25.png)

