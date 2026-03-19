"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def _print_recommendations(profile_name: str, user_prefs: dict, recommendations: list) -> None:
    print(f"\n=== {profile_name} ===")
    print(f"Prefs: {user_prefs}")
    print("\nTop recommendations:\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        title = song.get("title", "Unknown Title")
        artist = song.get("artist", "Unknown Artist")
        genre = song.get("genre", "?")
        mood = song.get("mood", "?")

        print(f"{rank:>2}. {title} — {artist}")
        print(f"    genre={genre} | mood={mood} | score={score:.2f}")
        print(f"    reasons: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "valence": 0.8,
            "danceability": 0.8,
            "acousticness": 0.2
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "valence": 0.6,
            "danceability": 0.5,
            "acousticness": 0.8
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "valence": 0.4,
            "danceability": 0.7,
            "acousticness": 0.1
        },
        # Edge case: conflicting preferences
        "Conflicting: High Energy + Melancholy": {
            "genre": "pop",
            "mood": "moody",
            "energy": 0.90,
            "valence": 0.3,
            "danceability": 0.7,
            "acousticness": 0.2
        }
    }

    for name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        _print_recommendations(name, user_prefs, recommendations)


if __name__ == "__main__":
    main()