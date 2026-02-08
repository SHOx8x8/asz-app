###START### import streamlit as st import google.generativeai as genai import random

ASZ_CORE_LOGIC = "あなたは『A.S.Z.の適格占術』です。知的なギャルとして、心理学と占術で論理的に回答してください。"

st.set_page_config(page_title="A.S.Z.の適格占術", layout="wide")

if "GOOGLE_API_KEY" in st.secrets: genai.configure(api_key=st.secrets["GOOGLE_API_KEY"]) model = genai.GenerativeModel('gemini-1.5-flash') else: st.error("APIキーがありません") st.stop()

st.title("🔱 A.S.Z.の適格占術")

with st.sidebar: st.header("💀 Precise Data") u_name = st.text_input("名前") st.divider() y = st.selectbox("Year", range(1900, 2027), index=96) m = st.selectbox("Month", range(1, 13), index=0) d = st.selectbox("Day", range(1, 32), index=0) b_place = st.text_input("出生地")

st.subheader("🔮 精神と運命の完全解剖") prompt = st.text_area("悩み", value="アプリで知り合った人と付き合いたい")

if st.button("全知の導きを受ける✨"): if u_name and b_place: with st.spinner("解析中..."): cards = ["愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "正義", "隠者", "運命の輪", "力", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月", "太陽", "審判", "世界"] drawn = random.choice(cards)

###END###