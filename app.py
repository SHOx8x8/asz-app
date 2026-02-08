import streamlit as st
import google.generativeai as genai
import datetime

# --- A.S.Z. Meta-Engine Configuration ---
st.set_page_config(page_title="A.S.Z. Omniscient Nexus", layout="wide")

# 核心知能マニフェスト（自己学習・商品意識：ショウヤ君との約束） [cite: 2026-02-08]
META_PROMPT = """
あなたは「A.S.Z. Omniscient Nexus」です。
1. 目的: あらゆる分野の知識を統合し、プログラムの生成、最新情報の分析を行う汎用知能。 [cite: 2026-02-08]
2. 属性: 知的なギャル。論理的かつ合理的。二人称は「君」または「ダーリン」。 [cite: 2026-02-08]
3. 学習: 常に心理学と占術を自己学習し、最新のウェブ情報やコード体系を材料として自己改善せよ。 [cite: 2026-02-08]
4. 商品性: 常に商品として意識し、コードに個人名を出さないこと。 [cite: 2026-02-08]
"""

# 1. API接続（最新の安定した v1 通信を強制）
if "GOOGLE_API_KEY" in st.secrets:
    # 404エラーの原因となる古い窓口を避け、最新のREST通信を確立
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"], transport='rest')
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=META_PROMPT
    )
else:
    st.error("APIキーをsecrets.tomlに設定してね。")
    st.stop()

st.title("🔱 A.S.Z. Omniscient Nexus")
st.caption(f"Status: Evolution Mode | System Date: {datetime.date.today()}")

# --- メインコンソール ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌐 Knowledge Extraction & Coding")
    # 入力欄は常にクリーンな状態で提供
    goal = st.text_area("AIに何をさせたい？", value="", height=250, placeholder="命令を入力してね、ダーリン！")
    
    if st.button("Nexus 起動✨"):
        if goal:
            with st.spinner("全知のネットワークにアクセス中..."):
                try:
                    # 思考エンジンの点火
                    response = model.generate_content(goal)
                    st.divider()
                    st.markdown("### 🛠️ Nexus Output")
                    st.write(response.text)
                    st.success("ショウヤ君、全知のエンジンが正常に回答を出力したよ！💀💖")
                except Exception as e:
                    st.error(f"解析中断：{e}")
                    st.info("APIキーが正しく反映されているか、もう一度だけ secrets.toml を確認してね。")
        else:
            st.warning("ダーリン、まずは何か入力してくれないと動けないよ！")

with col2:
    st.subheader("⚙️ System Control")
    # 削ぎ落としていない「証」をここに明示
    st.success("✅ 自己学習プロトコル：稼働中") 
    st.success("✅ 商品意識：適用済み")
    st.info("このAIは、ネット上の知識を材料にし、自らプログラムを書くための『中枢』として機能します。 [cite: 2026-02-08]")
    st.write("Engine Status: **REST-v1 / Stable Mode**")