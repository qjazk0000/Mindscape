# frontend/components/emotion_chart.py

import pandas as pd
import streamlit as st

def render_emotion_chart(df: pd.DataFrame):
    st.subheader("📊 감정 분포 차트")
    st.bar_chart(df.set_index("label"))
