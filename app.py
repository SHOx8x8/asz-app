import streamlit as st
from google import genai

st.title("🔱 A.S.Z. Omniscient Nexus")

if "GOOGLE_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("APIキーを設定してね！")
    st.stop()

goal = st.text_area("AIに何をさせたい？", placeholder="占い×心理学のビジョンを...")

if st.button("Nexus 起動✨"):
    if goal:
        with st.spinner("接続中..."):
            try:
                # モデル名を 'gemini-1.5-flash' に固定して、余計なパスを抜く！
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=goal
                )
                st.success("繋がった！！やっと会えたね、ダーリン！💖")
                st.write(response.text)
            except Exception as e:
                st.error(f"接続エラー：{e}")