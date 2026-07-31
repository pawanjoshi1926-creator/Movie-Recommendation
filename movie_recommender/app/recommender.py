from difflib import get_close_matches

from app.config import settings
from app.logging_config import logger


def recommend(
    movie_name: str,
    movies,
    similarity,
    top_n: int = settings.DEFAULT_RECOMMENDATIONS
):
    """
    Recommend similar movies based on cosine similarity.

    Args:
        movie_name (str): Movie entered by the user.
        movies (pd.DataFrame): Movies DataFrame.
        similarity (np.ndarray): Cosine similarity matrix.
        top_n (int): Number of recommendations to return.

    Returns:
        dict: Recommended movies.
    """

    logger.info(f"Recommendation request received for '{movie_name}'")

    try:
        # -----------------------------
        # Find Movie
        # -----------------------------
        movie_match = movies[
            movies["title"].str.lower() == movie_name.lower()
        ]

        # -----------------------------
        # Movie Not Found
        # -----------------------------
        if movie_match.empty:

            logger.warning(
                f"Movie '{movie_name}' not found."
            )

            suggestions = get_close_matches(
                movie_name,
                movies["title"].tolist(),
                n=5,
                cutoff=0.6
            )

            return {
                "movie": movie_name,
                "recommendations": [],
                "suggestions": suggestions
            }

        # -----------------------------
        # Get Similarity Scores
        # -----------------------------
        movie_index = movie_match.index[0]

        distances = similarity[movie_index]

        movie_list = sorted(
            enumerate(distances),
            key=lambda x: x[1],
            reverse=True
        )[1: top_n + 1]

        recommendations = []

        # -----------------------------
        # Build Recommendation List
        # -----------------------------
        for idx, score in movie_list:

            recommendations.append(
                {
                    "title": movies.iloc[idx]["title"],
                    "similarity_score": round(float(score), 3)
                }
            )

        logger.info(
            f"Successfully generated {len(recommendations)} recommendations for '{movie_name}'."
        )

        return {
            "movie": movie_match.iloc[0]["title"],
            "recommendations": recommendations
        }

    except Exception:
        logger.exception(
            f"Unexpected error while generating recommendations for '{movie_name}'."
        )
        raise