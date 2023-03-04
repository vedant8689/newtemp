import streamlit as st

# Create a sidebar with a title
st.sidebar.title("Sidebar Title")

# Add some text to the sidebar
st.sidebar.text("This is some text in the sidebar.")

# Add a slider to the sidebar
value = st.sidebar.slider("Sidebar Slider", 0, 10)

# Print the value of the slider
st.write("Slider Value:", value)
