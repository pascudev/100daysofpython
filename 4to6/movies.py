from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

#FIX PARA EL ERROR DE CERTIFICADO SSL
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
test = urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0','')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            if m.year > 4:
                directors[director].append(m)

    return directors

directors = get_movies_by_director()


print(directors)

def dir_movie_chart(directors):
    for d in directors:
        avg_score = 0
        final_avg = 0
        for m in d:
            avg_score = avg_score + m
            final_avg = float(avg_score / len(m), 1)
        return final_avg

pezon = dir_movie_chart(directors)
print(pezon)


cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)
    if len(movies) < 4:
        cnt.pop(director)


def get_directors(movies):
    parsed_directors = []
    for k, v in movies.items():
        parsed_directors.append(k)
    return parsed_directors

directors_list = get_directors(cnt)

#print(directors_list)

def get_target_movies(array):
    target_movies = []
    for d in directors_list:
        target_movies.append(directors[d])
    return target_movies

target_movies_list = get_target_movies(directors_list)
#print(target_movies_list[1])

#for m in target_movies_list:
    #for data in m:
        #print(data.title)





