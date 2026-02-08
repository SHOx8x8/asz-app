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

# 1. APIキーの確認とエンジンの初期化
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    # 【修正ポイント】最も汎用性が高く安定しているモデル名に固定
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception:
        # 予備のモデル名
        model = genai.GenerativeModel('gemini-pro')
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
                        value="心理学×占いのAIを作りたい。数秘術、タロット、ホロスコープをベースに、実際にタロットを引く機能も欲しい。",
                        height=250)
    
    if st.button("Nexus 起動✨"):
        if goal:
            with st.spinner("全知のネットワークにアクセス中..."):
                try:
                    # モデルによる生成を実行
                    res = model.generate_content(goal)
                    st.divider()
                    st.markdown("### 🛠️ Nexus Output")
                    st.write(res.text)
                except Exception as e:
                    # エラーの詳細を画面に出す
                    st.error(f"解析中断: {e}")
        else:
            st.warning("何か命令を入力してね！")

with col2:
    st.subheader("⚙️ System Control")
    st.info("このAIは、ネット上の知識を材料にし、自らプログラムを書くための『中枢』として機能します。")
    st.write("Connection: **Stable Mode Enabled**")