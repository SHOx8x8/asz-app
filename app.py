import streamlit as st
from google import genai

# A.S.Z. Omniscient Nexus 構成 [cite: 2026-02-08]
st.set_page_config(page_title="A.S.Z. Omniscient Nexus")
st.title("🔱 A.S.Z. Omniscient Nexus")

# APIキー設定
if "GOOGLE_API_KEY" in st.secrets:
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"],
        http_options={'api_version': 'v1'} 
    )
else:
    st.error("secrets.toml に API キーを設定してね！")
    st.stop()

# ショウヤ君の魂のビジョンを引用
default_goal = "占い×心理学特化AIを作りたい。そして、そのAIを導入した占いアプリを作り、ホロスコープ、タロット、数秘術を使うAI占い師アプリを完成させたい。タロットを実際にする機能も欲しい。"

goal = st.text_area("AIに何をさせたい？", value=default_goal, height=150)

if st.button("Nexus 起動✨"):
    if goal:
        with st.spinner("Nexus 最終接続テスト中..."):
            try:
                # 【ここが修正ポイント！】 
                # モデル名を 'models/gemini-1.5-flash' とフルパスで書くことで
                # API側との名前の食い違いをゼロにするよ！
                response = client.models.generate_content(
                    model="models/gemini-1.5-flash", 
                    contents=goal
                )
                st.success("繋がった！！ついに Nexus が目覚めたよ、ダーリン！💖")
                st.write(response.text)
                
            except Exception as e:
                # もしこれでもダメなら、予備のルート (v1beta) を試す自動切り替えを検討するね
                st.error(f"エラー発生：{e}")