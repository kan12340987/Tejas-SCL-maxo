# Tejas-SCL-maxo
<a href="https://github.com/kan12340987/Tejas-SCL-maxo/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/kan12340987/Tejas-SCL-maxo?style=for-the-badge"></a>
<a href="https://github.com/kan12340987/Tejas-SCL-maxo/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/kan12340987/Tejas-SCL-maxo?style=for-the-badge"></a>
<a href="https://github.com/kan12340987/Tejas-SCL-maxo/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/kan12340987/Tejas-SCL-maxo?style=for-the-badge"></a>

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>

<img src="https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>



#### Project Description

1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**

## Installation 

1. Fork and Clone
    <ol>
    <li>Fork Tejas-SCL-maxo Repo</li>
    <li>Clone the repo to your local system.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    pip install virtualenv
    ```
    ```bash
    virtualenv -p python venv
    ```
    ```bash
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv
    
    source venv/bin/activate
    ```
   
   If you are giving a different name other than `venv`, then please mention it in `.gitignore` first

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
## Development

4. Checkout to different branch
     ```git
    git status
    git pull
    git branch
    git checkout -b < your-branch-here >
    ```
   
5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a super user.
    In django if you want to access admin page, you need to create an account with staff status first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password or use Team credentials
   
7. Run the serve on localhost:
    ```bash
    python manage.py runserver
    ```

8. Make the changes and send a PR referencing the changes.
   

## Contributing/ Adding Features
   Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change in the project.
