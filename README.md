[![Build Status](https://travis-ci.org/JoshuaOndieki/ridemyway-api.svg?branch=master)](https://travis-ci.org/JoshuaOndieki/ridemyway-api) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/ae62c8dfec124626a765d1d11d0047db)](https://www.codacy.com/app/JoshuaOndieki/ridemyway-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JoshuaOndieki/ridemyway-api&amp;utm_campaign=Badge_Grade) [![Coverage Status](https://coveralls.io/repos/github/JoshuaOndieki/ridemyway-api/badge.svg?branch=master)](https://coveralls.io/github/JoshuaOndieki/ridemyway-api?branch=master) [![Maintainability](https://api.codeclimate.com/v1/badges/94e6632401a89578389d/maintainability)](https://codeclimate.com/github/JoshuaOndieki/ridemyway-api/maintainability)


# Ride My Way
Ride-my App is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

A few requirements to install, run and test this project.


**Git** : Use git to git clone this project locally. [git](https://git-scm.com/)
**Python-3.6.5**


### Installing
Type `git clone https://github.com/JoshuaOndieki/ridemyway-api.git` in your terminal.
1. Install Python 3.6.5
3. cd to the root dir of this repo `cd ridemyway-api`.
4. Create a virtual env and `pip install -r requirements.txt`
5. Run the app with `python run.py` or `python3 run.py`
6. Checkout the endpoints and test them with a tool like [POSTMAN](https://www.getpostman.com)

## Heroku
This Flask API has been hosted and is live at Heroku here [RideMyWay](https://ridemyway-app.herokuapp.com)

### Deployment
[Check out this step by step guide on how to deploy this app to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

## API ENDPOINTS

EndPoint | Functionality
-- | --
POST `/api/v1/rides` | Creates a new ride
GET `/api/v1/rides` | Fetches all available rides
GET `/api/v1/rides/<ride_id>` | Fetches a single ride
POST `/api/v1/auth/rides/<ride_id>/requests` | Creates a ride request


A Pivotal tracker board was used in planning and managing this project. The board is publicly available [here](https://www.pivotaltracker.com/n/projects/2179581)

## Testing

Run `nosetests --with-coverage --cover-package=ridemyway` to see the coverage and passing tests.
Manually test the endpoints with a tool like [POSTMAN](https://www.getpostman.com) on the endpoints provided above.

## Built With

- Python-3.6.5
- Flask-1.0.2

## Versioning

This project uses tags for release and versioning.
For the versions available, see the [tags on this repository](https://github.com/JoshuaOndieki/ridemyway-api/tags).

## Authors

* **Joshua Ondieki** - *Initial work* - [Joshua Ondieki](https://github.com/JoshuaOndieki)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Andela for this wonderful learning opportunity
* Inspiration
* Andela21 Teammates and facilitators for their support.
