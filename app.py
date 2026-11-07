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

col1, col2 = st.columns(2)

with col1:
    if st.button("YES, Obviously! ❤️"):
        st.balloons()
        st.success("Yayyyy! I knew it! 😂❤️")

with col2:
    if st.button("Let me think... 🤔"):
        st.info("Take your time, Munu! 😂❤️")

if st.button("Open Your Surprise 🎁"):
    st.success("You are special, Munu. Never forget that! ❤️")
