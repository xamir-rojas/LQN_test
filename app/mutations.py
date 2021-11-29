"""Mutations
Modify server-side data
"""
import graphene
from graphql_relay import from_global_id

from .models import Planet, People
from .types import PlanetType, PeopleType
from .utils import generic_model_mutation_process


class CreatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        # Input arguments for the mutation
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    # response of the mutation
    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        # Gets id from input or leaves it in None
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        #
        if raw_id:
            # from_global_id :
            # takes the raw_id and returns the Type name and ID used to create it
            # saves in data.id the ID of the Type
            data['id'] = from_global_id(raw_id)[1]
        planet = generic_model_mutation_process(**data)
        # Returns Planet instance
        return CreatePlanetMutation(planet=planet)


class CreatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.String(required=False)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=False)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=False)
        home_world = graphene.ID(required=True)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_home_world_id = input.get('home_world')
        home_world_id = from_global_id(raw_home_world_id)[1]
        input['home_world'] = Planet.objects.get(id=home_world_id)
        people = People(**input)
        people.save()
        return CreatePeopleMutation(people=people)


class UpdatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.String(required=False)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=False)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=False)
        home_world = graphene.ID(required=False)
    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        # Gets id from input or leaves
        raw_id = input.get('id')
        raw_home_world_id = input.get('home_world',None)
        # If there is a home world to update get the object
        if raw_home_world_id:
            home_world_id = from_global_id(raw_home_world_id)[1]
            input['home_world'] = Planet.objects.get(id=home_world_id)
        data = {'model': People, 'data': input}
        data['id'] = from_global_id(raw_id)[1]
        people = generic_model_mutation_process(**data)
        return UpdatePeopleMutation(people=people)
