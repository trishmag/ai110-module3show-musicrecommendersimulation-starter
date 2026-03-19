# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeRanker 1.0**

---

## 2. Intended Use  

This system recommends the **top 5 songs** from a small CSV catalog by scoring how well each song matches a user's stated preferences (genre, mood, and target energy). It is designed for **classroom exploration** to understand how recommender systems turn data into ranked suggestions.

Assumptions:

- The user can describe their taste using a few simple labels (like "pop" + "happy") and a numeric energy target.
- The labels in the dataset (genre/mood) are correct and consistent.

---

## 3. How the Model Works  

The model looks at each song and adds up points:

- If the song's **genre matches** the user's favorite genre, it gets a big boost.
- If the song's **mood matches**, it gets a smaller boost.
- For **energy**, the model gives more points when the song's energy is *close* to the user's target energy (songs that are too far away get fewer points).

Then it sorts all songs by total score and returns the top results with short "reasons" like “genre match” or “energy similarity.”

Changes from starter:

- Fixed `load_songs` to correctly parse numeric columns as numbers.
- Made scoring return both a **numeric score** and **human-readable reasons**.
- Implemented a real sorting-based recommender instead of returning the first \(k\) songs.

---

## 4. Data  

The dataset is `data/songs.csv` with **18 songs**.

Features included:

- Categorical: `genre`, `mood`
- Numeric (0.0–1.0): `energy`, `valence`, `danceability`, `acousticness`
- Numeric: `tempo_bpm`

Coverage is limited. The catalog includes genres like pop, lofi, rock, ambient, jazz, synthwave, hiphop, classical, country, kpop, metal, reggaeton, and folk, but it still cannot represent the full range of music styles or cultures.

---

## 5. Strengths  

Strengths:

- **Transparent**: every recommendation includes reasons, so the user can understand and critique it.
- **Works well for “clear vibe” users**: if someone knows their genre + mood + energy target, it often surfaces reasonable matches.
- **Stable and predictable**: small changes in energy preference cause small changes in score, rather than random shifts.

---

## 6. Limitations and Bias 

Limitations / bias risks:

- **Filter bubbles**: strong weights on genre/mood can repeatedly recommend the same style, reducing discovery.
- **Label subjectivity**: “mood” labels are subjective; if they’re wrong or inconsistent, the recommender will make wrong comparisons.
- **Catalog bias**: if a genre is underrepresented in the dataset, users who like that genre will get worse recommendations.
- **Oversimplified users**: real users often like multiple genres depending on context; a single fixed profile can misrepresent them.
- **No behavior signals**: it ignores skips, repeats, playlists, and listening sessions, which are a big part of real-world recommendation systems.

---

## 7. Evaluation  

I evaluated the system by running multiple user profiles in `src/main.py` and checking whether the top 5 results matched common-sense expectations:

- **High-Energy Pop** (pop + happy + high energy)
- **Chill Lofi** (lofi + chill + low energy, plus acousticness similarity)
- **Deep Intense Rock** (rock + intense + very high energy)
- **Conflicting profile** (high energy + melancholy mood) to stress test the logic

I also ran the provided unit tests in `tests/test_recommender.py` to confirm the OOP version sorts songs in the expected order and produces a non-empty explanation string.

---

## 8. Future Work  

If I continued this project, I would:

- Add **diversity / novelty** so the top \(k\) is not all the same genre (reduce filter bubbles).
- Let users have **multiple taste modes** (e.g., “work focus” vs “gym”) rather than one static profile.
- Incorporate more signals (even simulated ones) like **skips** and **likes** to show how collaborative filtering changes recommendations.

---

## 9. Personal Reflection  

The biggest learning moment was realizing that “recommendation” can be as simple as **a few weighted rules plus sorting**, yet it still feels personalized. I was surprised how quickly a small design choice (like giving genre a larger weight) can dominate the results and create a mini filter bubble.

AI help was most useful for brainstorming scoring ideas and edge cases, but I still needed to double-check that the math rewarded *closeness* (similarity) rather than just “higher is better.” This project made me more skeptical of real recommendations: even when they look smart, they can reflect the platform’s data and weighting choices.
