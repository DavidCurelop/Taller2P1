from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construct the full path to the JSON file
        # Asegúrate de que la ruta relativa esté correcta con respecto a DjangoProjectName.
        # El path relativo al archivo movies_descriptions.json en la carpeta DjangoProjectName sería la carpeta anterior 
        # json_file_path = "movies/movies_descriptions.json"
        json_file_path = 'movie\management\commands\movies.json'
        
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)
        
        # Add movies to the database
        for i in range(100):
            movie = movies[i]
            # Asegura que la película no exista ya en la base de datos
            exist = Movie.objects.filter(title=movie['Title']).first()
            if not exist:
                Movie.objects.create(
                    title=movie['Title'],
                    image='images\default.jpg',  # Asegúrate de que este path está correcto y que la imagen existe.
                    genre=movie['Main Genres'],
                    year=movie['Release Year']
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully added {} movies to the database'.format(len(movies))))
