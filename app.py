if "love_answered" not in st.session_state:
    st.session_state.love_answered = False

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("YES ❤️"):
        st.session_state.love_answered = True
        st.balloons()
        st.image(
            "https://media.tenor.com/2roX3uxz_68AAAAC/cute-love.gif",
            width=250
        )
        st.success("Yay! Deep is the happiest person! ❤️")

with col2:
    if st.button("THINK 🤔"):
        st.session_state.love_answered = True
        st.image(
            "https://media.tenor.com/6Z2Y8Q3qJwAAAAAC/thinking.gif",
            width=250
        )
        st.info("Take your time, Munu. Deep is waiting patiently. ❤️")

with col3:
    if st.button("NO 💔"):
        st.session_state.love_answered = True
        st.image(
            "https://media.tenor.com/1J5Q3Y7XQ4AAAAAC/crying-sad.gif",
            width=250
        )
        st.error("Oh no! Deep's heart is broken! 💔")

st.divider()

if st.button("Open Your Surprise 🎁"):
    if st.session_state.love_answered:
        st.success("Your surprise is ready, Munu! ❤️")
        st.balloons()
    else:
        st.warning("Please answer first, Munu! ❤️")
