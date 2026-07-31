from dataclasses import dataclass

import numpy as np
import pandas as pd

from fastapi import Depends, Request


@dataclass
class ModelStore:
    movies: pd.DataFrame
    similarity: np.ndarray


def get_models(request: Request) -> ModelStore:
    """
    Returns the loaded movie DataFrame and similarity matrix
    from the FastAPI application state.
    """

    return ModelStore(
        movies=request.app.state.movies,
        similarity=request.app.state.similarity
    )