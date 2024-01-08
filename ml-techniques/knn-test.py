import numpy as np
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']

ratings = pd.read_csv("/home/gabriel/Documentos/UTFPR/lamia-material/MLCourse/ml-100k/u.data", sep = '\t', names = r_cols, usecols=[0, 1, 2])

movies = ratings.groupby('movie_id').agg({'rating': ['size', 'mean']})

movie_num_ratings = pd.DataFrame(movies['rating']['size'])

movie_normalized_num_ratings = movie_num_ratings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
