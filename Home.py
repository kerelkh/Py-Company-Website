import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write(""""The quick brown fox jumps over the lazy dog" is an English-language pangram — a sentence that contains all the letters of the alphabet. The phrase is commonly used for touch-typing practice, testing typewriters and computer keyboards, displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.""")

st.subheader("Our team")

col1, col2, col3 = st.columns(3)

datas = pd.read_csv("data.csv")

with col1:
    for i, data in datas[:4].iterrows():
        st.write(f"{data[0]} {data[1]}")
        st.write(data[2])
        st.image(f"assets/images/{data[3]}")

with col2:
    for i, data in datas[4:8].iterrows():
        st.write(f"{data[0]} {data[1]}")
        st.write(data[2])
        st.image(f"assets/images/{data[3]}")

with col3:
    for i, data in datas[8:].iterrows():
        st.write(f"{data[0]} {data[1]}")
        st.write(data[2])
        st.image(f"assets/images/{data[3]}")