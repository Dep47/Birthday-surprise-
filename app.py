import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="💗",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = 1

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe0ec, #f5e3ff, #fff0f5);
}
h1, h2, h3, p {
    font-family: Georgia, serif;
}
.stButton > button {
    width: 100%;
    border-radius: 20px;
    border: 2px solid #e99abb;
    background-color: #fff0f6;
    color: #a33d70;
    font-weight: bold;
    padding: 12px;
}
.stButton > button:hover {
    background-color: #f8c9dc;
    color: #8e285c;
    border-color: #a33d70;
}
</style>
""", unsafe_allow_html=True)


if st.session_state.page == 1:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;
    background:#ffffffb8;
    border:2px solid #f2b3d0;
    border-radius:30px;
    padding:30px 15px;">

        <div style="font-size:65px;">🎀 💗 🎂</div>

        <h1 style="color:#a33d70;font-size:38px;">
            Happy Birthday,
        </h1>

        <h1 style="color:#d65c91;font-size:48px;">
            My Munu! ❤️
        </h1>

        <p style="color:#875477;font-size:18px;">
            Today is all about you, my favourite person.
        </p>

        <div style="font-size:35px;">🌷 🦋 🌷</div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;
    background:#ffffffa8;
    border-radius:25px;
    padding:20px;">

        <h2 style="color:#a33d70;">
            One little question for you... 💌
        </h2>

        <p style="color:#875477;font-size:20px;">
            Do you love Deep? 🥺❤️
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("YES ❤️"):
            st.session_state.answer = "YES"

    with col2:
        if st.button("THINK 🤔"):
            st.session_state.answer = "THINK"

    with col3:
        if st.button("NO 🙈"):
            st.session_state.answer = "NO"

    if st.session_state.answer == "YES":

        st.success("Awww! I knew it! I love you too, Munu! ❤️")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🎁 OPEN YOUR SURPRISE 🎁"):
            st.session_state.page = 2
            st.rerun()

    elif st.session_state.answer == "THINK":

        st.warning("Take your time, Munu! But don't think too much. 😂💕")

    elif st.session_state.answer == "NO":

        st.error("Wrong answer! Try again, birthday girl! 😂❤️")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align:center;color:#a33d70;">
        Made with endless love, just for you. 💗
    </p>
    """, unsafe_allow_html=True)


elif st.session_state.page == 2:

    st.markdown("""
    <div style="text-align:center;
    background:#ffffffb8;
    border:2px solid #f2b3d0;
    border-radius:30px;
    padding:25px 15px;">

        <div style="font-size:50px;">🎈 🎂 🎈</div>

        <h1 style="color:#a33d70;font-size:38px;">
            Happy Birthday Munu!
        </h1>

        <h2 style="color:#d65c91;">
            My Beautiful Birthday Girl ❤️
        </h2>

        <p style="color:#875477;font-size:18px;">
            Today, the world became more beautiful
            because you were born. 🌸
        </p>

        <div style="font-size:35px;">💗 🦋 💗</div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;
    background:#ffffffa8;
    border:2px solid #f2b3d0;
    border-radius:25px;
    padding:20px;">

        <h2 style="color:#a33d70;">
            A Birthday Cake for You! 🎂
        </h2>

        <div style="font-size:90px;">🎂</div>

        <p style="color:#875477;">
            Close your eyes, make a wish and blow the candles! ✨
        </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("🎂 BLOW THE CANDLES"):
        st.balloons()
        st.success("Your wish deserves to come true, Munu! ❤️")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;
    background:#ffffffa8;
    border:2px solid #f2b3d0;
    border-radius:25px;
    padding:22px;">

        <h2 style="color:#a33d70;">
            Our Little Memories 📸
        </h2>

        <p style="color:#875477;">
            Some moments deserve to stay forever. 💕
        </p>

    </div>
    """, unsafe_allow_html=True)

    image_extensions = [".jpg", ".jpeg", ".png", ".webp"]

    image_files = sorted([
        file for file in Path(__file__).parent.iterdir()
        if file.is_file() and file.suffix.lower() in image_extensions
    ])

    if image_files:
        for photo in image_files:
            st.image(str(photo), use_container_width=True)
    else:
        st.info("Your photos will appear here after uploading them to GitHub.")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;
    background:#ffffffa8;
    border:2px solid #f2b3d0;
    border-radius:25px;
    padding:22px;">

        <div style="font-size:45px;">🎵 🎶 💗</div>

        <h2 style="color:#a33d70;">
            A Song for My Birthday Girl
        </h2>

        <p style="color:#875477;">
            Aji Munu Jonmodin ❤️
        </p>

        <p style="color:#875477;">
            This song is dedicated to you, Munu. 💕
        </p>

    </div>
    """, unsafe_allow_html=True)

    components.html("""
    <div style="border-radius:15px;overflow:hidden;">
    <iframe
        width="100%"
        height="220"
        src="https://www.youtube.com/embed/LXd5OV5WjGE?autoplay=1&playsinline=1"
        title="Aji Munu Jonmodin"
        frameborder="0"
        allow="autoplay; encrypted-media; picture-in-picture"
        allowfullscreen>
    </iframe>
    </div>
    """, height=230)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;
    background:#ffffffa8;
    border:2px solid #f2b3d0;
    border-radius:25px;
    padding:22px;">

        <div style="font-size:45px;">💌 🌷 💗</div>

        <h2 style="color:#a33d70;">
            A Letter From Deep
        </h2>

        <p style="color:#875477;">
            A few words from my heart, only for you.
        </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 READ MY BIRTHDAY LETTER"):
        st.session_state.letter_open = not st.session_state.letter_open

    if st.session_state.letter_open:

        st.markdown("""
        <div style="background:#fff7fb;
        border:2px solid #f2b3d0;
        border-radius:20px;
        padding:25px;
        color:#875477;
        line-height:1.8;">

            <h2 style="text-align:center;color:#a33d70;">
                My Dear Munu ❤️
            </h2>

            <p>Happy Birthday, my love. ❤️</p>

            <p>
                I wish I could be beside you today,
                celebrate with you, see your beautiful smile
                and make this day even more special.
            </p>

            <p>
                Even though we are miles apart,
                you are always close to my heart.
                I hope this little surprise makes you smile.
            </p>

            <p>
                May your life be filled with happiness,
                success, peace and endless beautiful moments.
            </p>

            <p>
                Keep smiling, keep shining and never stop
                being the wonderful person you are.
            </p>

            <h3 style="text-align:right;color:#a33d70;">
                Forever yours,<br>
                Deep ❤️
            </h3>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;
    color:#a33d70;
    padding:20px;">

        <h2>Made with Love ❤️</h2>

        <p>Distance means nothing when someone means everything.</p>

        <div style="font-size:35px;">💗 🎀 🦋</div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("🏠 BACK TO HOMEPAGE"):
        st.session_state.page = 1
        st.session_state.answer = ""
        st.session_state.letter_open = False
        st.rerun()
