import streamlit as st
from google import genai

# A.S.Z. Omniscient Nexus 構成 [cite: 2026-02-08]
st.set_page_config(page_title="A.S.Z. Omniscient Nexus")
st.title("🔱 A.S.Z. Omniscient Nexus")

# APIキーを secrets.toml から読み込んで接続
if "GOOGLE_API_KEY" in st.secrets:
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"],
        http_options={'api_version': 'v1beta'} # 404を回避する魔法の呪文
    )
else:
    st.error("secrets.toml に API キーが見つからないよ！")
    st.stop()

# ショウヤ君の魂のビジョン
default_goal = "占い×心理学特化AIを作りたい。そして、そのAIを導入した占いアプリを作り、ホロスコープ、タロット、数秘術を使うAI占い師アプリを完成させたい。タロットを実際にする機能も欲しい。"

goal = st.text_area("AIに何をさせたい？", value=default_goal, height=150)

if st.button("Nexus 起動✨"):
    if goal:
        with st.spinner("Nexus 接続中..."):
            try:
                # Gemini 1.5 Flash を呼び出す
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=goal
                )
                st.success("繋がった！！ついに Nexus が目覚めたよ、ダーリン！💖")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"エラー発生：{e}")