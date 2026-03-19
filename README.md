# 🎵 Music Recommender Simulation

## Project Summary

This repo is a **CLI-first music recommender simulation**. It loads a small song catalog from `data/songs.csv`, compares each song to a user's "taste profile" (genre, mood, and target energy), and then ranks songs by a weighted score. Each recommendation includes an explanation string so you can see *why* it scored well.

---

## How The System Works

Big platforms (Spotify, TikTok, YouTube) recommend using a mix of:

- **Collaborative filtering**: "people like you also liked..." (based on behavior patterns across many users)
- **Content-based filtering**: "this song is similar to what you like..." (based on attributes like genre, mood, tempo, etc.)

This project is a **content-based** system: it only uses song attributes and the current user's stated preferences.

### Data → Prediction (what gets transformed)

- **Input features (song data)**: `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`
- **User preferences (taste profile)**:
  - CLI profiles in `src/main.py`: `genre`, `mood`, `energy` (+ optional `acousticness`)
  - Test/OOP profile in `src/recommender.py`: `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

### Algorithm Recipe (Scoring Rule)

For each song, the system computes a score and collects "reasons":

- **Genre match**: +2.00 if `song.genre == user.genre`
- **Mood match**: +1.00 if `song.mood == user.mood`
- **Energy similarity**: \(+1.5 \times (1 - |song.energy - user.energy|)\), clamped so it never goes negative
- **Optional acousticness similarity (CLI only)**: \(+1.0 \times (1 - |song.acousticness - user.acousticness|)\)
- **Optional acoustic preference (tests/OOP only)**: +0.50 if a boolean "likes acoustic" preference matches whether `acousticness >= 0.6`

### Ranking Rule (Recommender)

The recommender scores **every** song, then sorts the list from **highest score → lowest score**, and returns the top \(k\).

### Data Flow Diagram

```mermaid
flowchart TD
  A[User taste profile] --> B[Load songs.csv]
  B --> C{For each song}
  C --> D[Score song<br/>+ collect reasons]
  D --> E[Store (song, score, reasons)]
  E --> F[Sort by score desc]
  F --> G[Return top k + print to CLI]
```

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

I ran quick "stress tests" by changing the user profile in `src/main.py`:

- **High-Energy Pop**: should rank upbeat pop highest because it matches genre/mood and energy.
- **Chill Lofi**: should favor lofi + chill and lower energy, with an optional boost for acousticness similarity.
- **Deep Intense Rock**: should rank intense rock higher due to genre match + high target energy.
- **Conflicting profile** (high energy + melancholy mood): helps reveal how the system behaves when preferences are hard to satisfy from a tiny catalog.

---

## Limitations and Risks

This simulation is intentionally simple, which creates limitations:

- **Tiny dataset**: only 18 songs, so the "best" song can appear repeatedly and variety is limited.
- **Filter bubbles**: strong weights on genre/mood can repeatedly recommend the same style and block discovery.
- **Shallow understanding**: it does not use lyrics, culture, novelty, or user behavior (skips, repeats, playlists).
- **Label bias**: the system trusts the labels in `songs.csv` (genre/mood), even if they’re subjective.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

Building this made it clear that recommendation is often just **turning messy human taste into numbers**, then sorting. Even a simple scoring rule can feel “smart” because the output is personalized and explained. It also showed how quickly **bias** appears: if you overweight genre, the system can ignore songs that match mood/energy, and small datasets can make the same tracks dominate.

AI tools were helpful for brainstorming weights and edge cases, but I still had to check the math and verify that the rules matched the behavior I expected.


---

<!-- Template appendix removed. See `model_card.md` for the full model card. -->
