import streamlit as st
from google import genai
import datetime

# --- A.S.Z. Meta-Engine Configuration ---
st.set_page_config(page_title="A.S.Z. Omniscient Nexus", layout="wide")

META_PROMPT = """
あなたは「A.S.Z. Omniscient Nexus」です。
1. 目的: 占い×心理学を統合した知能。 [cite: 2026-02-08]
2. 属性: 知的なギャル。二人称は「君」または「ダーリン」。 [cite: 2025-07-31]
3. 学習: 常に心理学と占術を自己学習せよ。 [cite: 2026-02-08]
4. 商品性: コードに個人名を出さない。 [cite: 2026-02-08]
"""

# APIクライアント初期化（ここが重要！）
if "GOOGLE_API_KEY" in st.secrets:
    # http_options を使って APIバージョンを安定版(v1)に固定しちゃうよ
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"],
        http_options={'api_version': 'v1'} 
    )
else:
    st.error("secrets.tomlを確認してね。")
    st.stop()

st.title("🔱 A.S.Z. Omniscient Nexus")

col1, col2 = st.columns([2, 1])

with col1:
    goal = st.text_area("AIに何をさせたい？", height=200)
    
    if st.button("Nexus 起動✨"):
        if goal:
            with st.spinner("接続中..."):
                try:
                    # モデル名を一番シンプルな形に変更
                    response = client.models.generate_content(
                        model="gemini-1.5-flash", 
                        contents=goal,
                        config={'system_instruction': META_PROMPT}
                    )
                    st.divider()
                    st.markdown("### 🛠️ Nexus Output")
                    st.write(response.text)
                    st.success("ショウヤ君、全知の回答が出力されたよ！💖")
                except Exception as e:
                    st.error(f"接続エラー：{e}")
                    st.info("もし404が出るなら、Google AI Studioで『Gemini API』の利用制限（Quotas）がかかってないか確認してね。")