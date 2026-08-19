# app/dependencies/model.py

import app.services.model_loader as model_loader


def get_movies():
    return model_loader.movies


def get_similarity():
    return model_loader.similarity
