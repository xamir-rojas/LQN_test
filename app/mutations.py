"""Mutations
Modify server-side data
"""
import graphene
from graphql_relay import from_global_id

from .models import Planet
from .types import PlanetType
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
