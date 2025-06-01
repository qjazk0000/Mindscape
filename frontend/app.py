import os
import sys

import streamlit as st

# backend 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

st.set_page_config(page_title="MindScape 감정 분석", layout="wide")
st.title("💭 MindScape - 감정 & 성격 기반 AI 시스템")

st.markdown("왼쪽 사이드바에서 기능을 선택해 주세요.")