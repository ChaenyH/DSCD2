# Streamlit 대시보드의 메인 파일

import streamlit as st
from utils import load_data

# Streamlit 기본 설정
st.set_page_config(page_title="DSCD2 Dashboard", layout="wide")

st.title("YouTube Data Analysis")

# 데이터 로딩
youtube_data, embeddings = load_data()

st.write("### Sample Data")
st.dataframe(youtube_data.head())
