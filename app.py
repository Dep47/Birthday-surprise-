
import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

if "love_answer" not in st.session_state:
    st.session_state.love_answer = None

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5, #f5e6ff, #ffe4ec);
}
.welcome {
    text-align: center;
    padding: 25px 10px;
}
.question {
    background: rgba(255,255,255,0.8);
    padding: 22px;
    border-radius: 20px;
    text-align: center;
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
    st.markdown("<h3 style='text-align:center;'>Yayyyy! 🥰</h3>", unsafe_allow_html=True)
    st.image(
        "https://media.tenor.com/2roX3uxz_68AAAAC/cute-love.gif",
        width=280
    )
    st.success("I knew it! Deep is the happiest person today! ❤️")

elif st.session_state.love_answer == "THINK":
    st.markdown("<h3 style='text-align:center;'>Hmmmm... 🤔</h3>", unsafe_allow_html=True)
    st.image(
        "https://media.tenor.com/6Z2Y8Q3qJwAAAAAC/thinking.gif",
        width=280
    )
    st.info("Awww, take your time Munu! Such an innocent thinker! 😂❤️")

elif st.session_state.love_answer == "NO":
    st.markdown("<h3 style='text-align:center;'>Nooooo! 😭</h3>", unsafe_allow_html=True)
    st.image(
        "https://media.tenor.com/1J5Q3Y7XQ4AAAAAC/crying-sad.gif",
        width=280
    )
    st.error("Deep's little heart is broken! 💔😭")

st.divider()

if st.session_state.love_answer == "YES":
    st.markdown("""
    <div class="lock">
        <h2>🎁 Your Birthday Surprise</h2>
        <h1>🔓 UNLOCKED ❤️</h1>
        <p>Your special surprise is ready, Munu!</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Your Surprise 🎁", use_container_width=True):
        st.balloons()
        st.success("Let's go, Munu! ❤️")

else:
    st.markdown("""
    <div class="lock">
        <h2>🎁 Your Birthday Surprise</h2>
        <h1>🔒 LOCKED</h1>
        <p>Something special is waiting for you!</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr>
<p style="text-align:center;">
    Made with endless love by Deep ❤️
</p>
""", unsafe_allow_html=True)
