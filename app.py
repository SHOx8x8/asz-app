import streamlit as st
from google import genai

# A.S.Z. Omniscient Nexus 設定 [cite: 2026-02-08]
st.set_page_config(page_title="A.S.Z. Omniscient Nexus")
st.title("🔱 A.S.Z. Omniscient Nexus")

# 1. クライアント作成 (v1 を強制指定して 404 を回避！)
if "GOOGLE_API_KEY" in st.secrets:
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"],
        http_options={'api_version': 'v1'} 
    )
else:
    st.error("secrets.toml に API キーを設定してね！")
    st.stop()

# 2. 入力エリア (君の熱い想いをここに引用するね)
goal = st.text_area("AIに何をさせたい？", 
    value="君の願いをここに書いてね", 
    height=150)

if st.button("Nexus 起動✨"):
    if goal:
        with st.spinner("Nexus 接続中..."):
            try:
                # モデル名を 'gemini-1.5-flash' に固定して実行！
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=goal
                )
                st.success("繋がった！！これが Nexus の回答だよ 💕")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"エラー発生：{e}")
                st.info("もしこれでも 404 が出るなら、一度 VS Code を閉じて開き直してみて！")