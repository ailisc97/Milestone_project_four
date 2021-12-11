# Milestone Project 4

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## Table of Contents
* [Purpose](#Purpose)
* [User Experience Design (UX)](#User-Experience-Design)
  * [User stories](#User-Stories)
    * [First Time Visitor Goals](#First-Time-Visitor-Goals)
    * [Returning Visitor Goals](#Returning-Visitor-Goals)
    * [Frequent User Goals](#Frequent-User-Goals)
  * [The Scope Plane](#The-Scope-Plane)
  * [Structure](#Structure)
  * [Design](#Design)
    * [Colour Scheme](#Colour-Scheme)
    * [Typography](#Typography)
    * [Wireframes](#Wireframes)
    * [Database Design](#Database-Design)
    * [Security](#Security)
* [Limitations](#Limitations)
- [Features](#Features)
    * [Existing Features](#Existing-Features)
    * [Future Features](#Features-Left-to-Implement)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Test Strategy](#Test-Strategy)
    * [Test Results](#Test-Results)
* [Deployment](#Deployment)
    * [Project Creation](#Project-Creation)
    * [GitHub Pages](#Using-Github-Pages)
    * [Locally](Run-Locally)
    * [GitHub Pages](#Deployment-To-Heroku)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)
  * [Comments](#Comments)


## Purpose
This website was created for Milestone Project 4 in the Software Development Course for Code Insitute. The languages used in the project are the languages which have been thought in the course up until now, which include, HTML, CSS, JS, User Centric Design, Interactive Front End Development, Python Essential, Backend Development and Full Stack Frameworks with Django.

The live website can be found on Heroku [here](https://ailisc97-milestone-projectfour.herokuapp.com/)

## Curran Fitness Website

![Website Mockup](static/images/Capture.PNG)


Curran Fitness, is a website in which users can find an exercise course or even workout gear for your exciting new transformation. Users have accounts, and they have an area to write blogs about the courses or the workout gear. People can also leave comments on the blog. This project is for the Milestone Project Four which has python, backend technology, in the form of Heroku and also Full Stack Framworks with Django.



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## User Experience Design

### User stories
#### First Time Visitor Goals
* As a First Time user,I want to easily and quickly navigate the website to fitness courses.
* As a First Time user,I want to easily and quickly navigate the website to fitness equipment.
* As a First Time user,I want to easily and quickly navigate the website to fitness clothes.
* As a First Time user, I want to easily and quickly navigate search for different products.
* As a First Time user, I want to easily and quickly navigate to the special offers.

#### Returning Visitor Goals
* As a Returning User, I want to see new courses and products by filters.
* As a Returning user, I want to set up an account.

#### Frequent Visitor Goals
* As a Frequent user, I want write a blog on my fitness course.
* As a Frequent user, I want comment on other peoples blog.

### **The Scope Plane**

**Features planned:**
* Responsive design.
* Website title and information on the site purpose.
* Navigation Menu (Site Wide).
* Django databases to store event information and user login/profile information.
* Login functionality.
* Logout functionality.
* Account functionality.
* Blog functionality.
* Comment functionality.
* Stripe functionality.
* Place Page to view all products.
* Options on Nav bar on how to view certain products and the order to view products.

### Structure
All Pages will have a Navigation bar (using Bootstrap) at the top of the Webpage that allows the User to select different products, by certain categories and to search different products.
The purpose of this is to fulfill user story:
> As a First Time user,I want to easily and quickly navigate the website to fitness courses.
> As a First Time user,I want to easily and quickly navigate the website to fitness equipment.
> As a First Time user,I want to easily and quickly navigate the website to fitness clothes.

The search function for the User to search different products.
> As a First Time user, I want to easily and quickly navigate search for different products.
> As a Returning User, I want to see new courses and products by filters.

Users who set up an account would want search the blog and the comments for reviews on the products.
> As a Frequent user, I want write a blog on my fitness course.
> As a Frequent user, I want comment on other peoples blog.

### Design
#### Colour Scheme
The background colour used is white. The home page has a girl doing yoga with an interactive button to check out the products. Each product has a picture of the what is sold, or in terms of the courses its a photo in relation to the course. 

In the blog page (blog.html), the comments page (blog_detail.html), the signup (account_signup) and the login(account_login) the form it's self is a white with black and a user friendly button.

The search bar is in the nav bar (base.html) there is an icon to press to search.

####  Typography
The font on the website is **Lato**. This font was off Google Fonts.

#### Wireframes
Index.html page and Resturant Page Desktop<br>
![Wireframe](static/images/Index&Restaurant_Desktop.jpg)<br>

Place page and Create_resturant page Desktop<br>
![Wireframe](static/images/Place&Create_Desktop.jpg)<br>

Edit_resturant page and Delete_restaurant page Desktop<br>
![Wireframe](static/images/Edit&Delete_Desktop.jpg)<br>

Login and Sign In Desktop<br>
![Wireframe](static/images/Login&Signup_Desktop.jpg)<br>

Index.html page and Resturant Page Phone<br>
![Wireframe](static/images/Index&Restaurant_Phone.jpg)<br>

Place page and Create_resturant page Phone<br>
![Wireframe](static/images/Place&Create_Phone.jpg)<br>

Edit_resturant page and Delete_restaurant page Phone<br>
![Wireframe](static/images/Edi&Delete_Phone.jpg)<br>

Login and Sign In Phone<br>
![Wireframe](static/images/Login&Signup_Phone.jpg)<br>

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#### Database Design
The database being used to store all products and customer information is built into Django and can be accessed by the site administrators by typing "/admin" at the end of the web address.

Here are screenshots of what it looks like:

<img src="media/readme/Django.PNG" style="margin: 0;">
<img src="media/readme/Django1.PNG" style="margin: 0;">

To deploy to Heroku I used the Postgres free package. Heroku Postgres is a managed SQL database service provided directly by Heroku. You can access a Heroku Postgres database from any language with a PostgreSQL driver, including all languages officially supported by Heroku. In addition to a variety of management commands available via the Heroku CLI, Heroku Postgres provides a web dashboard, the ability to share queries with dataclips, and several other helpful features. See more information on Postgres [here](https://devcenter.heroku.com/articles/heroku-postgresql)

<img src="media/readme/Heroku.PNG" style="margin: 0;">

#### Security

Database connection details are set up in an env.py for development, for 
security reasons this is not uploaded to GitHub so that database and connection details are not visible to 
users. In production these are stored in Heroku. 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Limitations
The biggest limitation I faced was that the photos of the products were not loading onto Heroku, I could get the home page photo but none of the product photos would show. To get the photos onto the website I needed to use Cloudinary, this caused a load of issues for me. I needed a lot of help from the tutor suport and with Heroku being down for a day aswell it took quite a long time. 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

## Features
 
### Existing Features
The Nav bar, footer and form were all from Bootstrap.

### Features Left to Implement


## Technologies
  
* HTML
	* This project uses HTML as the main language used for the Website.
* CSS
	* This project uses CSS to style the Website.
* JavaScript
    * This project uses JS to have the game being able to function and the sendEmail which sends me an email when someone clicks  submit on the form.
* Python
	* This project uses CSS to connect to the background.
    * Python Modules used (These can be found in the requirements.txt project file):
        * asgiref==3.4.1
        * cloudinary==1.28.0
        * dj-database-url==0.5.0
        * dj3-cloudinary-storage==0.0.6
        * Django==3.2.9
        * django-allauth==0.41.0
        * django-countries==7.2.1
        * django-crispy-forms==1.13.0
        * gunicorn==20.1.0
        * oauthlib==3.1.1
        * Pillow==8.4.0
        * psycopg2==2.9.2
        * python3-openid==3.2.0
        * pytz==2021.3
        * requests-oauthlib==1.3.0
        * sqlparse==0.4.2
        * stripe==2.63.0
* [Heroku](https://dashboard.heroku.com/)
	* Heroku is used for the deployment of the website.
* [Cloudinary](https://cloudinary.com)
    * Cloudinary is used to upload the images to Heroku.
* [Bootstrap](https://getbootstrap.com/)
	* The Bootstrap framework is used for Navigation bar, the carousel and the contact us form.
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used throughout the project to import the *Roboto* font.
* [GitPod](https://www.gitpod.io/)
    *GitPod is used to develop the website and where the code for the website was wrote.
* [GitHub](https://github.com/)
	* GitHub is the site used to store the code for the Website and [Git Pages](https://pages.github.com/) is used for the deployment of the live site.
* [Git](https://git-scm.com/)
	* Git is used as software to commit and push code to the GitHub repository where the source code is stored.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements in various different sized. It also helped debug issues and test different CSS styles.
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * tecnisih.com Multi Device Website Mockup Generator was used to create the Mock up image in this README
* [HTML Checker](https://validator.w3.org/nu/)
    * HTML Checker is an important website to make sure there are no errors in the HTML code.
* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator)
    * CSS Checker is an important website to make sure there are no errors in the CSS code.
* [JSHint](https://jshint.com/)
    * JS Checker is an important website to make sure there are no errors in the JS code.
* [Python syntax checker](http://pep8online.com/)
    * Python Checker is an important website to make sure there are no errors in the JS code.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## Testing

### Test Strategy
#### **Summary**
Testing is required on all features and user stories documented in this README. 
All clickable links must redirect to the correct pages. 

HTML Code must pass through the [W3C HTML Validator](https://validator.w3.org/#validate_by_uri).

CSS Code must pass through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

JavaScript code must pass through the [JSHint Validator](https://jshint.com/).

Python Code must pass through [PEP8 Validator](http://pep8online.com/)

All Code passed through the validator.

#### **High Level Test Cases**
![Test Cases](media/readme/TestCases.xlsx)

#### **Access Requirements**
Tester must have access to Heroku and the SuperUser account in order to manually verify the insertion 
of records to users and events collections.

#### **Regression Testing**
All features previous tested during development in a local environment must be regression 
tested in production on the live website.

#### **Assumptions and Dependencies**
Testing is dependent on the website being deployed live on Heroku.


### Test Results

Full test results can be found [here](media/readme/TestCases.xlsx)

****

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## Deployment

### Project Creation
To create this project I used the CI Gitpod Full Template by navigating 
[here](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking the 'Use this template' button.

I was then directed to the create new repository from template page and entered in my desired repo name, then 
clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

* git add . -This would add all the work from the different pages to the GitHub.
* git add index.html -Would only save the work from Index.html
* git pull - This would pull the GitHub version of my project.
* git commit -m "MESSAGE" - This would commit the added work from git add . and leave a message beside it.
* git push- This pushed the added work to GitHub
* python3 -m http.server - This opened the website on the right hand side of the page.


### Using Github Pages
1. On the GitHub [Repository:](https://github.com/ailisc97/Milestone_project_four)
1. Click the 'Settings' Tab on the right hand side.
1. Click on options.
1. Scroll Down to the Git Hub Pages Heading.
1. Select 'main' as the source.
1. Click the Save button.
1. Click on the link to go to the deployed page

### Run Locally
**Note: The project will not run locally with database connections unless the user sets up an [env.py](https://pypi.org/project/env.py/) file configuring IP, PORT, 
HEROKU_URI, MONGO_DBNAME and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository 
for security purposes.**
1. On the GitHub [Repository:](https://github.com/ailisc97/Project_Milestone_3)
1. Click on the download code button, you will get options to clone the GitHub Repository or Download the Zip file.
1. If you downloaded the zip file open the file using one of your IDE application.
1. Or if you choice to clone the GitHub Repository, then open up a terminal and get to a directory of your choice then type in "git clone" followed by the GitHub Repository URL.
1. The clone will be created on your loacal machine. 

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:
> pip install -r requirements.txt


URL to deployed Heroku [here](https://resturant-places.herokuapp.com/home)

### Deployment to Heroku

**Create application:**
1. Navigate to Heroku.com and login.
1. Click on the new button.
1. Select create new app.
1. Enter the app name.
1. Select region.

**Set up connection to Github Repository:**

1. Click the deploy tab and select GitHub - Connect to GitHub.
1. A prompt to find a github repository to connect to will then be displayed.
1. Enter the repository name for the project and click search.
1. Once the repo has been found, click the connect button.

**Set environment variables:**

Click the settings tab and then click the Reveal Config Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (database name you want to connect to)
4. key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and 
    dbname that you set up in the link).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).

**Enable automatic deployment:**
1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## Credits

### Code
Code for the Navigation bar and the footer was taken from [Bootstrap](https://getbootstrap.com/).

I took insperation from the mini project which was completed with the college. <br>

### Content
Content was created by Ailis Curran.

### Acknowledgements
I would like to thank my mentor Spencer Barriball for all his help throughout the project.

### Comments
README.md insperation was taken from my previous Milestone Project. It gave me a template to complete my README, all README content is my own.