# Lap4-code-challenge

## Installation & Usage

### Installation

* Clone or download the repo.
* Open terminal and navigate to repo folder.
* run `pipenv install -r requirements.txt` to install dependencies
* then run `pipenv shell` to enter the virtual environment
* Alternatively install with your package manager of choice using the provided `requirements.txt`

### Usage

* Run `pipenv run dev` to launch the dev server.
* Run `pipenv run start` to launch a production server with gunicorn.
* Note that the database is created locally when the app is run, and gets stored in a file called `urls.db`

## Wins & Challenges

### Wins

* being able to go to the site using the shorten link
* being able to display the base url without hard coding it

### Challenges

* finding out what request method gave us the correct base url so we could prepend it to the url returned to the user
