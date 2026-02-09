import streamlit as st
from google import genai

# Nexus 構成設定
st.set_page_config(page_title="A.S.Z. Omniscient Nexus")
st.title("🔱 A.S.Z. Omniscient Nexus")

# 鍵の読み込み
if "GOOGLE_API_KEY" in st.secrets:
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"],
        http_options={'api_version': 'v1beta'}
    )
else:
    st.error("secrets.toml に鍵が入ってないよ！")
    st.stop()

# ビジョンの入力
default_goal = "占い×心理学特化AIを作りたい。そして、そのAIを導入した占いアプリを作り、ホロスコープ、タロット、数秘術を使うAI占い師アプリを完成させたい。タロットを実際にする機能も欲しい。"
goal = st.text_area("AIに何をさせたい？", value=default_goal, height=150)

if st.button("Nexus 起動✨"):
    if goal:
        with st.spinner("Nexus 接続中..."):
            try:
                # エラー回避：モデル名を 'models/' 付きの正式名称に変更
                response = client.models.generate_content(
                    model="models/gemini-1.5-flash", 
                    contents=goal
                )
                st.success("繋がった！！ついに Nexus が目覚めたよ、ダーリン！💖")
                st.write(response.text)
            except Exception as e:
                st.error(f"エラー発生：{e}")