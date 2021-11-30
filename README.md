# LQN Technical Test

> The startup focused on transforming the way homebuyers access the best mortgage alternative.

# Part 1 - logic test

1. Develop an algorithm that prints the numbers from 0 to 100. In addition, the word buzz must be printed on the same line if the number is even. If the number is a multiple of 5, the word bazz must be printed on the same line.

    * solution at `logic_test.py` function `numbers_multiplies()`

2. Your task in this exercise is as follows:Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon), and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final letter of thepreceding name. No Pokemonname is to be repeated

    * solution at `logic_test.py`  function `pokemon_subsequent_names()`

### Running the logic test
```sh
python3 logic_test.py 
```
# Part 2 - SW API GraphQL 

An existing application needs to be modified. The application is written in Python and Django, the original scroller is no longer available and it is necessary to add new functionality to the site.

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project
```
git clone https://github.com/gustav0/swapi.git
```

Move into de repo and install dependencies
```
pip install -r requirements.txt
```

Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```

### Running the server
```
python manage.py runserver
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Runing the tests
```
python manage.py test
```

## GraphQl examples of Queries and Mutations: 

### Queries

```graphql
{
  allPlanets(last:4){
  	edges{
      cursor,
      node{
        id,
        name,
        population
      }
    }
	}
}
```

```graphql
{
  allPeople(last:4){
  	edges{
      cursor,
      node{
        id,
        name,
        homeWorld {
          id
        }
      }
    }
	}
}
```

```graphql
{
  planet(id:"UGxhbmV0VHlwZTo3Mw=="){
  	name
	}
}
```

### Mutations

```graphql
mutation($planet:CreatePlanetMutationInput!){
  createPlanetMutation(input:$planet){
    planet{
      id,
      name,
      created,
      population
    }
  }
}
# Query variables
{
  "planet": {
    "id": "UGxhbmV0VHlwZTo3Mw==",
    "name": "planet",
    "population": "300",
    "diameter": "20"
  }
}

```

```graphql
mutation($people:CreatePeopleMutationInput!){
  createPeopleMutation(input:$people){
    people{
      id,
      name,
      height,
      homeWorld{
        id,
        name
      }
    }
  }
}
# Query variables
{
  "people": {
    "name": "new player",
    "height": "180",
    "homeWorld": "UGxhbmV0VHlwZTo3Mw==",
    "films": [
      {"id": "RmlsbVR5cGU6Mw=="}
    ]
	}
}
```

```graphql
mutation($people:UpdatePeopleMutationInput!){
  updatePeopleMutation(input:$people){
    people{
      name,
      height,
      homeWorld{
        id,
        name
      }
    }
  }
}
# Query variables
{
  "people": {
    "id": "UGVvcGxlVHlwZTo5MA==",
    "name": "new player",
    "height": "180",
    "homeWorld": "UGxhbmV0VHlwZTo3Mw=="
	}
}
```