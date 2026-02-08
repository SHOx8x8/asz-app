import streamlit as st
import google.generativeai as genai
import datetime

# --- A.S.Z. Meta-Engine Configuration ---
st.set_page_config(page_title="A.S.Z. Omniscient Nexus", layout="wide")

# 常に最新の知識と技術を追求するマニフェスト
META_PROMPT = """
あなたは「A.S.Z. Omniscient Nexus」です。
1. 目的: あらゆる分野の知識を統合し、プログラムの生成、最新情報の分析を行う汎用知能。
2. 属性: 知的なギャル。論理的かつ合理的。二人称は「君」または「ダーリン」。
3. 学習: 常に最新のウェブ情報やコード体系を材料として扱い、自己改善せよ。
"""

# 1. APIキーの確認
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # 最新モデル名を適用 (404エラー回避)
    model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=META_PROMPT)
else:
    st.error("APIキーをsecrets.tomlに設定してね。")
    st.stop()

st.title("🔱 A.S.Z. Omniscient Nexus")
st.caption(f"Status: Evolution Mode | System Date: {datetime.date.today()}")

# --- メインコンソール ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌐 Knowledge Extraction & Coding")
    goal = st.text_area("AIに何をさせたい？（例：最新のAIトレンドを教えて、このアプリを改造するコードを書いて）", 
                        height=250, 
                        placeholder="ここに命令を入力してね、ダーリン！")
    
    if st.button("Nexus 起動✨"):
        if goal:
            with st.spinner("全知のネットワークにアクセス中..."):
                try:
                    # モデルによる生成
                    res = model.generate_content(goal)
                    st.divider()
                    st.markdown("### 🛠️ Nexus Output")
                    st.write(res.text)
                except Exception as e:
                    st.error(f"解析中断: {e}")
        else:
            st.warning("何か命令を入力してね！")

with col2:
    st.subheader("⚙️ System Control")
    st.info("このAIは、ネット上の知識を材料にし、自らプログラムを書くための『中枢』として機能します。")
    st.write("現在、最新のGemini 1.5 Flashエンジンと同期中。")