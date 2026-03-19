# 🎵 Music Recommender Simulation
Project Summary
In this project, I built a rule-based music recommender system that suggests songs based on a user’s preferences for genre, mood, energy, valence, danceability, and acousticness.
The system represents songs as structured data and compares them against a user profile using a weighted scoring function. Each song is assigned a score based on how closely it matches the user’s preferences, and the top-ranked songs are returned as recommendations.
The recommender also explains why each song was selected by showing which features contributed to its score. This makes the system interpretable and helps demonstrate how recommendation systems work in practice.

# How The System Works
The system uses the following components:
Song Features
Each song includes the following attributes:
Genre
Mood
Energy
Tempo (BPM)
Valence
Danceability
Acousticness
These features describe both categorical and numerical aspects of a song.

# User Profile
The user profile stores preferences such as:
Favorite genre
Favorite mood
Target energy level
Valence preference
Danceability preference
Acousticness preference

# Scoring Method
The recommender computes a score for each song by combining:
Genre match (exact match gives a high score boost)
Mood match (exact match gives a score boost)
Energy similarity (difference between user and song energy)
Valence similarity
Danceability similarity
Acousticness similarity
Each component contributes a weighted value to the final score.

# Recommendation Selection
All songs are scored against the user profile
Songs are sorted by score in descending order
The top k songs (typically 5) are returned
Each recommendation includes an explanation of why it scored well

# Getting Started
Setup
Create a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate (Mac or Linux)
.venv\Scripts\activate (Windows)

Install dependencies
pip install -r requirements.txt

Run the app
python -m src.main

# Running Tests
Run the starter tests with:
pytest
You can add more tests in tests/test_recommender.py.

# Experiments I Tried
- Increasing the weight of genre improved how strongly genre-aligned songs ranked higher
- Adding acousticness helped better identify lofi and chill songs
- Adjusting energy similarity affected whether high-energy songs dominated recommendations
- Different user profiles produced noticeably different rankings, showing that the system adapts to preferences

# Limitations and Risks
- The system only works on a small dataset
- It does not understand lyrics or deeper semantic meaning of songs
- It relies on manually chosen weights rather than learned parameters
- It may over-prioritize certain features like genre or energy
- It assumes user preferences are static and does not learn from feedback
# 🎧 Model Card - Music Recommender Simulation
1. Model Name
VibeFinder 1.0

2. Intended Use
This system suggests 3 to 5 songs from a small catalog based on a user’s preferred genre, mood, energy level, and other audio features. It is intended for educational purposes to demonstrate how recommendation systems work and is not designed for production use.

3. How It Works
The recommender compares each song in the dataset to a user’s preference profile. It assigns a score based on how closely the song matches the user’s preferences across multiple features.
Categorical features such as genre and mood contribute fixed boosts when they match, while numerical features such as energy, valence, danceability, and acousticness are compared using similarity-based calculations. The final score is a weighted combination of these factors.
Songs are then ranked by their scores, and the highest-scoring songs are returned as recommendations along with explanations describing which features influenced their ranking.
4. Data
The dataset consists of a small CSV file (songs.csv) containing a limited number of songs (approximately 10–20 entries depending on the version).
Each song includes:
- Title and artist
- Genre and mood labels
- Audio features such as energy, tempo, valence, danceability, and acousticness
The dataset represents a simplified and curated collection of songs intended for demonstration rather than real-world diversity. As a result, it may reflect limited genres and moods.
5. Strengths
- Produces interpretable recommendations with clear explanations
- Works well when user preferences align with available song features
- Easy to understand and debug due to rule-based logic
- Flexible enough to adjust scoring weights for experimentation
6. Limitations and Bias
- The recommender may favor certain genres or moods depending on dataset distribution
- It assumes all users express preferences in the same way
- It does not account for cultural context, trends, or listening history
- It may over-rely on a few dominant features such as genre or energy
- It cannot adapt or improve automatically without manual changes
7. Evaluation
The system was evaluated by testing multiple user profiles with different combinations of preferences. The recommendations were reviewed to determine whether they aligned with expected outcomes.
The system was also validated by inspecting the scoring logic and ensuring that songs with matching attributes received higher scores than those that did not.
8. Future Work
- Incorporate collaborative filtering or machine learning models
- Add more songs to improve diversity and coverage
- Introduce diversity-aware ranking to avoid similar recommendations
- Include user feedback to refine recommendations over time
- Expand feature set to include lyrical or semantic analysis
9. Personal Reflection
This project demonstrates how recommendation systems can be built using relatively simple rule-based logic while still producing meaningful results. It helped illustrate how user preferences can be translated into numerical scores and how different features contribute to ranking decisions.

It also highlights potential bias and limitations in recommendation systems, such as over-reliance on certain features and lack of adaptability. In real-world systems, more advanced techniques and continuous learning would be needed to provide more personalized and fair recommendations.