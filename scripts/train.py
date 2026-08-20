import pandas as pd
import numpy as np
from pathlib import Path
movies = pd.read_csv("movies.csv")
movies[['title', 'genres', 'keywords', 'cast', 'director', 'overview']].head()
movies = movies[
    [
        "title",
        "genres",
        "keywords",
        "cast",
        "director",
        "overview",
        "tagline"
    ]
]
movies.head()
# selecting the relevant features for recommendation

selected_features = ['title','genres','keywords','overview','tagline','cast','director']

# replacing the null valuess with null string

for feature in selected_features:
  movies[feature] = movies[feature].fillna('')

movies["tags"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["cast"] + " " +
    movies["director"] + " " +
    movies["overview"]
)

movies[["title", "tags", "genres"]].head()
new_df = movies[["title", "tags", "genres"]]
new_df.head()
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)
vectors = cv.fit_transform(new_df["tags"])
vectors.shape
vectors.toarray()
cv.get_feature_names_out()
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)
similarity.shape
similarity[0]
movies_list = sorted(
    list(enumerate(similarity[0])),
    key=lambda x: x[1],
    reverse=True
)[1:6]

print(movies_list[:10])
def recommend(movie):

     movie_index = new_df[
     new_df["title"].str.lower() == movie.lower()
     ].index[0]

     distances = similarity[movie_index]

     movies_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
     )[1:6]

     recommendations = []

     for movie in movies_list:
        recommendations.append(
            new_df.iloc[movie[0]].title
        )

     return recommendations

recommend("Avatar")

import pickle
artifact_dir = Path("artifacts/v1")

artifact_dir.mkdir(
    parents=True,
    exist_ok=True
)

pickle.dump(
    new_df,
    open(artifact_dir / "movies.pkl", "wb")
)

pickle.dump(
    similarity,
    open(artifact_dir / "similarity.pkl", "wb")
)