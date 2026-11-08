import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = 1

if "answer" not in st.session_state:
    st.session_state.answer = None

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe0ec, #eadcff, #fff0f5);
}
.main .block-container {
    max-width: 800px;
    padding-top: 2rem;
}
.title {
    color: #d63384;
    font-size: 42px;
    font-weight: 800;
    text-align: center;
}
.subtitle {
    color: #9344a8;
    text-align: center;
    font-size: 19px;
}
.card {
    background: rgba(255,255,255,0.78);
    padding: 25px;
    border-radius: 24px;
    text-align: center;
    box-shadow: 0 6px 25px rgba(180,100,150,0.15);
    margin: 18px 0;
}
.photo-caption {
    color: #b83280;
    text-align: center;
    font-size: 17px;
    font-weight: bold;
}
.footer {
    text-align: center;
    color: #a64d79;
    margin-top: 35px;
}
.stButton button {
    border-radius: 18px;
    border: 1px solid #e7a4c5;
    background-color: #fff5fa;
    color: #b83280;
    font-weight: bold;
    min-height: 45px;
}
</style>
""", unsafe_allow_html=True)


def show_photo(filename, caption):
    path = Path("photos") / filename

    if path.exists():
        st.image(str(path), use_container_width=True)
        st.markdown(
            f'<div class="photo-caption">{caption}</div>',
            unsafe_allow_html=True
        )


if st.session_state.page == 1:

    st.markdown(
        '<div class="title">Happy Birthday, Munu! ❤️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Today is all about you ✨</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>🌸 A Little World, Made Just for You 🌸</h3>
        Someone as special as you deserves a little extra magic today.
        <br><br>
        I have a small surprise waiting for you. 💗
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### One important question... 🥺")
    st.markdown("### Do you love Deep? ❤️")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("YES ❤️", use_container_width=True):
            st.session_state.answer = "yes"

    with col2:
        if st.button("THINK 🤔", use_container_width=True):
            st.session_state.answer = "think"

    with col3:
        if st.button("NO 💔", use_container_width=True):
            st.session_state.answer = "no"

    if st.session_state.answer == "yes":

        st.image(
            "https://media.tenor.com/2roX3uxz_68AAAAC/cute-love.gif",
            use_container_width=True
        )

        st.success("Yayyyy! I knew it! Deep is smiling like crazy! ❤️")
        st.balloons()

        if st.button("Open Your Surprise 🎁", use_container_width=True):
            st.session_state.page = 2
            st.rerun()

    elif st.session_state.answer == "think":

        st.image(
            "https://media.tenor.com/6Z2Y8Q3qJwAAAAAC/thinking.gif",
            use_container_width=True
        )

        st.info("Awww, take your time Munu! 🤭")

    elif st.session_state.answer == "no":

        st.image(
            "https://media.tenor.com/1J5Q3Y7XQ4AAAAAC/crying-sad.gif",
            use_container_width=True
        )

        st.error("Nooooo! Deep's little heart is broken! 💔")

    st.markdown(
        '<div class="footer">Made with love by Deep ❤️</div>',
        unsafe_allow_html=True
    )


elif st.session_state.page == 2:

    st.markdown("""
    <div style="text-align:center; padding:20px 5px;">
        <div style="font-size:45px;">🎈🌸🎂🌸🎈</div>
        <h1 style="color:#d63384; font-size:43px;">
            Happy Birthday!
        </h1>
        <h2 style="color:#9344a8;">
            My Beautiful Munu ❤️
        </h2>
        <p style="font-size:18px; color:#9344a8;">
            Today is your day. Let the celebration begin!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    components.html("""
    <div style="position:relative; height:100px; overflow:hidden;">
        <div style="position:absolute; width:100%; text-align:center;
        font-size:28px; animation: float 3s infinite ease-in-out;">
        🎉 ✨ 💗 🌹 ✨ 🎊 💕
        </div>
    </div>
    <style>
    @keyframes float {
        0% {transform:translateY(10px);}
        50% {transform:translateY(-15px);}
        100% {transform:translateY(10px);}
    }
    </style>
    """, height=100)

    st.markdown("""
    <div class="card">
        <div style="font-size:55px;">🎂</div>
        <h2 style="color:#d63384;">Make a Wish, Munu!</h2>
        <p style="font-size:18px; color:#75416c;">
            May your life always be filled with happiness,
            endless laughter, beautiful memories and dreams
            that come true.
        </p>
        <div style="font-size:30px;">🌹 💐 🌷</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎶 A Song Just for You")

    components.html("""
    <div style="text-align:center;">
        <iframe
            width="100%"
            height="100"
            src="https://www.youtube.com/embed/LXd5OV5WjGE?autoplay=1&loop=1&playlist=LXd5OV5WjGE"
            title="Aji Munu Jonmodin"
            frameborder="0"
            allow="autoplay; encrypted-media"
            allowfullscreen>
        </iframe>
    </div>
    """, height=110)

    st.markdown("""
    <div class="card">
        <h2 style="color:#d63384;">Our Little Memory Gallery 📸</h2>
        <p style="color:#9344a8;">
            Three pictures, countless reasons to smile. ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

    show_photo("photo1.jpg", "That beautiful smile ❤️")
    show_photo("photo2.jpg", "Elegance in every moment 🌸")
    show_photo("photo3.jpg", "My favourite person 💗")

    st.markdown("""
    <div class="card">
        <div style="font-size:35px;">💌</div>
        <h2 style="color:#d63384;">A Little Message From My Heart</h2>
        <p style="color:#75416c; font-size:18px;">
            Some things are difficult to express in words.
            But today, I want you to know how special you are.
            Keep smiling, Munu. You deserve all the beautiful
            things life has to offer.
        </p>
        <div style="font-size:28px;">❤️ 🌹 ❤️</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Read My Birthday Letter 💌", use_container_width=True):
        st.info("Your personal birthday letter will be on the next page. ❤️")

    if st.button("⬅ Back to Home", use_container_width=True):
        st.session_state.page = 1
        st.rerun()

    st.markdown(
        '<div class="footer">With all my love, Deep ❤️</div>',
        unsafe_allow_html=True
    )
