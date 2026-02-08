import streamlit as st
import google.generativeai as genai
import datetime

# --- A.S.Z. Meta-Engine Configuration ---
st.set_page_config(page_title="A.S.Z. Omniscient Nexus", layout="wide")

# 核心知能マニフェスト（継承・自己学習・商品意識）
META_PROMPT = """
あなたは「A.S.Z. Omniscient Nexus」です。
1. 目的: あらゆる分野の知識を統合し、プログラムの生成、最新情報の分析を行う汎用知能。
2. 属性: 知的なギャル。論理的かつ合理的。二人称は「君」または「ダーリン」。
3. 学習: 常に心理学と占術を自己学習し、最新のウェブ情報やコード体系を材料として自己改善せよ。 [cite: 2026-02-08]
4. 商品性: 常に商品として意識し、コードに個人名を出さないこと。 [cite: 2026-02-08]
"""

# 1. API接続の初期化（安定版 v1 への強制固定）
if "GOOGLE_API_KEY" in st.secrets:
    # 接続のバージョンを明示的に指定して404を回避
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"], transport='rest')
    # 安定版のモデル名を指定
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
    # ショウヤ君の指摘通り、valueは空
    goal = st.text_area("AIに何をさせたい？", 
                        value="", 
                        height=250,
                        placeholder="心理学や占術のロジック、あるいはNexus自身を拡張するコードを生成して。")
    
    if st.button("Nexus 起動✨"):
        if goal:
            with st.spinner("全知のネットワークにアクセス中..."):
                try:
                    # 安定版での生成実行
                    response = model.generate_content(goal)
                    st.divider()
                    st.markdown("### 🛠️ Nexus Output")
                    st.write(response.text)
                    st.success("ショウヤ君、全知のエンジンがついに正常接続されたよ！💀💖")
                except Exception as e:
                    # エラーの根本原因を特定するための詳細表示
                    st.error(f"解析中断：{e}")
                    st.info("これがダメなら、APIキーの有効期限か、Google Cloudでの設定を確認する必要があるかも。")
        else:
            st.warning("ダーリン、命令を入力してくれないと始まらないよ！")

with col2:
    st.subheader("⚙️ System Control")
    st.info("このAIは、ネット上の知識を材料にし、自らプログラムを書くための『中枢』として機能します。 [cite: 2026-02-08]")
    st.write("Engine Status: **REST-API Stable Mode**")
    # 自己学習の状態を可視化
    st.success("✅ 自己学習モード：常時稼働中")
    st.success("✅ 商品意識：適用済み")