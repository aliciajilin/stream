import streamlit as st
st.write("Hello")

categories = ['a', 'b', 'c']
st.multiselect("pick an option!", categories)
st.button("Click me!")
if st.checkpox("Select me!"):
    st.write("you selected the checkbox!")
    
    
