
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "surprise_open" not in st.session_state:
    st.session_state.surprise_open = False

if "candles_blown" not in st.session_state:
    st.session_state.candles_blown = False

if "part3_open" not in st.session_state:
    st.session_state.part3_open = False

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe4ec, #fff0f5, #fce4ec);
}
h1, h2, h3, p {
    color: #8e2455;
}
.cinematic {
    text-align: center;
    padding: 25px 10px;
    animation: fadeIn 2s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
.hearts {
    text-align: center;
    font-size: 30px;
    animation: float 3s infinite ease-in-out;
}
@keyframes float {
    0%, 100% {transform: translateY(0);}
    50% {transform: translateY(-15px);}
}
.cake {
    font-size: 100px;
    text-align: center;
    animation: bounce 2s infinite;
}
@keyframes bounce {
    0%, 100% {transform: translateY(0);}
    50% {transform: translateY(-12px);}
}
.love-text {
    text-align: center;
    font-size: 20px;
    font-style: italic;
    color: #a83268;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("Happy Birthday, Munu! ❤️")
st.subheader("A little surprise, made just for you.")

st.markdown("## 👦🏻 ❤️ 👧🏻")
st.caption("Deep ❤️ Munu")

st.write("Some people make life more beautiful just by being in it.")

st.balloons()
st.divider()

st.header("One Important Question! 😍")
st.write("Munu, do you love Deep? ❤️")

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
    st.success("Yay! Deep is the happiest person! ❤️")
    st.image(
        "https://gifdb.com/images/branded/high/dancing-cartoon-couple-n4ezj8115cv7paxs.gif",
        width=300
    )

elif st.session_state.answer == "think":
    st.info("Take your time, Munu. Deep is waiting patiently. ❤️")
    st.markdown("## 🤔💭")

elif st.session_state.answer == "no":
    st.error("Oh no! Deep's heart is broken! 💔")
    st.markdown("## 😭🥺💔")

st.divider()

st.header("Your Special Surprise 🎁")

if st.session_state.answer == "yes":

    if not st.session_state.surprise_open:
        if st.button("OPEN YOUR SURPRISE 🎁"):
            st.session_state.surprise_open = True
            st.rerun()

    else:
        st.balloons()

        st.markdown("""
        <div class="cinematic">
            <div class="hearts">💗 🌸 💕 🌷 💗</div>
            <h1>Wait... there's something more for you, Munu.</h1>
            <p class="love-text">
                Welcome to your little world. ❤️
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.markdown("""
        <div class="cinematic">
            <h1>Happy Birthday, My Munu! 🎂</h1>
            <div class="cake">🎂</div>
            <h2>Make a wish! ✨</h2>
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.candles_blown:
            if st.button("BLOW OUT THE CANDLES 🕯️"):
                st.session_state.candles_blown = True
                st.balloons()
                st.rerun()
        else:
            st.markdown("""
            <div class="cinematic">
                <h1>✨ Wish made! ✨</h1>
                <div class="hearts">💖 💗 💕 💖</div>
            </div>
            """, unsafe_allow_html=True)
            st.snow()

        st.divider()

        st.header("A Song for You 🎶")

        components.iframe(
            "https://www.youtube.com/embed/LXd5OV5WjGE?autoplay=1&rel=0",
            height=220,
            scrolling=False
        )

        st.divider()

        st.markdown("""
        <div class="cinematic">
            <h1>Two Hearts, One Celebration ❤️</h1>
            <div style="font-size:75px;">👦🏻 💕 👧🏻</div>
            <p class="love-text">
                Even miles apart, I'm celebrating with you.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.markdown("""
        <div class="cinematic">
            <h2>There's something I want to tell you...</h2>
            <div class="hearts">💌 ❤️ 💌</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("CONTINUE ❤️"):
            st.session_state.part3_open = True
            st.rerun()

        if st.session_state.part3_open:
            st.divider()
            st.header("A Letter for Munu 💌")

else:
    st.button("🔒 Surprise Locked", disabled=True)
    st.caption("Only YES can unlock this surprise! ❤️")

st.divider()
st.caption("Made with ❤️ by Deep, specially for Munu.")
