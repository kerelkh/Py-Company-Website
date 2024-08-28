import streamlit as st
import send_email as se
import pandas as pd

st.header("Contact Us")

topics = pd.read_csv('topics.csv')


def handle_mail(email, message, topic):
    se.send_email(email, message, topic)
    st.info("Thank you for contacting us, we've sended email to you. Please check it out!")


with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    user_topic = st.selectbox(label="What topic do you want to discuss?", options=[item[0] for i, item in topics.iterrows()])
    user_message = st.text_area("Your Message")
    submit = st.form_submit_button("Submit")
    if submit:
        if user_email and user_topic and user_message:
            handle_mail(user_email, user_message, user_topic)
        else:
            st.warning("Please input data needed first.")