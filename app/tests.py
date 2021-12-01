import json

from graphene_django.utils.testing import GraphQLTestCase

from graphql_relay import from_global_id, to_global_id

from swapi.schema import schema
from .models import Planet, Film
from .types import PlanetType, FilmType


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)

    def test_create_people(self):
        response = self.query(
            '''
            mutation createPeopleMutation($people:CreatePeopleMutationInput!){
              createPeopleMutation(input:$people){
                people{
                  name,
                  height,
                  homeWorld{
                    id,
                  }
                }
              }
            }
        ''', variables={
                'people': {
                    'name': "new player",
                    'height': 1800,
                    'homeWorld': "UGxhbmV0VHlwZTox",
                    'films': [
                        {'id': "RmlsbVR5cGU6MQ=="}
                    ]
                }
            }
        )
        self.assertResponseNoErrors(response)
        # converts json response to python object
        content = json.loads(response.content)
        expected_response = {
            "data": {
                "createPeopleMutation": {
                    "people": {
                        "name": "new player",
                        "height": "1800",
                        "homeWorld": {
                            "id": "UGxhbmV0VHlwZTox",
                        }
                    }
                }
            }
        }
        self.assertEqual(expected_response, content)
