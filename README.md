# Tejas-SCL-maxo

<br>
<!-- Team Logos --!>

<img src="https://ibb.co/86fz4Ty" height=120px/>
 


<!-- Heads -->
  <h1 align="center">Tejas x SCL</h1>
  <h2 align="center">NoteRepo</h2>
  <p align="center">
    All your Cheatsheets, Reference Books and Practice Papers, at One Place!
    <br />
    <a href="#documentation"><strong>Documentation</strong></a>
    <br />
    <br />
    <a href="https://noterepo.herokuapp.com/"target="_blank" rel="noopener noreferrer">View a Live Demo</a>
    · 
    <a href="https://github.com/kan12340987/Tejas-SCL-maxo/issues/new">Report a Bug</a>
    ·
    <a href="https://github.com/kan12340987/Tejas-SCL-maxo/issues/new">Request a Feature</a>
  </p>
</p>

<!-- Logos -->
<br>
<p align="center">
  <a href="https://github.com/kan12340987/Tejas-SCL-maxo/blob/main/README.md">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" alt="Logo" width="80" height="80"> &nbsp;
    <a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>  
    <img src="https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo-shadow.png" alt="Bootstrap logo" width="100" height="80">  
  </a>
<br>
<br>

<!-- Repo detail Stickers -->
<p align="center">                          
    <a href="https://github.com/kan12340987/Tejas-SCL-maxo/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/kan12340987/Tejas-SCL-maxo?style=for-the-badge"></a>
    <a href="https://github.com/kan12340987/Tejas-SCL-maxo/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/kan12340987/Tejas-SCL-maxo?style=for-the-badge"></a>
    <a href="https://github.com/kan12340987/Tejas-SCL-maxo/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/kan12340987/Tejas-SCL-maxo?style=for-the-badge"></a>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#a-note-for-contributors">A Note for the contributors</a></li>
        <li><a href="#project-description">Project Description</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#development">Development</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing / Adding features</a></li>
  </ol>
</details>

<br />

<!-- About Project -->

## About the Project

#### A Note for Contributors

```
This is the official project repo for SCL-Maxo, a 40-day Hackathon organised by Sushiksha, World Konkani Center.
The repo is monitored and only members from team Tejas are allowed to make changes. 
Thus, we will not be accepting any PRs from anyone apart from team members. 
For further details, you can get in touch with the repo owner or contributors. 
```


#### Project Description

1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**
3. Database used: **Sqlite**

<!-- Getting started -->

## Getting Started

### Installation 

