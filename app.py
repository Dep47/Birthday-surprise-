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

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "surprise_unlocked" not in st.session_state:
    st.session_state.surprise_unlocked = False

if "candles_out" not in st.session_state:
    st.session_state.candles_out = False


st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f6, #f5eaff, #ffe4ef);
}

.block-container {
    max-width: 750px;
    padding-top: 2rem;
}

h1, h2, h3, p {
    text-align: center;
}

.stButton button {
    width: 100%;
    border-radius: 30px;
    border: none;
    background: linear-gradient(90deg, #ff77aa, #c084fc);
    color: white;
    font-weight: bold;
    padding: 12px;
}

.stButton button:hover {
    color: white;
    border: 1px solid white;
}

</style>
""", unsafe_allow_html=True)


def go_to_page(page):
    st.session_state.page = page


# ---------------- PAGE 1: WELCOME ----------------

if st.session_state.page == 1:

    components.html("""
    <div style="text-align:center;padding:15px;">
        <div style="font-size:45px;">🎀 💗 🎀</div>
        <div style="font-size:55px;">🌸</div>
    </div>
    """, height=120)

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.75);
        padding:30px 20px;
        border-radius:30px;
        text-align:center;
        box-shadow:0 8px 25px rgba(200,100,150,0.15);
    ">
        <h1 style="color:#d63384;">Happy Birthday Munu! ❤️</h1>

        <h3 style="color:#a8558e;">A little surprise made with love...</h3>

        <p style="color:#80536b;font-size:18px;">
            Today is all about you.
            I made something special just for you.
        </p>

        <div style="font-size:40px;">🦋 🌷 💕 🌷 🦋</div>

        <h2 style="color:#c02675;">Deep ❤️ Munu</h2>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        "<h3 style='color:#a8558e;'>Before opening your surprise... 💌</h3>",
        unsafe_allow_html=True
    )

    questions = [
        "1. Do you love me? ❤️",
        "2. Do you miss me? 🥺",
        "3. Will you stay with me forever? 💍"
    ]

    options = ["Yes ❤️", "Think 🤔", "No 🙈"]

    for i, question in enumerate(questions):
        st.markdown(
            f"<h4 style='color:#a33d70;'>{question}</h4>",
            unsafe_allow_html=True
        )

        st.session_state.answers[i] = st.radio(
            "Choose your answer:",
            options,
            key=f"question_{i}",
            horizontal=True
        )

    st.write("")

    if st.button("🎁 UNLOCK MY SURPRISE ❤️"):

        if all(
            st.session_state.answers.get(i) == "Yes ❤️"
            for i in range(3)
        ):
            st.session_state.surprise_unlocked = True
            st.success("Awww! All correct answers! ❤️")

        else:
            st.session_state.surprise_unlocked = False
            st.warning("You have to say YES to all three questions! 🙈")

    if st.session_state.surprise_unlocked:

        st.markdown("""
        <div style="
            background:#fff0f6;
            padding:20px;
            border-radius:20px;
            text-align:center;
        ">
            <h2 style="color:#d63384;">Yayyyy! ❤️</h2>
            <p style="font-size:20px;color:#a8558e;">
                Your birthday surprise is waiting for you!
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("OPEN YOUR BIRTHDAY SURPRISE 🎂"):
            go_to_page(2)
            st.rerun()


# ---------------- PAGE 2: BIRTHDAY CELEBRATION ----------------

elif st.session_state.page == 2:

    components.html("""
    <div style="text-align:center;">
        <div style="font-size:35px;">🎈 🎀 🎈 🎉 🎈</div>
        <div style="font-size:50px;">🎂</div>
    </div>
    """, height=120)

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.8);
        border-radius:30px;
        padding:25px 15px;
        text-align:center;
        box-shadow:0 8px 25px rgba(200,100,150,0.15);
    ">
        <h1 style="color:#d63384;">Happy Birthday Munu! 🎂</h1>

        <h3 style="color:#a8558e;">My favourite person ❤️</h3>

        <p style="font-size:17px;color:#80536b;">
            Today the world became more beautiful
            because you were born.
        </p>

        <div style="font-size:35px;">🌸 🦋 💗 🦋 🌸</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        "<h2 style='color:#d63384;'>🎂 Make a Birthday Wish!</h2>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="text-align:center;font-size:65px;">
        🎂
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.candles_out:

        st.markdown(
            "<p style='color:#a8558e;'>Close your eyes and make a wish! ✨</p>",
            unsafe_allow_html=True
        )

        if st.button("🕯️ BLOW THE CANDLES"):

            st.session_state.candles_out = True
            st.rerun()

    else:

        st.markdown("""
        <div style="
            background:#fff0f6;
            padding:20px;
            border-radius:20px;
            text-align:center;
        ">
            <h2 style="color:#d63384;">Wish made! ✨</h2>
            <p style="font-size:20px;color:#a8558e;">
                May all your dreams come true, Munu! ❤️
            </p>
            <div style="font-size:35px;">🎉 🎊 💗 🎊 🎉</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        "<h2 style='color:#d63384;'>Our Little Memories 📸</h2>",
        unsafe_allow_html=True
    )

    image_extensions = [".jpg", ".jpeg", ".png", ".webp"]

    image_files = []

    for extension in image_extensions:
        image_files.extend(
            Path(".").glob(f"*{extension}")
        )

    image_files = sorted(image_files)

    if image_files:

        for i, photo in enumerate(image_files[:3]):

            st.image(
                str(photo),
                use_container_width=True
            )

            captions = [
                "A beautiful moment ❤️",
                "My favourite smile 🥰",
                "Forever special 💗"
            ]

            st.markdown(
                f"<p style='color:#a8558e;'>{captions[i]}</p>",
                unsafe_allow_html=True
            )

    else:

        st.info(
            "Add your three birthday photos to the same folder as app.py."
        )

    st.write("")

    st.markdown(
        "<h2 style='color:#d63384;'>A Song Just For You 🎵</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:#80536b;'>Listen to this special birthday song! ❤️</p>",
        unsafe_allow_html=True
    )

    components.html("""
    <div style="border-radius:20px;overflow:hidden;">
        <iframe
            width="100%"
            height="220"
            src="https://www.youtube.com/embed/LXd5OV5WjGE"
            title="Birthday Song"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
        </iframe>
    </div>
    """, height=230)

    st.write("")

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#fff0f6,#f3e8ff);
        padding:25px;
        border-radius:25px;
        text-align:center;
    ">
        <h2 style="color:#d63384;">One More Surprise... 💌</h2>

        <p style="color:#80536b;font-size:17px;">
            I have something from my heart to tell you.
        </p>

        <div style="font-size:35px;">💌 🌷 ❤️</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 OPEN MY LETTER"):

        go_to_page(3)
        st.rerun()

    st.write("")

    if st.button("⬅️ BACK TO WELCOME PAGE"):

        go_to_page(1)
        st.rerun()


# ---------------- PAGE 3: ASSAMESE BIRTHDAY LETTER ----------------

elif st.session_state.page == 3:

    components.html("""
    <div style="text-align:center;padding:15px;">
        <div style="font-size:45px;">💌 🌷 💗 🌷 💌</div>
    </div>
    """, height=100)

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#fff7fb,#ffe6f0);
        border:2px solid #f2b3d0;
        border-radius:25px;
        padding:25px;
        color:#80536b;
        line-height:1.9;
        box-shadow:0 8px 25px rgba(174,91,137,0.13);
    ">

        <div style="text-align:center;font-size:45px;">
            💌 🌷 ❤️
        </div>

        <h2 style="color:#a33d70;text-align:center;">
            মোৰ মৰমৰ মুনু ❤️
        </h2>

        <p style="text-align:left;font-size:17px;">
            মোৰ মৰমৰ মুনু,
        </p>

        <p style="text-align:left;font-size:17px;">
            জন্মদিনৰ বহুত বহুত মৰম আৰু শুভেচ্ছা। ❤️
        </p>

        <p style="text-align:left;font-size:17px;">
            কি লিখিম ভাবি পোৱা নাই, মাথোঁ ইমানেই ক'ব বিচাৰোঁ যে তুমি মোৰ বাবে বহুত বিশেষ। সদায় কাষত থাকিব নোৱাৰিলেও মনত কিন্তু সদায় আছা।
        </p>

        <p style="text-align:left;font-size:17px;">
            তোমাৰ মুখৰ হাঁহিটো সদায় এনেকৈয়ে থাকক। তুমি যি বিচৰা, জীৱনত সকলো পাবা। মাজে মাজে কাজিয়া হ'ব, অভিমান হ'ব, কিন্তু তাৰ মাজতো আমাৰ মৰমখিনি এনেকৈয়ে থাকক।
        </p>

        <p style="text-align:left;font-size:17px;">
            আজি তোমাৰ বাবে বিশেষ দিন, দিনটো ভালকে যাওঁক, সুখী হৈ থাকিবা আৰু নিজৰ যত্ন ল'বা।
        </p>

        <p style="text-align:left;font-size:17px;">
            Happy Birthday, Munu. বহুত মৰম তোমালৈ। ❤️
        </p>

        <div style="text-align:center;font-size:35px;margin-top:20px;">
            💗 🦋 🌸 💗
        </div>

        <h3 style="text-align:right;color:#a33d70;">
            Forever yours,<br>
            Deep ❤️
        </h3>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div style="text-align:center;">
        <h2 style="color:#d63384;">I LOVE YOU, MUNU ❤️</h2>
        <div style="font-size:40px;">🌹 💗 🦋 💗 🌹</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅️ BACK TO BIRTHDAY CELEBRATION"):

        go_to_page(2)
        st.rerun()
