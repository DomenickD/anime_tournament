import streamlit as st
import pandas as pd
import random
import math

# --- App Config ---
st.set_page_config(page_title="Anime Power Rankings", page_icon="⚔️", layout="wide")

# --- Elo Rating System ---
def expected_score(rating_a, rating_b):
    return 1 / (1 + math.pow(10, (rating_b - rating_a) / 400))

def update_ratings(rating_winner, rating_loser, k=32):
    expected_winner = expected_score(rating_winner, rating_loser)
    expected_loser = expected_score(rating_loser, rating_winner)
    
    new_winner = rating_winner + k * (1 - expected_winner)
    new_loser = rating_loser + k * (0 - expected_loser)
    
    return new_winner, new_loser

# --- Initial Data ---
DEFAULT_ANIME = [
    "Solo Leveling",
    "Sword Art Online",
    "Jujutsu Kaisen",
    "Demon Slayer",
    "Attack on Titan",
    "DanDanDan",
    "One Punch Man",
    "My Hero Academia",
    "Bleach",
    "That Time I Got Reincarnated as a Slime",
    "Overlord",
    "The Rising of the Shield Hero",
    "Chainsaw Man",
    "Kaiju No. 8",
    "Mashle: Magic and Muscles",
    "Mob Psycho 100"
]

# --- State Management ---
if 'ratings' not in st.session_state:
    st.session_state.ratings = {anime: 1200.0 for anime in DEFAULT_ANIME}

if 'matchup' not in st.session_state:
    st.session_state.matchup = random.sample(list(st.session_state.ratings.keys()), 2)

# --- Action Handlers ---
def handle_vote(winner, loser):
    # Update ratings
    r_win = st.session_state.ratings[winner]
    r_lose = st.session_state.ratings[loser]
    new_r_win, new_r_lose = update_ratings(r_win, r_lose)
    st.session_state.ratings[winner] = new_r_win
    st.session_state.ratings[loser] = new_r_lose
    
    # Pick new matchup
    anime_list = list(st.session_state.ratings.keys())
    st.session_state.matchup = random.sample(anime_list, 2)

# --- UI Layout ---
st.title("⚔️ Anime Power Rankings")
st.markdown("Help Cody find the ultimate anime! Vote for the better anime in each matchup. Ratings use the continuous Elo system.")

# Matchup Section
st.header("Who wins?")
st.markdown("<br>", unsafe_allow_html=True)
col1, col_vs, col2 = st.columns([4, 1, 4])

anime_a, anime_b = st.session_state.matchup

with col1:
    st.markdown(f"<h3 style='text-align: center; color: #1f77b4;'>{anime_a}</h3>", unsafe_allow_html=True)
    if st.button(f"👈 Vote for {anime_a}", width="stretch", type="primary"):
        handle_vote(anime_a, anime_b)
        st.rerun()

with col_vs:
    st.markdown("<h2 style='text-align: center; color: #666;'>VS</h2>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<h3 style='text-align: center; color: #ff7f0e;'>{anime_b}</h3>", unsafe_allow_html=True)
    if st.button(f"Vote for {anime_b} 👉", width="stretch", type="primary"):
        handle_vote(anime_b, anime_a)
        st.rerun()

st.divider()

# Leaderboard Section
st.header("🏆 Full Leaderboard")

df = pd.DataFrame([
    {"Anime": anime, "Rating": round(rating)} 
    for anime, rating in st.session_state.ratings.items()
])
df = df.sort_values(by="Rating", ascending=False).reset_index(drop=True)
df.index += 1  # Start rank at 1

# Display dataframe
st.dataframe(df, width="stretch")

st.sidebar.title("Settings")
if st.sidebar.button("Reset Rankings"):
    st.session_state.ratings = {anime: 1200.0 for anime in DEFAULT_ANIME}
    st.session_state.matchup = random.sample(list(st.session_state.ratings.keys()), 2)
    st.sidebar.success("Rankings reset!")
    st.rerun()
