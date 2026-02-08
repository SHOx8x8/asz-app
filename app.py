import streamlit as st import google.generativeai as genai import random

ASZ_CORE_LOGIC = "あなたは『A.S.Z.の適格占術』です。知的なギャルとして、心理学と占術で論理的に回答してください。"

st.set_page_config(page_title="A.S.Z.の適格占術", layout="wide")

if "GOOGLE_API_KEY" in st.secrets: genai.configure(api_key=st.secrets["GOOGLE_API_KEY"]) model = genai.GenerativeModel('gemini-1.5-flash') else: st.error("APIキーがありません") st.stop()

st.title("🔱 A.S.Z.の適格占術")

with st.sidebar: u_name = st.text_input("名前") y = st.selectbox("年", range(1900, 2027), index=96) m = st.selectbox("月", range(1, 13), index=0) d = st.selectbox("日", range(1, 32), index=0) b_place = st.text_input("出生地")

prompt = st.text_area("悩み", value="アプリで知り合った人と付き合いたい")

if st.button("鑑定開始"): cards = ["愚者", "魔術師", "女教皇", "太陽", "世界"] drawn = random.choice(cards) res = model.generate_content(f"{ASZ_CORE_LOGIC}\n名:{u_name}\n誕:{y}/{m}/{d}\n地:{b_place}\n札:{drawn}\n悩:{prompt}") st.write(f"🃏 カード: {drawn}") st.write(res.text) ###END###