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

if st.button("Open Your Surprise 🎁"):
    st.success("You are special, Munu. Never forget that! ❤️")
