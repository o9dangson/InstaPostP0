# InstaPost

Instapost is an online web service that allows users to plan and log their day to day lives in an effort to enhance their quality of life.


## Prerequisites

In order to run the program off of this repo, there are a few installments required.

1. `psycopg2`
    - `pip install psycopg2`
    - This program stores user data on an online aws account database.
2. `virtualenv`
    - `pip install virtualenv`
    - Virtual environment for preventing corruption of files in working environment
3. `python`
    - The basis of most functioning code. Most versions will do. But `python3` is the most up to date version.
4. `flask`
    - `pip install flask`
    - Without flask, you won't be able to run this on a browser.
5. `pytest`
    - `pip install pytest`
    - Unit tests are written in python and can be run with `pytest` command.
6. `Postgresql`
    - Code runs using postgresql database on an AWS account. you will need to create a database in order to run correctly.    

## Setup

After cloning the repo, there are a few extra steps that need to be done in order to set up the environment.
1. `database/connection.py`
    - this file contains the details for connecting to your AWS database. Replace the details using your own database that you created on your AWS account.
    - Naturally, you need to make sure the three tables on the database exist prior to starting the program.
    - `setup()` : this function exists to help the process. If you run into errors, simply copy and past the `qry` into a terminal that you logged on mannually using `psql` command.
2. `virtualenv venv`
    - creates a virtual environment for the code to run. Do this in the folder you cloned the repo in.  
3. `source venv/Scripts/activate`
    - creates a virtual environment for the code to run. Do this command in the same location as step 2.

## Testing/Debugging

- `pytest` : You will need fresh tables in order to pass the tests. `DROP` and `CREATE` them once more before doing so.
- `logs.txt` : all requests while the program is running are logged to this file.
  
## Running the Code

-   `python app.py`

## Trello Board
User Stories, and Sprint Outline
https://trello.com/b/aez6STia/kanban-p0