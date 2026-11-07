
import streamlit as st
import time
import os

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="❤️",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe0ec, #fff0f5, #f8d7ff);
}
h1, h2, h3, p {
    color: #a52a62;
    text-align: center;
}
.question {
    background: rgba(255,255,255,0.75);
    padding: 22px;
    border-radius: 20px;
    text-align: center;
    margin: 15px 0;
    box-shadow: 0 4px 15px rgba(180,50,100,0.12);
}
.stButton button {
    border-radius: 25px;
    background-color: #ff69a6;
    color: white;
    border: none;
    font-weight: bold;
    width: 100%;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "surprise" not in st.session_state:
    st.session_state.surprise = False

st.markdown("# 🎀 Happy Birthday Munu ❤️")
st.markdown("### A little surprise from someone who misses you.")

st.markdown("""
<div class="question">
<h2>Hey Munu! 💗</h2>
<p>Before opening your birthday surprise, answer these three little questions.</p>
</div>
""", unsafe_allow_html=True)

questions = [
    "Munu, do you love Deep? ❤️",
    "Do you miss me sometimes? 🥺",
    "Will you accept my little birthday surprise? 🎁"
]

for i, question in enumerate(questions):
    st.markdown(f"""
    <div class="question">
    <h3>{question}</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("YES ❤️", key=f"yes{i}"):
            st.session_state.answers[i] = "YES"

    with col2:
        if st.button("THINK 🤔", key=f"think{i}"):
            st.session_state.answers[i] = "THINK"

    with col3:
        if st.button("NO 🙈", key=f"no{i}"):
            st.session_state.answers[i] = "NO"

    answer = st.session_state.answers.get(i)

    if answer == "YES":
        st.success("Awww! I knew it! ❤️")
    elif answer == "THINK":
        st.info("Take your time, Munu. I'm waiting! 🥺")
    elif answer == "NO":
        st.warning("Ouch! My heart needs a hug. 😂")

st.markdown("---")

if all(st.session_state.answers.get(i) == "YES" for i in range(3)):
    st.balloons()

    if st.button("🔓 OPEN YOUR SURPRISE ❤️"):
        st.session_state.surprise = True

else:
    st.markdown("### 🔒 Your surprise is waiting...")
    st.caption("Answer YES to all three questions to unlock it. ❤️")

if st.session_state.surprise:

    st.markdown("---")
    st.markdown("# 🎉 SURPRISE MUNU! 🎉")
    st.markdown("## Happy Birthday, My Favourite Person ❤️")

    st.markdown("""
    <div class="question">
    <h2>🎂 Make a wish, Munu! 🎂</h2>
    <h1>💗 🕯️ 💗</h1>
    <p>Even miles apart, I'm celebrating with you.</p>
    </div>
    """, unsafe_allow_html=True)

    st.snow()

    st.markdown("## 🎵 A song for you")

    st.video("https://youtu.be/LXd5OV5WjGE")

    st.markdown("## 📸 Our Little Memories")

    photos = ["photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg"]

    for photo in photos:
        if os.path.exists(photo):
            st.image(photo, use_container_width=True)

    st.markdown("## 💌 A Little Letter For You")

    st.markdown("""
    <div class="question">
    <h3>My Munu ❤️</h3>
    <p>
    আজি তোমাৰ জন্মদিন। দূৰত থাকিলেও আজি দিনটো
    মোৰ বাবেও বহুত বিশেষ।

    তোমাৰ হাঁহিটো সদায় এনেকৈয়ে থাকক।
    জীৱনৰ প্ৰতিটো সপোন পূৰণ হওক।

    মই সদায় বিচাৰোঁ তুমি সুখী হোৱা।
    আৰু তোমাৰ এই বিশেষ দিনটো বহুত ধুনীয়াকৈ পাৰ হওক।

    Happy Birthday, Munu! ❤️
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("# ❤️ Always keep smiling, Munu!")
