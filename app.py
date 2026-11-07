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
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("YES ❤️"):
        st.balloons()
        st.markdown("# 💃🕺❤️")
        st.success("Yay! Deep is the happiest person! ❤️")

with col2:
    if st.button("THINK 🤔"):
        st.markdown("# 🤔💭")
        
st.info("Take your time, Munu. Deep is waiting patiently. ❤️")

with col3:
    if st.button("NO 💔"):
        st.markdown("# 😭🥺💔")
        st.error("Oh no! Deep's heart is broken! 💔")


if st.button("Open Your Surprise 🎁"):
    st.success("You are special, Munu. Never forget that! ❤️")
