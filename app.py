import random
import streamlit as st

# 1. Setup your data structure
roles = {
    "DPS": {
        "items": ["Ashe","Anran", "Bastion", "Cassidy", "Echo", "Emre", "Freja", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Reaper", "Shion", "Sierra", "Sojourn", "Soldier: 76", "Sombra", "Symmetra", "Torbjörn", "Tracer","Vendetta", "Venture", "Widowmaker"],
        "message": "The chosen DPS is: **{pick}**"
    },
    "Tank": {
        "items": ["D.Va", "Dmon","Domina", "Doomfist", "Hazard", "Junker Queen", "Mauga", "Orisa", "Ramattra", "Reinhardt", "Roadhog", "Sigma", "Winston", "Zarya", "Wrecking Ball"],
        "message": "Your random tank is: **{pick}**"
    },
    "Support": {
        "items": ["Ana", "Baptiste", "Brigitte", "Doctrine", "Illari", "Jetpack Cat", "Juno", "Kiriko", "Lifeweaver", "Lúcio", "Mercy","Mizuki", "Sombra", "Moira", "Wuyang", "Zenyatta"],
        "message": "The chosen Support is: **{pick}**"
    }
}

# 2. App Header styling
st.title("🎯 OW Randomizer")
st.write("Welcome to the randomizer! Tap a role below to get a character.")

# 3. Create three side-by-side buttons for mobile layouts
col1, col2, col3 = st.columns(3)

# 4. Handle button interactions natively without loops
with col1:
    if st.button("🛡️ Tank", use_container_width=True):
        pick = random.choice(roles["Tank"]["items"])
        st.info(roles["Tank"]["message"].format(pick=pick))

with col2:
    if st.button("⚔️ DPS", use_container_width=True):
        pick = random.choice(roles["DPS"]["items"])
        st.error(roles["DPS"]["message"].format(pick=pick))

with col3:
    if st.button("➕ Support", use_container_width=True):
        pick = random.choice(roles["Support"]["items"])
        st.success(roles["Support"]["message"].format(pick=pick))
