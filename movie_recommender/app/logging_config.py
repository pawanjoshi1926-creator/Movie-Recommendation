import logging


logging.basicConfig(
    filename="movie_api.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("movie_recommender")