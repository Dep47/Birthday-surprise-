
import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Munu ❤️",
    page_icon="🎂",
    layout="centered"
)

st.title("Happy Birthday, Munu! ❤️")

st.subheader("A little surprise, made just for you.")
st.markdown("## 👦🏻 ❤️ 👧🏻")
st.caption("Deep ❤️ Munu")

st.write("Some people make life more beautiful just by being in it.")

st.balloons()
st.divider()

st.header("One Important Question! 😍")

st.write("Munu, do you love Deep? ❤️")

if "love_answered" not in st.session_state:
    st.session_state.love_answered = False

if "answer" not in st.session_state:
    st.session_state.answer = ""

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("YES ❤️"):
        st.session_state.answer = "yes"
        st.session_state.love_answered = True

with col2:
    if st.button("THINK 🤔"):
        st.session_state.answer = "think"
        st.session_state.love_answered = True

with col3:
    if st.button("NO 💔"):
        st.session_state.answer = "no"
        st.session_state.love_answered = True

# CARTOON REACTIONS

if st.session_state.answer == "yes":

    st.success("Yay! Deep is the happiest person! ❤️")

    st.image(
        "https://gifdb.com/images/branded/high/dancing-cartoon-couple-n4ezj8115cv7paxs.gif",
        width=300
    )

elif st.session_state.answer == "think":

    st.info("Take your time, Munu. Deep is waiting patiently. ❤️")

    st.markdown("## 🤔💭")

    st.image(
        "https://media.tenor.com/7Z8nJ4K5wJAAAAAC/thinking.gif",
        width=300
    )

elif st.session_state.answer == "no":

    st.error("Oh no! Deep's heart is broken! 💔")

    st.markdown("## 😭🥺💔")

    st.image(
        "https://media.tenor.com/3u8xJZ8n7HAAAAAC/sad-cartoon.gif",
        width=300
    )

st.divider()

if st.button("Open Your Surprise 🎁"):

    if st.session_state.love_answered:
        st.success("Your surprise is ready, Munu! ❤️")
        st.balloons()

    else:
        st.warning("Please answer first, Munu! ❤️")

st.divider()

st.caption("Made with ❤️ by Deep, specially for Munu.")


