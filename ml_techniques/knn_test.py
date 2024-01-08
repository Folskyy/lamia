"""Simples implementação da técnica KNN para recomendações de um filme"""

import numpy as np
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']

# lê o arquivo já separando as colunas desejadas
ratings = pd.read_csv("/home/gabriel/Documentos/UTFPR/lamia-material/MLCourse/ml-100k/u.data",
                       sep = '\t', names = r_cols, usecols=[0, 1, 2])

# Agrupamento pelo id do filme
movies = ratings.groupby('movie_id').agg({'rating': ['size', 'mean']})

movie_num_ratings = pd.DataFrame(movies['rating']['size'])

movie_normal_ratings = movie_num_ratings.apply(lambda x: (x-np.min(x)) / (np.max(x)-np.min(x)))
