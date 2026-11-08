
import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

if "love_answer" not in st.session_state:
    st.session_state.love_answer = None

if "surprise_opened" not in st.session_state:
    st.session_state.surprise_opened = False

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5, #f5e6ff, #ffe4ec);
}
h1, h2, h3, p {
    color: #753653;
}
.welcome {
    text-align: center;
    padding: 25px 10px;
}
.question {
    background: rgba(255,255,255,0.75);
    padding: 22px;
    border-radius: 20px;
    text-align: center;
    margin: 15px 0;
}
.lock {
    background: #f7dce9;
    padding: 22px;
    border-radius: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="welcome">
    <h1>🎂 Happy Birthday, Munu! ❤️</h1>
    <h3>Today is all about you.</h3>
    <p>Someone as special as you deserves a little extra magic today.</p>
    <h2>💗 ✨ 💗</h2>
    <h3>A little world, made just for you...</h3>
    <p>Made with love by Deep ❤️</p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="question">
    <h2>First, answer me something! 🙈</h2>
    <h3>Do you love Deep? ❤️</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("YES ❤️", use_container_width=True):
        st.session_state.love_answer = "YES"

with col2:
    if st.button("THINK 🤔", use_container_width=True):
        st.session_state.love_answer = "THINK"

with col3:
    if st.button("NO 💔", use_container_width=True):
        st.session_state.love_answer = "NO"

if st.session_state.love_answer == "YES":
    st.image(
        "https://media.tenor.com/2roX3uxz_68AAAAC/cute-love.gif",
        width=250
    )
    st.success("Yayyyy! I knew it! Deep is smiling like crazy! 🥰")

elif st.session_state.love_answer == "THINK":
    st.image(
        "https://media.tenor.com/6Z2Y8Q3qJwAAAAAC/thinking.gif",
        width=250
    )
    st.info("Awww, take your time! Thinking so seriously? 😂")

elif st.session_state.love_answer == "NO":
    st.image(
        "https://media.tenor.com/1J5Q3Y7XQ4AAAAAC/crying-sad.gif",
        width=250
    )
    st.error("Nooooo! My little heart! 😭💔")

st.divider()

st.markdown("""
<div class="question">
    <h2>Okay, one more thing! 🎮</h2>
    <h3>How well do you know Deep?</h3>
    <p>Let's play a little birthday challenge! 💕</p>
</div>
""", unsafe_allow_html=True)

q1 = st.radio(
    "1. Who is more dramatic? 😂",
    ["Deep", "Munu", "Both equally"]
)

q2 = st.radio(
    "2. Who says sorry first? 🥺",
    ["Deep", "Munu", "Depends on the situation"]
)

q3 = st.radio(
    "3. Who misses the other person more? ❤️",
    ["Deep", "Munu", "Both equally"]
)

st.divider()

st.markdown("""
<div class="lock">
    <h2>🎁 Your Birthday Surprise</h2>
    <h1>🔒 LOCKED</h1>
    <p>Something special is waiting for you!</p>
    <p>Answer YES and complete all three challenges to unlock it. ❤️</p>
</div>
""", unsafe_allow_html=True)

game_completed = all([q1, q2, q3])

can_unlock = (
    st.session_state.love_answer == "YES"
    and game_completed
)

if st.button(
    "Open Your Surprise 🎁",
    use_container_width=True,
    disabled=not can_unlock
):
    st.session_state.surprise_opened = True
    st.balloons()

if st.session_state.surprise_opened:
    st.success("Your surprise is ready, Munu! ❤️")
    st.markdown("### See you inside... 💗")
elif not can_unlock:
    st.warning("Complete the three challenges and choose YES to unlock your surprise! ❤️")

st.markdown("""
<hr>
<p style="text-align:center;">
    Made with endless love by Deep ❤️
</p>
""", unsafe_allow_html=True)
