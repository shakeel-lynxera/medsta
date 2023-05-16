# Medsta

The Job Portal is a dynamic platform designed to provide a LinkedIn-like experience.
It offers a comprehensive range of features for users to explore and engage with.
Users can search and discover job opportunities tailored to their preferences and
qualifications. Additionally, they have the ability to connect with other professionals,
make friends, and engage in meaningful conversations through the built-in chat functionality.
The platform also enables users to create posts, share their thoughts, and engage with 
others through likes and comments. With its robust set of features, the Job Portal
aims to empower users in their professional journey while fostering networking and 
collaboration within the community.


## Tools and Technologies
        PostgresSQL
        Python3
        Django==3.24
        HTML
        CSS
        Bootstrap
        JS
        jQuery
        Ajax

## Running the Project

To run the project, follow these steps:

1. Set up a virtual environment using the command: `python -m venv venv`
2. Activate the virtual environment.
3. Install the required packages by running: `pip install -r requirement.txt`
4. Migrate Database Schema: `python manage.py migrate`
5. Start the Django development server: `python manage.py runserver`
6. Access the website in your browser at: `http://localhost:8000/`


## Directory structure
    .
    |
    |-- authModule
    |-- baselayer
    |-- medsta
    |   |-- settings
    |   |-- urls
    |-- posts
    |   |-- urls
    |   |-- models
    |   |-- views
    |-- users
    |   |-- urls
    |   |-- models
    |   |-- views
    |-- utilies
    |-- requirement.txt
    |-- manage.py

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push the branch to your forked repository: `git push origin feature-name`
5. Open a pull request on GitHub.

Please ensure that your code follows the project's coding conventions and includes appropriate tests.
