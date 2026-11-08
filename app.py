import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

if "answer" not in st.session_state:
    st.session_state.answer = None

st.markdown("""
<style>
.stApp {
    background: linear-gradient(145deg, #ffe4ef 0%, #f4e5ff 50%, #fff0e5 100%);
}
.block-container {
    max-width: 760px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3, p {
    text-align: center;
}
.stButton > button {
    width: 100%;
    min-height: 55px;
    border-radius: 18px;
    border: 2px solid #efa8c8;
    background: #fff8fc;
    color: #a43e75;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton > button:hover {
    background: #ffd6e8;
    border-color: #d96b9e;
    color: #8c285d;
}
.greeting {
    text-align: center;
    color: #995078;
    font-size: 18px;
    line-height: 1.8;
}
.gift-box {
    background: rgba(255,255,255,0.72);
    border: 2px solid #f2b3d0;
    border-radius: 28px;
    padding: 25px 15px;
    text-align: center;
    margin: 25px 0;
    box-shadow: 0 8px 25px rgba(174,91,137,0.13);
}
.gift-heading {
    color: #a33d70;
    font-size: 25px;
    font-weight: bold;
}
.gift-description {
    color: #80536b;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">
    <div style="font-size:48px;">🎀 🌸 🦋 🌸 🎀</div>
    <div style="font-size:65px;">🎂</div>
    <h1 style="color:#b33f78;font-size:42px;">
        Happy Birthday,<br>My Munu! ❤️
    </h1>
    <div class="greeting">
        Today is all about you. ✨<br>
        Someone as special as you deserves<br>
        a little extra magic today.<br><br>
        <b>A little world, made just for you...</b>
    </div>
    <div style="font-size:30px;margin-top:15px;">
        💗 🌷 💕 🌷 💗
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#a33d70;">Before your surprise... 💌</h2>
<h3 style="color:#80536b;">Do you love Deep? ❤️</h3>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("YES ❤️"):
        st.session_state.answer = "yes"

with col2:
    if st.button("THINK 🤔"):
        st.session_state.answer = "think"

with col3:
    if st.button("NO 💔"):
        st.session_state.answer = "no"

if st.session_state.answer == "yes":
    cartoon = """
    <div class="character">🥰</div>
    <div class="hearts">💖 💕 💗 💞</div>
    <h2 style="color:#d63384;">Yayyyyy! I knew it! ❤️</h2>
    <p>Deep is smiling like crazy right now! 🥹</p>
    """
elif st.session_state.answer == "think":
    cartoon = """
    <div class="character">🤔</div>
    <div class="hearts">💭 💭 💭</div>
    <h2 style="color:#a35b91;">Awww, take your time, Munu! 🌷</h2>
    <p>No pressure... I'll wait for your answer. 😊</p>
    """
elif st.session_state.answer == "no":
    cartoon = """
    <div class="character">😭</div>
    <div class="hearts">💔 🥺 💔</div>
    <h2 style="color:#a33d70;">Nooooo! My little heart! 💔</h2>
    <p>Deep needs a big hug now! 🥹</p>
    """
else:
    cartoon = """
    <div class="character">🐻‍❄️</div>
    <h2 style="color:#a35b91;">Waiting for your answer... 💗</h2>
    <p>Choose honestly, Munu! 😊</p>
    """

components.html(f"""
<div style="text-align:center;padding:10px;">
<style>
.character {{
    font-size:125px;
    animation:bounce 1.5s infinite;
}}
.hearts {{
    font-size:35px;
    margin:10px;
}}
p {{
    color:#80536b;
    font-size:18px;
}}
@keyframes bounce {{
    0%,100% {{transform:translateY(0);}}
    50% {{transform:translateY(-15px);}}
}}
</style>
{cartoon}
</div>
""", height=280)

st.markdown("""
<div class="gift-box">
    <div style="font-size:75px;">🎁</div>
    <div class="gift-heading">A Special Surprise for You</div>
    <div class="gift-description">
        A little something made with lots of love,<br>
        especially for my Munu. 💝
    </div>
</div>
""", unsafe_allow_html=True)

if st.session_state.answer == "yes":
    st.success("🔓 Your surprise is unlocked! ❤️")
    st.button("🎁 OPEN YOUR SURPRISE", key="open_surprise")
else:
    st.button(
        "🔒 SURPRISE LOCKED — SAY YES ❤️",
        disabled=True,
        key="locked_surprise"
    )

st.markdown("""
<br>
<div style="text-align:center;color:#a35b91;">
    Made with love by Deep ❤️<br>
    <small>A little piece of my heart, just for you.</small>
</div>
""", unsafe_allow_html=True)
