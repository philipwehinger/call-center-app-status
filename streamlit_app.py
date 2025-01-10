import streamlit as st

THUMBS_DOWN = "tommel_ned.png"
THUMBS_UP = "tommel_opp.png"
st.title("Is the call center APP running?")


# Initialize session state for the toggle
if "show_thumbs_up" not in st.session_state:
    st.session_state.show_thumbs_up = True

# Function to toggle the state
def toggle_image():
    st.session_state.show_thumbs_up = not st.session_state.show_thumbs_up

# Display the appropriate image based on state
if st.session_state.show_thumbs_up:
    st.image(THUMBS_UP, caption="Thumbs Up", use_container_width=True)
else:
    st.image(THUMBS_DOWN, caption="Thumbs Down", use_container_width =True)

# Button to toggle the state
st.button("Change Status", on_click=toggle_image)