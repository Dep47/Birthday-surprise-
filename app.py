import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = 1

if "answer" not in st.session_state:
    st.session_state.answer = None

if "candles_out" not in st.session_state:
    st.session_state.candles_out = False


if st.session_state.page == 1:

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

        if st.button("🎁 OPEN YOUR SURPRISE"):
            st.session_state.page = 2
            st.rerun()

    else:
        st.button(
            "🔒 SURPRISE LOCKED — SAY YES ❤️",
            disabled=True
        )

    st.markdown("""
    <br>
    <div style="text-align:center;color:#a35b91;">
        Made with love by Deep ❤️<br>
        <small>A little piece of my heart, just for you.</small>
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.page == 2:

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe0ed, #eadcff, #fff0d9);
    }
    .block-container {
        max-width: 850px;
        padding-top: 1.5rem;
    }
    .birthday-title {
        text-align: center;
        color: #b33e78;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 2px 3px 8px #ffffff;
    }
    .birthday-subtitle {
        text-align: center;
        color: #875477;
        font-size: 19px;
    }
    .photo-card {
        background: white;
        padding: 10px;
        border-radius: 18px;
        box-shadow: 0 7px 20px #bd82a555;
        margin-bottom: 15px;
    }
    .photo-caption {
        text-align: center;
        color: #a33d70;
        font-size: 16px;
        padding: 8px;
    }
    .cake-box {
        text-align: center;
        background: #ffffffa8;
        border: 2px solid #f2b3d0;
        border-radius: 25px;
        padding: 20px;
        margin: 25px 0;
    }
    .stButton > button {
        width: 100%;
        min-height: 52px;
        border-radius: 18px;
        background: #fff5fa;
        color: #a33d70;
        border: 2px solid #efa8c8;
        font-size: 17px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    components.html("""
    <div style="height:100px; overflow:hidden; position:relative;">
    <style>
    .balloon {
        position:absolute;
        bottom:-100px;
        font-size:45px;
        animation:float 7s infinite ease-in;
    }
    .b1 {left:8%;animation-delay:0s;}
    .b2 {left:28%;animation-delay:2s;}
    .b3 {left:52%;animation-delay:1s;}
    .b4 {left:75%;animation-delay:3s;}
    .b5 {left:90%;animation-delay:1.5s;}
    @keyframes float {
        0% {transform:translateY(0) rotate(0deg);opacity:0;}
        15% {opacity:1;}
        100% {transform:translateY(-220px) rotate(20deg);opacity:0;}
    }
    </style>
    <div class="balloon b1">🎈</div>
    <div class="balloon b2">🎀</div>
    <div class="balloon b3">🎈</div>
    <div class="balloon b4">💗</div>
    <div class="balloon b5">🎈</div>
    </div>
    """, height=100)

    st.markdown("""
    <div class="birthday-title">
        Happy Birthday, My Munu! ❤️
    </div>
    <div class="birthday-subtitle">
        Today the world feels a little more beautiful because of you. 🌷
    </div>
    """, unsafe_allow_html=True)

    components.html("""
    <div style="text-align:center;font-size:28px;padding:15px;">
    <div style="animation:sparkle 2s infinite;">
    ✨ 🎊 🎉 ✨ 🎊 🎉 ✨
    </div>
    <style>
    @keyframes sparkle {
        0%,100% {transform:scale(1);}
        50% {transform:scale(1.08);}
    }
    </style>
    </div>
    """, height=75)

    st.markdown("""
    <div class="cake-box">
        <div style="font-size:85px;">🎂</div>
        <h2 style="color:#b33e78;">Make a Birthday Wish, Munu! 💗</h2>
        <p style="color:#875477;">
        Close your eyes, make a wish and get ready to blow out your candles.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.candles_out:
        st.markdown("""
        <h2 style="text-align:center;color:#b33e78;">
        🌟 Your wish is on its way! 🌟
        </h2>
        <div style="text-align:center;font-size:65px;">🎂💨💗</div>
        """, unsafe_allow_html=True)

        if st.button("🕯️ LIGHT THE CANDLES AGAIN"):
            st.session_state.candles_out = False
            st.rerun()

    else:
        st.markdown("""
        <div style="text-align:center;font-size:45px;">
        🕯️ 🕯️ 🕯️
        </div>
        """, unsafe_allow_html=True)

        if st.button("💨 BLOW OUT YOUR CANDLES"):
            st.session_state.candles_out = True
            st.rerun()

    st.markdown("""
    <h2 style="text-align:center;color:#a33d70;">
    A Birthday Girl Deserves All The Attention! 🌸
    </h2>
    <p style="text-align:center;color:#875477;">
    A few beautiful pictures of the birthday girl herself. ❤️
    </p>
    """, unsafe_allow_html=True)

    photo_files = [
        ("photos/munu1.jpg", "Our Birthday Princess 👑"),
        ("photos/munu2.jpg", "Simply Beautiful 🌷"),
        ("photos/munu3.jpg", "Keep Smiling, Munu! 💗")
    ]

    for photo, caption in photo_files:
        if os.path.exists(photo):
            st.markdown('<div class="photo-card">', unsafe_allow_html=True)

            st.image(photo, use_container_width=True)

            st.markdown(
                f'<div class="photo-caption">{caption}</div>',
                unsafe_allow_html=True
            )

            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.warning(f"Please upload {photo} to your GitHub repository.")

    st.markdown("""
    <div style="text-align:center;background:#ffffffa8;
    border:2px solid #f2b3d0;border-radius:25px;padding:22px;">
        <div style="font-size:45px;">🎵 🎶 💗</div>
        <h2 style="color:#a33d70;">A Song for My Birthday Girl</h2>
        <p style="color:#875477;">Aji Munu Jonmodin ❤️</p>
    </div>
    """, unsafe_allow_html=True)

    components.html("""
    <div style="text-align:center;">
    <iframe
        width="100%"
        height="100"
        src="https://www.youtube.com/embed/LXd5OV5WjGE"
        title="Aji Munu Jonmodin"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
    </div>
    """, height=115)

    st.markdown("""
    <div style="text-align:center;background:#ffffffa8;
    border-radius:25px;padding:25px;margin-top:25px;">
        <div style="font-size:55px;">💌</div>
        <h2 style="color:#a33d70;">One More Little Surprise...</h2>
        <p style="color:#875477;">
        There are some things I want to tell you from my heart.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.button("💌 READ MY BIRTHDAY LETTER")

    st.markdown("""
    <br>
    <div style="text-align:center;color:#a35b91;">
    Made with endless love by Deep ❤️<br>
    <small>Happy Birthday once again, Munu! 🎂</small>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🏠 BACK TO WELCOME PAGE"):
        st.session_state.page = 1
        st.rerun()

    st.stop()
