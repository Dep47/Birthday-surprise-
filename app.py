
import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(145deg, #ffe0eb, #fff0f5, #ffd6e7);
}
h1, h2, h3 {
    color: #b52d62;
    text-align: center;
}
p {
    color: #873653;
    text-align: center;
    font-size: 17px;
}
.stButton button {
    background: linear-gradient(90deg, #ff4d88, #ff78a5);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 12px;
    font-weight: bold;
    width: 100%;
}
div[data-testid="stRadio"] {
    background: rgba(255,255,255,0.55);
    padding: 15px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "surprise_opened" not in st.session_state:
    st.session_state.surprise_opened = False

st.markdown("""
# 🎂 Happy Birthday, Munu! ❤️

### A little surprise, made just for you.

👦🏻 ❤️ 👧🏻

### Deep ❤️ Munu

Some people make life more beautiful
just by being in it.

Today is all about YOU. 🥰

I made something little and special.

### Are you ready? ❤️
""")

st.balloons()

st.divider()

st.markdown("""
## 💌 A Little Game For You

Before opening your birthday surprise,
you have to answer three little questions!

Be honest, Munu! 😁❤️
""")

st.markdown("## 💗 Question 1")

st.markdown("### Munu, do you love Deep? ❤️")

q1 = st.radio(
    "Choose your answer:",
    ["YES ❤️", "THINK 🤔", "NO 💔"],
    index=None,
    key="q1"
)

if st.button("Submit Answer 1"):
    if q1:
        st.session_state.answers["q1"] = q1
    else:
        st.warning("Choose one answer first! 😁")

if "q1" in st.session_state.answers:
    if st.session_state.answers["q1"] == "YES ❤️":
        st.success("Yay! Deep is the happiest person! ❤️")
        st.markdown("## 🥰 💑 ❤️")
    elif st.session_state.answers["q1"] == "THINK 🤔":
        st.info("Take your time, Munu. Deep is waiting patiently. ❤️")
        st.markdown("## 🤔 💭 🥺")
    else:
        st.error("Oh no! Deep's heart is broken! 💔")
        st.markdown("## 😭 🥺 💔")

st.divider()

st.markdown("## 💕 Question 2")

st.markdown("### What makes Deep happiest?")

q2 = st.radio(
    "Your answer:",
    [
        "Talking with Munu ❤️",
        "Eating pizza 🍕",
        "Sleeping 😴"
    ],
    index=None,
    key="q2"
)

if st.button("Submit Answer 2"):
    if q2:
        st.session_state.answers["q2"] = q2
    else:
        st.warning("Choose one answer first! 😁")

if "q2" in st.session_state.answers:
    if st.session_state.answers["q2"] == "Talking with Munu ❤️":
        st.success("Absolutely correct! You are his happiness! 🥰")
        st.markdown("## 🧸 ❤️ 🥰")
    elif st.session_state.answers["q2"] == "Eating pizza 🍕":
        st.info("Pizza is good, but Munu is better! 😂❤️")
        st.markdown("## 🍕 😂")
    else:
        st.info("Sleeping is important, but Munu comes first! ❤️")
        st.markdown("## 😴 🥰")

st.divider()

st.markdown("## 💖 Question 3")

st.markdown("### Where is Deep sending you birthday wishes from?")

q3 = st.radio(
    "Guess:",
    [
        "Mumbai 🌆",
        "Guwahati 🌸",
        "The Moon 🌙"
    ],
    index=None,
    key="q3"
)

if st.button("Submit Answer 3"):
    if q3:
        st.session_state.answers["q3"] = q3
    else:
        st.warning("Choose one answer first! 😁")

if "q3" in st.session_state.answers:
    if st.session_state.answers["q3"] == "Mumbai 🌆":
        st.success("Yes! From Mumbai, with lots of love! ❤️")
        st.markdown("## 🌆 💌 ❤️")
    elif st.session_state.answers["q3"] == "Guwahati 🌸":
        st.info("Not this time! Deep is sending wishes from Mumbai! 😁")
        st.markdown("## 🌸 😁")
    else:
        st.info("Haha! Not from the Moon, from Mumbai! 😂")
        st.markdown("## 🌙 🚀")

st.divider()

if len(st.session_state.answers) == 3:
    st.markdown("""
    ## 🎁 All Three Questions Completed!

    ### Your surprise is ready! ❤️
    """)

    if st.button("🎁 OPEN YOUR BIRTHDAY SURPRISE ❤️"):
        st.session_state.surprise_opened = True
        st.rerun()

else:
    st.info(
        f"💌 Complete all three questions to unlock your surprise! "
        f"({len(st.session_state.answers)}/3)"
    )

if st.session_state.surprise_opened:

    st.balloons()
    st.snow()

    st.markdown("---")

    st.markdown("""
    # 🎉 HAPPY BIRTHDAY MUNU! 🎂

    ## ❤️ 🥳 💗

    ### This Little Surprise Is All Yours!

    You are special, Munu.

    Never forget that! ❤️

    ### 🥰 🎀 🧸 💐

    May your life always be filled with
    happiness, laughter and beautiful moments.

    May this new year of your life bring
    you everything your heart wishes for.

    ### With love,

    # Deep ❤️
    """)

    st.divider()

    st.markdown("""
    # 🎵 A Song For You 🎵

    ### Aji Munu Jonmodin ❤️

    Because today deserves its own soundtrack! 🥰
    """)

    playlist_id = "OLAK5uy_k9Dn0CJOLE0N_JMuT7dLMV-OfuyYzzE_8"

    st.iframe(
        f"https://www.youtube-nocookie.com/embed/videoseries?list={playlist_id}&autoplay=1",
        height=220
    )

    st.markdown("""
    ## 🎂 Once Again, Happy Birthday!

    ### Lots of love from Mumbai to you. 💌

    ## ❤️ Deep & Munu ❤️
    """)

    st.balloons()
