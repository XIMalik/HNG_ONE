HNG_ONE

The application I've built is a simple API that returns a dictionary from a GET request, with no parameters or payload. 
Response objects come in a dictionary, in that dictionary are my email, current date & time in ISO format and this github repo link. 
Below is a sample response 

{
    "email": "myemail@gmail.com",
    "current_datetime": "2025-01-29T09:34:02.577313",
    "github_url": "https://www.github.com/HNG_ONE"
}

To run this locally, run:
1. pip install r.txt: To install all project requirements
2. python manage.py migrate: To make migrations
3. python manage.py runserver: To start project
4. Make your request with no payload

HNG_ONE
XIMALIK
