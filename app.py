
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday, Munu ❤️",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).parent
PHOTO_DIR = ROOT / "photos"

PHOTO_ITEMS = [
    ("photo1.jpg", "Blue looks magical on you 💙"),
    ("photo2.jpg", "My favourite view, even from far away 🤍"),
    ("photo3.jpg", "A little chaos, a lot of memories. ❤️"),
]

SONG_EMBED_URL = (
    "https://www.youtube-nocookie.com/embed/videoseries"
    "?list=OLAK5uy_k9Dn0CJOLE0N_JMuT7dLMV-OfuyYzzE_8"
    "&rel=0"
)

LETTER_GREETING = "মোৰ মৰমৰ মুনু,"

LETTER_BODY = """জন্মদিনৰ বহুত বহুত মৰম আৰু শুভেচ্ছা। ❤️

কি লিখিম ভাবি পোৱা নাই, মাথোঁ ইমানেই ক'ব বিচাৰোঁ যে তুমি মোৰ বাবে বহুত বিশেষ। সদায় কাষত থাকিব নোৱাৰিলেও মনত কিন্তু সদায় আছা।

তোমাৰ মুখৰ হাঁহিটো সদায় এনেকৈয়ে থাকক। তুমি যি বিচৰা, জীৱনত সকলো পাবা। মাজে মাজে কাজিয়া হ'ব, অভিমান হ'ব, কিন্তু তাৰ মাজতো আমাৰ মৰমখিনি এনেকৈয়ে থাকক।

আজি তোমাৰ বাবে বিশেষ দিন, দিনটো ভালকে যাওঁক, সুখী হৈ থাকিবা আৰু নিজৰ যত্ন ল'বা।

Happy Birthday, Munu. বহুত মৰম তোমালৈ। ❤️"""

LETTER_CLOSING = "সদায় তোমাৰ,"
LETTER_SIGNATURE = "Deep"

for key, default in {
    "answers_submitted": False,
    "surprise_opened": False,
    "letter_opened": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Noto+Serif+Bengali:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background: radial-gradient(ellipse at top, #39223d 0%, #1c1728 42%, #101827 100%);
    color: #fff5f7;
    font-family: 'Poppins', sans-serif;
}

.block-container {
    max-width: 760px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    color: #ffe5ed !important;
}

.hero {
    text-align: center;
    padding: 2.2rem 1rem 1.6rem;
    border: 1px solid rgba(255,220,235,.18);
    border-radius: 26px;
    background: linear-gradient(145deg, rgba(255,255,255,.10), rgba(255,255,255,.035));
    box-shadow: 0 18px 55px rgba(0,0,0,.22);
}

.eyebrow {
    color: #f4b9cc;
    letter-spacing: .22em;
    text-transform: uppercase;
    font-size: .72rem;
}

.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2.7rem, 9vw, 4.8rem);
    line-height: 1.04;
    margin: .5rem 0;
    color: #fff0f4;
}

.hero-sub {
    color: #f6d6e1;
    font-size: 1rem;
    line-height: 1.8;
}

.section-card {
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,220,235,.14);
    border-radius: 22px;
    padding: 1.2rem 1.25rem;
    margin: 1.2rem 0;
}

.soft {
    color: #e9cbd7;
    line-height: 1.8;
}

.rose-line {
    text-align: center;
    color: #f3a9c1;
    letter-spacing: .55rem;
    font-size: 1.2rem;
    margin: 1.1rem 0;
}

.photo-caption {
    text-align: center;
    color: #f8dce6;
    font-size: .95rem;
    margin: .35rem 0 1.3rem;
}

