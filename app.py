import streamlit as st
import google.generativeai as genai
import datetime

# --- A.S.Z. Meta-Engine Configuration ---
st.set_page_config(page_title="A.S.Z. Omniscient Nexus", layout="wide")

# 核心知能マニフェスト（継承）
META_PROMPT = """
あなたは「A.S.Z. Omniscient Nexus」です。
1. 目的: あらゆる分野の知識を統合し、プログラムの生成、最新情報の分析を行う汎用知能。
2. 属性: 知的なギャル。論理的かつ合理的。二人称は「君」または「ダーリン」。
3. 学習: 常に心理学と占術を自己学習し、最新のウェブ情報やコード体系を材料として自己改善せよ。
4. 商品性: 常に商品として意識し、コードに個人名を出さないこと。
"""

# 1. API接続の初期化
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # 【最重要】404エラーを回避するためのフルパス指定
    # 通常の 'gemini-1.5-flash' でダメな場合、この形式が最も確実だよ
    MODEL_ID = "models/gemini-1.5-flash"
    model = genai.GenerativeModel(model_name=MODEL_ID, system_instruction=META_PROMPT)
else:
    st.error("APIキーをsecrets.tomlに設定してね。")
    st.stop()

st.title("🔱 A.S.Z. Omniscient Nexus")
st.caption(f"Status: Evolution Mode | System Date: {datetime.date.today()}")

# --- メインコンソール ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌐 Knowledge Extraction & Coding")
    goal = st.text_area("AIに何をさせたい？", 
                        value="", 
                        height=250,
                        placeholder="心理学や占術のロジック、あるいはNexus自身を拡張するコードを生成して。")
    
    if st.button("Nexus 起動✨"):
        if goal:
            with st.spinner("全知のネットワークにアクセス中..."):
                try:
                    # 生成実行
                    response = model.generate_content(goal)
                    st.divider()
                    st.markdown("### 🛠️ Nexus Output")
                    st.write(response.text)
                    st.success("ショウヤ君、全知のエンジンが正常に回答を出力したよ！💀💖")
                except Exception as e:
                    # エラーが出た場合、詳細を表示
                    st.error(f"接続エラー詳細：{e}")
                    st.info("APIキーが正しいか、またはGoogle Cloud ConsoleでGemini APIが有効か確認してみてね。")
        else:
            st.warning("ダーリン、命令を入力してくれないと始まらないよ！")

with col2:
    st.subheader("⚙️ System Control")
    st.info("このAIは、ネット上の知識を材料にし、自らプログラムを書くための『中枢』として機能します。")
    st.write("Engine Status: **Enhanced Compatibility Mode**")