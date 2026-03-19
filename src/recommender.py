from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

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
        scored: List[Tuple[float, Song]] = []
        for song in self.songs:
            score, _reasons = _score_song_like(
                favorite_genre=user.favorite_genre,
                favorite_mood=user.favorite_mood,
                target_energy=user.target_energy,
                likes_acoustic=user.likes_acoustic,
                song_genre=song.genre,
                song_mood=song.mood,
                song_energy=song.energy,
                song_acousticness=song.acousticness,
            )
            scored.append((score, song))

        scored.sort(key=lambda t: t[0], reverse=True)
        return [song for _score, song in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _score, reasons = _score_song_like(
            favorite_genre=user.favorite_genre,
            favorite_mood=user.favorite_mood,
            target_energy=user.target_energy,
            likes_acoustic=user.likes_acoustic,
            song_genre=song.genre,
            song_mood=song.mood,
            song_energy=song.energy,
            song_acousticness=song.acousticness,
        )
        return "; ".join(reasons) if reasons else "No strong matches, but included for variety."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    songs: List[Dict] = []
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Computes a weighted relevance score for one song and returns (score, reasons).
    """
    favorite_genre = str(user_prefs.get("genre", "")).strip().lower()
    favorite_mood = str(user_prefs.get("mood", "")).strip().lower()
    target_energy = float(user_prefs.get("energy", 0.5))
    target_acousticness = user_prefs.get("acousticness", None)

    score, reasons = _score_song_like(
        favorite_genre=favorite_genre,
        favorite_mood=favorite_mood,
        target_energy=target_energy,
        likes_acoustic=None,
        song_genre=str(song.get("genre", "")).strip().lower(),
        song_mood=str(song.get("mood", "")).strip().lower(),
        song_energy=float(song.get("energy", 0.0)),
        song_acousticness=float(song.get("acousticness", 0.0)),
    )

    if target_acousticness is not None:
        # Optional numeric feature used by CLI profiles (kept separate from the test OOP profile)
        diff = abs(float(song.get("acousticness", 0.0)) - float(target_acousticness))
        acoustic_points = 1.0 * max(0.0, 1.0 - diff)
        score += acoustic_points
        reasons.append(f"acousticness similarity (+{acoustic_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores all songs, sorts them by score (high -> low), and returns the top-k.
    """
    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, "; ".join(reasons)))

    scored.sort(key=lambda t: t[1], reverse=True)
    return scored[:k]


def _score_song_like(
    *,
    favorite_genre: str,
    favorite_mood: str,
    target_energy: float,
    likes_acoustic: bool | None,
    song_genre: str,
    song_mood: str,
    song_energy: float,
    song_acousticness: float,
) -> Tuple[float, List[str]]:
    """
    Shared scoring core used by both the CLI functions and the OOP Recommender.
    """
    score = 0.0
    reasons: List[str] = []

    # Categorical matches
    if favorite_genre and song_genre == favorite_genre:
        score += 2.0
        reasons.append("genre match (+2.00)")

    if favorite_mood and song_mood == favorite_mood:
        score += 1.0
        reasons.append("mood match (+1.00)")

    # Numerical similarity (closer is better): similarity = 1 - |a-b|, clamped to [0,1]
    energy_similarity = max(0.0, 1.0 - abs(song_energy - target_energy))
    energy_points = 1.5 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # Simple boolean preference for acoustic songs (used by tests)
    if likes_acoustic is not None:
        acoustic_is_high = song_acousticness >= 0.6
        if likes_acoustic == acoustic_is_high:
            score += 0.5
            reasons.append("acoustic preference match (+0.50)")

    return score, reasons