from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    def load_songs(csv_path: str) -> List[Dict]:
        import csv

    songs = []
    print(f"Loading songs from {csv_path}...")

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            })

    return songs
    print(f"Loading songs from {csv_path}...")
    return []

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    results = []

    for song in songs:
        score = 0
        reasons = []

        # Genre
        if song["genre"] == user_prefs["genre"]:
            score += 2.0
            reasons.append("genre match (+2.0)")

        # Mood
        if song["mood"] == user_prefs["mood"]:
            score += 1.5
            reasons.append("mood match (+1.5)")

        # Energy
        energy_diff = abs(song["energy"] - user_prefs["energy"])
        energy_score = (1 - energy_diff) * 1.5
        score += energy_score
        reasons.append(f"energy similarity (+{round(energy_score,2)})")

        # Valence
        val_diff = abs(song["valence"] - user_prefs["valence"])
        val_score = (1 - val_diff) * 1.2
        score += val_score
        reasons.append(f"valence similarity (+{round(val_score,2)})")

        # Danceability
        dance_diff = abs(song["danceability"] - user_prefs["danceability"])
        dance_score = (1 - dance_diff) * 1.0
        score += dance_score
        reasons.append(f"danceability similarity (+{round(dance_score,2)})")

        # Acousticness
        ac_diff = abs(song["acousticness"] - user_prefs["acousticness"])
        ac_score = (1 - ac_diff) * 1.0
        score += ac_score
        reasons.append(f"acousticness similarity (+{round(ac_score,2)})")

        explanation = ", ".join(reasons)

        results.append((song, score, explanation))

    # Sort highest → lowest
    results.sort(key=lambda x: x[1], reverse=True)

    return results[:k]