1. Fork and Clone
    <ol>
    <li>Fork the Tejas-SCL-maxo Repository</li>
    <li>Clone the repo to your local system.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv

    source venv/bin/activate
    ```
   
   If you are using another name for the virtual environment other than `venv`, then please mention it in `.gitignore`.

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
### Development

4. Checkout to a different branch
     ```git
    git status
    git pull
    git branch
    git checkout -b <your-branch-here>
    ```
   
5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a super user.
    In Django, if you want to access admin page, you need to create an account with staff status first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password. You can bypass a common password for development purposes.
   
7. Run the server on localhost:
    ```bash
    python manage.py runserver
    ```

8. Make the changes and send a PR, referencing the changes.
   

## Contributing
   Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change in the project.

<br>
<br>
<br>
<br>

# Documentation

<br>
<br>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#logging-in">Logging In</a>
      <ul>
        <li><a href="#creating-an-account">Creating an account</a></li>
        <li><a href="#logging-options">Logging options</a></li>
        <li><a href="#logging-in-after-sign-up">Logging in after Sign Up</a></li>
        <li><a href="#log-out">Log out</a></li>
      </ul>
    </li>
    <li>
      <a href="#utility">Utility </a>
      <ul>
        <li><a href="#the-home-page">The Home page</a></li>
        <li><a href="#utility-options">Utility Options</a></li>
        <li><a href="#forums">Forums</a></li>
        <li><a href="#contact-us">Contact Us</a></li>
        <li><a href="#profile-section">Profile Section</a></li>
      </ul>
    </li>
    <li>
      <a href="#admin-only-section">Admin only Section</a>
      <ul>
        <li><a href="#adding-new-users">Adding New Users</a></li>
        <li><a href="#adding-resources">Adding resources</a></li>
      </ul>
    </li>
  </ol>
</details>
<br>
<br>

## Logging In
<br>

### Creating an account
<br>

You can create an account on NoteRepo by clicking on the ```Log In``` button on the top right corner of the Main Page

<img src="media\ReadMe Screenshots\Login\MainHomePage.png">

<br>
<br>

### Logging options
<br>

Once in, you should see a ```Sign In``` screen. If you already have an account, you can Sign In directly from here. You can also Sign In through sites like ```Facebook```, ```GitHub```, ```Google``` or ```LinkedIn``` (Note: Some functions could still be under development) Else, you can click on the ```Sign Up``` button towards the left to Sign Up to NoteRepo.

<img src="media\ReadMe Screenshots\Login\SignInScreen.png">

<br>
<br>

### Logging in after Sign Up
<br>

Once in the ```Sign Up``` screen, you can fill in basic details like username and you E-Mail to sign up to NoteRepo. You can also Sign Up through sites like ```Facebook```, ```GitHub```, ```Google``` or ```LinkedIn``` (Note: Some functions could still be under development)

<img src="media\ReadMe Screenshots\Login\SignUpScreen.png">

<br>

```Note: You may be redirected to the Sign In page after signing up. You can sign in by re-entering the details you provided during sign up.```

<br>

Once Logged in, you should be seeing the following landing page. If you do not however, try logging in again.

<img src="media\ReadMe Screenshots\Login\HomePage.png">

<br>
<br>

### Log out
<br>

To log out, click on the the ```Profile``` option on the Navigation Bar towards the top right.
<br>
<img src="media\ReadMe Screenshots\Login\HomePage2.png">
<br>
<br>

This will open up the profile section. From here click on your username on the top right.
<br>
<img src="media\ReadMe Screenshots\Login\ProfileSection.png">
<br>
<br>
From the drop-down menu, click on Logout. This should log you out and take you make to the Home Page.

<img src="media\ReadMe Screenshots\Login\LogOutDropdown.png">



<br>
<br>

## Utility 
<br>

### The Home page
<br>

Once logged in, the landing page will the first thing you will see. This is the hub of the website which includes various option.
<br>
<br>

<img src="media\ReadMe Screenshots\Utilities\HomePage2.png">
<br>
<br>


### Utility Options

**Navigation Bar**
<ul>
<li>Home - Takes you to the Home Page(current page)</li>
<br>
<br>
<li>About Us - Takes us to the about us section of the page</li>
<br>
<img src="media\ReadMe Screenshots\Utilities\AboutUs.png">
<br>
<br>
<li>Forums - Takes you the forum section of the page (under development)</li>
<br>

**```This Feature is currently under Development```**
<br>
<br>
<li>Contact Us - To send us a message</li>
<br>

**```This Feature is currently under Development```**
<br>
<br>
<li>Profile - Takes you to the profile section</li>
<br>
<img src="media\ReadMe Screenshots\Utilities\Profile.png">
<br>
<br>
</ul>


**Main Page**
<ul>
<li>Notes - Takes you to the Cheatsheets/Notes section</li>
<br>
<img src="media\ReadMe Screenshots\Utilities\Cheatsheets.png">
<br>
<br>
<li>References - Takes you to the References/textbooks section</li>
<br>
<img src="media\ReadMe Screenshots\Utilities\References.png">
<br>
<br>
<li>Papers - takes you to the Question papers section</li>
<br>
<img src="media\ReadMe Screenshots\Utilities\Papers.png">
<br>
<br>
</ul>

**You can View and Download any of the listed books by clicking on ```Download```. The links will take you to Google PDF Links and all options provided by Google PDF viewer will be available (requires you to login to you Google account)**

1. The search function is currently under development.
2. The add button is currently under development.

<br>
<br>

### Forums 
**```This Feature is currently under Development```**

<br>
<br>

### Contact Us
**```This Feature is currently under Development```**

<br>
<br>

### Profile Section
<br>

**In this section, the user will be able to add details about himself. All of this data is kept private and not shared with anyone.**
<br>

<img src="media\ReadMe Screenshots\Utilities\Profile.png">

<br>
<br>

## Admin Only Section 
<br>

**This section requires superuser status or staff user permission to be accessed. to know more, visit the Creating a super user section in the <a href="#development">Development</a> tab above.**

**After this you can visit the admin section by adding ```admin``` to the end of the url after host**
eg: 127.0.0.1:8080/admin

<img src="media\ReadMe Screenshots\Admin\Admin.png">

<br>
<br>

### Adding New Users
<br>
There are two way of adding users.
<ol>
<li>Through the normal Sign In page. This directly adds users to the admin section </li>
<li>Adding users through the admin section:

<ol> 
<li>Go to the admin section by following the instructions above.</li>
<br>
<img src="media\ReadMe Screenshots\Admin\Admin.png">
<br>
<br>
<li>Select the users section on the left then select add users on the top right</li>
<br>
<img src="media\ReadMe Screenshots\Admin\AdminUsers.png ">
<br>
<br>
<li>Here you can add details of the user and they will be registered as a user.</li> 
<br>
<img src="media\ReadMe Screenshots\Admin\AdminUsers.png ">
<br>
<br>
</ol>
</li>
</ol>

### Adding resources

**Adding resources like Cheatsheets, Reference books and question papers can only be done by ```Super Users``` or users with ```Staff Status``` and via the Admin section. Refer details about Admin section and Creating a super user above.**

<ol>
<li>Visit the Admin section</li>
<br>
<img src="media\ReadMe Screenshots\Resouces\Admin.png">
<br>
<br>
<li> Choose any of the options from Q Papers, Notes, Textbooks</li>
<br>
<img src="media\ReadMe Screenshots\Resouces\AdminNotes.png">
<br>
<br>
<li>Once selected, you will be presented with a form of details to fill for each of the 3 addable resources, you can fill these up and this, will add a new addab;e to the table.</li>
<br>
<img src="media\ReadMe Screenshots\Resouces\AdminNotesEditor.png">
<br>
<br>
<br>
<img src="media\ReadMe Screenshots\Resouces\QPpapersEditor.png">
<br>
<br>
<br>
<img src="media\ReadMe Screenshots\Resouces\TextbooksEditor.png">
<br>
<br>
</ol>
