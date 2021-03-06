# Politico API

The general elections are around the corner, hence it’s a political season. Get into the mood of
the season and help build a platform which both the politicians and citizens can use.
Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency

[![Build Status](https://travis-ci.com/kipruto/politico-api.svg?branch=develop)](https://travis-ci.com/kipruto/politico-api) [![Coverage Status](https://coveralls.io/repos/github/kipruto/politico-api/badge.svg)](https://coveralls.io/github/kipruto/politico-api)[![Maintainability](https://api.codeclimate.com/v1/badges/3f1a8deeeeab4a8fa0f4/maintainability)](https://codeclimate.com/github/kipruto/politico-api-v1/maintainability)

## Features
1. The API can register users
2. The API can login users
3. The API can create a political party.
4. The API can get all political parties.
5. The API can get a specific political party.
6. The API can edit a specific political party.
7. The API can delete a particular political party.
8. The API can create a political office
9. The API can get all political offices
10. The API can register a user as a candidate
11. The API can get election results per elective office
12. The API can allow a user petition an election outcome
13. The API can allow a user to reset login credentials



## Installation

### Step 1

1. Clone the repository [```here```](https://github.com/kipruto/politico-api)

2. Open terminal application on your local machine

3. On the terminal, run ``` git clone https://github.com/kipruto/politico-api.git ``` command

```$ cd politico-api```

3. Create and activate virtual environment

```$ virtualenv venv```

```$ source venv/bin/activate```

4. Install project dependencies 

```$ pip install -r requirements.txt```

### Step 2

#### Configuring environment variables 

```
export FLASK_APP="run.py"
export FLASK_ENV="development"
export FLASK_DEBUG=1
```

### Step 3

#### Running the application

```$ flask run```

### Step 4

#### Testing

```$ pytest --cov=app tests```

### Version 1 API Endpoints

#### Parties Endpoints : /api/v1/

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/parties``` | Create a political party
```GET``` | ```/parties``` | Get all political parties
```GET``` | ```/parties/int:id``` | Get a specific political party
```PATCH``` | ```/parties/int:id/string:name``` | Edit a political party
```DELETE``` | ```/parties/int:id``` | Delete particular political party

#### Offices Endpoints : /api/v1/

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/offices``` | Create a political office
```GET``` | ```/offices``` | Get all political offices
```GET``` | ```/offices/int:id``` | Get a specific political party


### Version 2 API Endpoints

#### Parties Endpoints : /api/v2/

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/parties``` | Create a political party
```GET``` | ```/parties``` | Get all political parties
```GET``` | ```/parties/int:id``` | Get a specific political party
```PATCH``` | ```/parties/int:id/string:name``` | Edit a political party
```DELETE``` | ```/parties/int:id``` | Delete particular political party

#### Offices Endpoints : /api/v2/

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/offices``` | Create a political office
```GET``` | ```/offices``` | Get all political offices
```GET``` | ```/offices/int:id``` | Get a specific political party
```POST``` | ```/office/int: id/register``` | Register a user as an election candidate
```GET``` | ```/office/int: id/result``` | Collate and fetch results of a specific office 
```GET``` | ```/offices/int:id``` | Get results of an elective office following an election

#### Users Endpoints : /api/v2/

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/auth/signup``` | Create user account
```GET``` | ```/auth/login``` | User login
```POST``` | ```/auth/reset``` | Enables a user to reset login credentials


#### Votes Endpoints : /api/v2/

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/votes/``` | Enables a user vote for a candidate
```GET``` | ```/offices/int:id``` | Get a specific political party
```POST``` | ```/petitions/``` | Enables a user challenge an election's outcome