.letter {
    background: linear-gradient(145deg, #fff7f0, #ffe8ee);
    color: #563744;
    border-radius: 18px;
    padding: 1.5rem;
    box-shadow: 0 15px 45px rgba(0,0,0,.22);
    font-family: 'Noto Serif Bengali', serif;
    line-height: 2;
    white-space: pre-line;
    font-size: 1rem;
}

.letter .greeting {
    font-size: 1.25rem;
    font-weight: 700;
    color: #9b4566;
    margin-bottom: 1rem;
}

.letter .sign {
    text-align: right;
    margin-top: 1.4rem;
    color: #9b4566;
    font-weight: 600;
}

.ending {
    text-align: center;
    padding: 2.3rem 1rem;
    margin-top: 1.6rem;
    border-radius: 24px;
    background: linear-gradient(145deg, rgba(194,85,128,.22), rgba(255,255,255,.06));
    border: 1px solid rgba(255,210,230,.2);
}

.ending-main {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(1.8rem, 6vw, 2.8rem);
    color: #ffe5ed;
    line-height: 1.3;
}

.petals {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}

.petal {
    position: absolute;
    top: -12%;
    width: 12px;
    height: 18px;
    border-radius: 80% 0 80% 0;
    background: linear-gradient(135deg, #ffd5e2, #d94e83);
    opacity: .55;
    animation: fall linear infinite;
}

.petal:nth-child(1) {
    left: 8%;
    animation-duration: 13s;
    animation-delay: -4s;
}

.petal:nth-child(2) {
    left: 23%;
    animation-duration: 17s;
    animation-delay: -10s;
}

.petal:nth-child(3) {
    left: 39%;
    animation-duration: 14s;
    animation-delay: -7s;
}

.petal:nth-child(4) {
    left: 57%;
    animation-duration: 19s;
    animation-delay: -12s;
}

.petal:nth-child(5) {
    left: 74%;
    animation-duration: 15s;
    animation-delay: -5s;
}

.petal:nth-child(6) {
    left: 91%;
    animation-duration: 18s;
    animation-delay: -9s;
}

@keyframes fall {
    0% {
        transform: translate3d(0,-5vh,0) rotate(0);
    }
    100% {
        transform: translate3d(70px,115vh,0) rotate(540deg);
    }
}

div.stButton > button {
    border-radius: 999px;
    border: 1px solid rgba(255,220,235,.35);
    background: linear-gradient(110deg,#b84c78,#e47b9d);
    color: white;
    font-weight: 600;
    min-height: 2.8rem;
    padding: .45rem 1.3rem;
}

div.stButton > button:hover {
    border-color: #ffe2ec;
    color: white;
    background: linear-gradient(110deg,#cc5e89,#ef91ae);
}

div[data-testid="stRadio"] label {
    color: #fff1f5;
}

div[data-testid="stMarkdownContainer"] p {
    color: inherit;
}

footer {
    visibility: hidden;
}

@media(max-width:600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        padding: 1.8rem .8rem;
    }

    .section-card {
        padding: 1rem;
    }

    .letter {
        padding: 1.1rem;
        font-size: .94rem;
    }
}
</style>

<div class="petals">
    <span class="petal"></span>
    <span class="petal"></span>
    <span class="petal"></span>
    <span class="petal"></span>
    <span class="petal"></span>
    <span class="petal"></span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="eyebrow">A little surprise from Mumbai to Guwahati</div>
    <div class="hero-title">Happy Birthday,<br>Munu ❤️</div>
    <div class="hero-sub">
        Today is all about you.<br>
        Ready to open something made with love?
    </div>
    <div style="font-size:2rem;margin-top:.8rem">🌹 ✨ 🌹</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="rose-line">✿ ✿ ✿</div>', unsafe_allow_html=True)

if not st.session_state.surprise_opened:

    st.markdown("""
    <div class="section-card">
        <h3 style="text-align:center">Before your surprise… 💌</h3>
        <p class="soft" style="text-align:center">
            Answer these three little questions first.
            No pressure… but I might judge your answers. 😌
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("birthday_questions"):

        q1 = st.radio(
            "1. Munu, do you love Deep?",
            ["YES ❤️", "THINK 🤔", "NO 🙄"],
            index=None
        )

        q2 = st.radio(
            "2. What makes Deep happiest?",
            ["Talking with Munu 💬", "Pizza 🍕", "Sleeping 😴"],
            index=None
        )

        q3 = st.radio(
            "3. Where is Deep sending birthday wishes from?",
            ["Mumbai 🌃", "Guwahati 🌸", "The Moon 🌙"],
            index=None
        )

        submitted = st.form_submit_button(
            "Submit my answers 💗",
            use_container_width=True
        )

    if submitted:
        if not q1 or not q2 or not q3:
            st.warning("Answer all three questions first, Munu. 😊")
        else:
            st.session_state.answers_submitted = True
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.q3 = q3
            st.rerun()

    if st.session_state.answers_submitted:

        st.markdown("""
        <div class="section-card">
            <h3 style="text-align:center">Answers received! 😄</h3>
            <p class="soft" style="text-align:center">
                Okay, Munu… I accept your answers.
                Your surprise is waiting.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open your birthday surprise 🎁", use_container_width=True):
            st.session_state.surprise_opened = True
            st.balloons()
            st.snow()
            st.rerun()

else:

    st.balloons()

    st.markdown("""
    <div class="section-card" style="text-align:center">
        <div style="font-size:3rem">🎂 🎉 💖</div>
        <h2 style="font-family:'DM Serif Display',serif">
            It's your day, Munu!
        </h2>
        <p class="soft">
            A small celebration, made from miles away,
            with a whole lot of love.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="rose-line">🌹 &nbsp; 🌹 &nbsp; 🌹</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="section-card">
        <h3 style="text-align:center">A birthday song for you 🎶</h3>
        <p class="soft" style="text-align:center">
            Tap play and enjoy your little birthday moment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    components.iframe(SONG_EMBED_URL, height=180, scrolling=False)

    st.markdown(
        '<div class="rose-line">✿ ✿ ✿</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="section-card">
        <h2 style="text-align:center">A few moments of you 📸</h2>
        <p class="soft" style="text-align:center">
            Some memories deserve their own little place.
        </p>
    </div>
    """, unsafe_allow_html=True)

    found_photos = 0

    for filename, caption in PHOTO_ITEMS:
        image_path = PHOTO_DIR / filename

        if image_path.exists():
            found_photos += 1
            st.image(str(image_path), use_container_width=True)
            st.markdown(
                f'<div class="photo-caption">{caption}</div>',
                unsafe_allow_html=True
            )

    if found_photos == 0:
        st.info("Add your photos to the photos folder to show them here.")
    elif found_photos < 3:
        st.caption(
            f"{found_photos} of 3 photos found. "
            "Add the missing image files to the photos folder."
        )

    st.markdown(
        '<div class="rose-line">🌹 ✨ 🌹</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="section-card" style="text-align:center">
        <h2>A little letter for you 💌</h2>
        <p class="soft">
            Some things are easier to write than to say.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.letter_opened:

        st.markdown("""
        <div style="text-align:center;font-size:5rem">
            💌
        </div>
        <p class="soft" style="text-align:center">
            There's something inside, just for you.
        </p>
        """, unsafe_allow_html=True)

        if st.button("Open your letter 💗", use_container_width=True):
            st.session_state.letter_opened = True
            st.rerun()

    else:

        st.markdown(
            f'<div class="letter">'
            f'<div class="greeting">{LETTER_GREETING}</div>'
            f'{LETTER_BODY}'
            f'<div class="sign">{LETTER_CLOSING}<br>{LETTER_SIGNATURE}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("""
    <div class="ending">
        <div style="font-size:2.4rem">❤️ 🌙 ❤️</div>
        <div class="ending-main">
            Distance is just a number.<br>
            You're always close to my heart.
        </div>
        <p class="soft" style="margin-top:1rem">
            Happy Birthday, Munu.
            Always sending you love, from Mumbai. ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align:center;color:#d9afbf;font-size:.8rem;margin-top:2rem">
        Made with love, just for Munu · Deep ❤️
    </p>
    """, unsafe_allow_html=True)
