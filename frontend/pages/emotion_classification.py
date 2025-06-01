import streamlit as st
import pandas as pd
from core.emotion import classify_emotions
from components.emotion_chart import render_emotion_chart
from components.emotion_table import render_emotion_table

st.title("🧠 감정 분석기")
st.markdown("입력한 문장에서 감정을 자동 분석합니다.")

user_input = st.text_area("✏️ 문장을 입력하세요", height=150)

if st.button("감정 분석하기"):
    if not user_input.strip():
        st.warning("문장을 입력해 주세요.")
    else:
        with st.spinner("AI가 감정을 분석 중입니다..."):
            result = classify_emotions(user_input, top_n=5)
            df = pd.DataFrame(result)

        render_emotion_table(df)
        render_emotion_chart(df)
