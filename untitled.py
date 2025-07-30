import streamlit as st
import joblib

vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

st.title("Fake News Detector")
st.write("Enter a news article below to check whether it is fake or real")

news_input = st.text_area("News article:","")

if st.button("Check News"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        pred = model.predict(transform_input)
        if pred[0]==1:
            st.success("The news is real!!")
        else:
            st.error("The news is Fake!")
    else:
        st.warning("Please Enter some text to analyze")
