from functools import reduce
from django.db import models
from model_utils.models import TimeStampedModel


class SimpleNameModel(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Planet(TimeStampedModel, SimpleNameModel):
    """ Planetas del universo de Star Wars """

    rotation_period = models.CharField(max_length=40, blank=True)
    orbital_period = models.CharField(max_length=40, blank=True)
    diameter = models.CharField(max_length=40, blank=True)
    climate = models.CharField(max_length=40, blank=True)
    gravity = models.CharField(max_length=40, blank=True)
    terrain = models.CharField(max_length=40, blank=True)
    surface_water = models.CharField(max_length=40, blank=True)
    population = models.CharField(max_length=40, blank=True)

    class Meta:
        db_table = 'planet'


class People(TimeStampedModel, SimpleNameModel):
    """ Personajes del universo de Star Wars """
    # Gender Choices
    MALE = 'male'
    FEMALE = 'female'
    HERMAPHRODITE = 'hermaphrodite'
    NA = 'n/a'
    # Hair and Eye Color Choices
    BLACK = 'black'
    BROWN = 'brown'
    BLONDE = 'blonde'
    RED = 'red'
    WHITE = 'white'
    BALD = 'bald'
    YELLOW = 'yellow'
    GREEN = 'green'
    PURPLE = 'purple'
    UNKNOWN = 'unknown'

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (HERMAPHRODITE, 'Hermaphrodite'),
        (NA, 'N/A'),
    )

    HAIR_COLOR_CHOICES = (
        (BLACK, 'Black'),
        (BROWN, 'Brown'),
        (BLONDE, 'Blonde'),
        (RED, 'Red'),
        (WHITE, 'White'),
        (BALD, 'Bald')
    )
    EYE_COLOR_CHOICES = (
        (BLACK, 'Black'),
        (BROWN, 'Brown'),
        (YELLOW, 'Yellow'),
        (RED, 'Red'),
        (GREEN, 'Green'),
        (PURPLE, 'Purple'),
        (UNKNOWN, 'Unknown'),
    )

    height = models.CharField(max_length=16, blank=True)
    mass = models.CharField(max_length=16, blank=True)
    hair_color = models.CharField(
        max_length=32, choices=HAIR_COLOR_CHOICES, blank=True)
    skin_color = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(
        max_length=32, choices=EYE_COLOR_CHOICES, blank=True)
    birth_year = models.CharField(max_length=16, blank=True)
    gender = models.CharField(max_length=64, choices=GENDER)
    home_world = models.ForeignKey(
        Planet, on_delete=models.CASCADE, related_name='inhabitants')

    class Meta:
        db_table = 'people'
        verbose_name_plural = 'people'


class Director(SimpleNameModel):
    """ Directores de películas"""

    class Meta:
        db_table = 'director'


class Producer(SimpleNameModel):
    """ Productores de películas"""

    class Meta:
        db_table = 'producer'


class Film(TimeStampedModel):
    title = models.CharField(max_length=100)
    episode_id = models.PositiveSmallIntegerField()  # TODO: Agregar choices
    opening_crawl = models.TextField(max_length=1000)
    release_date = models.DateField()
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, related_name='films')
    producer = models.ManyToManyField(Producer, related_name='films')
    characters = models.ManyToManyField(
        People, related_name='films', blank=True)
    planets = models.ManyToManyField(Planet, related_name='films', blank=True)

    class Meta:
        db_table = 'film'

    def __str__(self):
        return self.title
