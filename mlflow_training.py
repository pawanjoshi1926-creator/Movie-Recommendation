import mlflow
import pandas as pd


def get_genres(value):

    if pd.isna(value):
        return set()

    return set(
        str(value).lower().split()
    )


def is_relevant(
    original_genres,
    recommended_genres
):

    original = get_genres(original_genres)
    recommended = get_genres(recommended_genres)

    return len(original & recommended) > 0


def get_recommendation_indices(
    movie_index,
    similarity,
    top_n=5
):

    distances = similarity[movie_index]

    movie_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        index
        for index, score
        in movie_list[1:top_n + 1]
    ]


def precision_at_k(movie_index, recommendations, movies, top_n=5):

    original_genres = get_genres(
        movies.iloc[movie_index]["genres"]
    )

    if not original_genres:
        return 0.0

    relevant = 0

    for recommended_index in recommendations[:top_n]:

        recommended_genres = get_genres(
            movies.iloc[recommended_index]["genres"]
        )

        if original_genres.intersection(recommended_genres):
            relevant += 1

    return relevant / top_n


def evaluate_recommender(
    movies,
    similarity,
    sample_size=100,
    top_n=5
):

    scores = []

    sample_indices = movies.index[:sample_size]

    for movie_index in sample_indices:

        recommendations = get_recommendation_indices(
            movie_index,
            similarity,
            top_n
        )

        score = precision_at_k(
            movie_index,
            recommendations,
            movies,
            top_n
        )

        scores.append(score)

    return sum(scores) / len(scores)


# ---------------------------------
# Load your existing artifacts
# ---------------------------------

movies = pd.read_pickle("artifacts/movies.pkl")

print("Movies columns:")
print(movies.columns.tolist())

print("\nFirst movie:")
print(movies.iloc[0])

similarity = pd.read_pickle(
    "artifacts/similarity.pkl"
)


# ---------------------------------
# MLflow experiment
# ---------------------------------

mlflow.set_experiment(
    "Movie Recommendation System"
)


with mlflow.start_run():

    # Parameters
    mlflow.log_param(
        "algorithm",
        "cosine_similarity"
    )

    mlflow.log_param(
        "vectorizer",
        "TF-IDF"
    )

    mlflow.log_param(
        "top_n",
        5
    )

    mlflow.log_param(
        "evaluation_sample_size",
        100
    )

    # Evaluation
    precision = evaluate_recommender(
        movies,
        similarity,
        sample_size=100,
        top_n=5
    )

    # Metric
    mlflow.log_metric(
        "precision_at_5",
        precision
    )

    # Artifacts
    mlflow.log_artifacts(
        "model_package",
        artifact_path="recommendation_model"
    )

    print(
        f"Precision@5: {precision:.4f}"
    )

