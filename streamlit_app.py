import requests
import streamlit as st

# -------------------------
# Configuration
# -------------------------

API_URL = "http://127.0.0.1:8000/api/v1/recommend"

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# -------------------------
# Title
# -------------------------

st.title("🎬 Movie Recommendation System")

st.write(
    "Enter a movie name and discover similar movies."
)

# -------------------------
# User Input
# -------------------------

movie = st.text_input(
    "Movie Name",
    placeholder="Example: Avatar"
)

# -------------------------
# Recommend Button
# -------------------------

if st.button("Recommend"):

    if movie.strip() == "":
        st.warning("Please enter a movie name.")

    else:

        with st.spinner("Finding recommendations..."):

            response = requests.get(
                API_URL,
                params={"movie": movie}
            )

        # -------------------------
        # Success
        # -------------------------

        if response.status_code == 200:

            data = response.json()

            st.success(
                f"Recommendations for '{data['movie']}'"
            )

            for i, rec in enumerate(
                data["recommendations"],
                start=1
            ):

                st.write(
                    f"**{i}. {rec['title']}** "
                    f"(Similarity: {rec['similarity_score']:.3f})"
                )

        # -------------------------
        # Movie Not Found
        # -------------------------

        elif response.status_code == 404:

            detail = response.json()["detail"]

            st.error(detail["message"])

            suggestions = detail.get("suggestions", [])

            if suggestions:

                st.write("Did you mean:")

                for movie in suggestions:
                    st.write(f"- {movie}")

        # -------------------------
        # Other Errors
        # -------------------------

        else:

            st.error(
                f"API Error ({response.status_code})"
            )