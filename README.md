# News-App
This python flask framework  News-App project was  created on 28/02/2022

## Author

[Ian Otieno](https://github.com/ian-otieno)

 ## Description
A web application built using Python framework (Flask) NEWS API and application deployed to heroku. The app shows information about news articles from popular sources, top headlines around the globe, provides news categories and the various sources available for the user.

## Live Demo
Click on the link below to view the site:https://ianonewsapp.herokuapp.com/

## Requirements
The user can perform the following functions:
- See various news sources on the homepage of the application
- Select a news source and see all news articles from the selected news source in the application.
- See the image, description and the time a news article was created.
- Click on an article and read the full article on the source website.

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- flask
## Technologies Used
- python 3.8.10
## Project Setup Instructions
1) Git clone the repository
```
https://github.com/ian-otieno/News-App.git
```
2. cd into News-App
```
cd  News-App
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Execute run.py
```
run.py
```

## Behaviour Driven Development
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Displays news headlines|**on page load**|shows news headlines 0n the page
| Display articles from a news source | **Click a news source** | Redirected to a page with articles from the source |
| Display news sources | **On page load** | List of various news sources is displayed in a list |
| Display tabs with news by category | **On Tab link click** | Clickable links to open news based on category which is comprised of business, sports,health,technology and entertainment each displays news when clicked on the nav toggle bar |
| To Read an entire article  | **Click an article** | Redirected to the news source's site to read the entire article |

## Known Bugs
- There are no known bugs

## Contact Information
If you have any question or contributions, please find me on [Gmail](ian.otieno@student.moringaschool.com)

  &#169; 2022 Ian Otieno
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)




   
