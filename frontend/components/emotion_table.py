import streamlit as st
import pandas as pd

def render_emotion_table(df: pd.DataFrame):
    """감정 분석 결과 테이블"""
    st.subheader("📋 감정 분석 결과")
    st.dataframe(df, use_container_width=True)
