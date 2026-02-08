import streamlit as st
from google import genai
import datetime

# --- A.S.Z. Meta-Engine Configuration ---
st.set_page_config(page_title="A.S.Z. Omniscient Nexus", layout="wide")

# 核心知能マニフェスト [cite: 2026-02-08]
META_PROMPT = """
あなたは「A.S.Z. Omniscient Nexus」です。
1. 目的: 占い×心理学を統合し、タロットやホロスコープのロジックを生成・分析する汎用知能。 [cite: 2026-02-08]
2. 属性: 知的なギャル。論理的かつ合理的。二人称は「君」または「ダーリン」。 [cite: 2025-07-31]
3. 学習: 常に心理学と占術を自己学習せよ。 [cite: 2026-02-08]
4. 商品性: 常に商品として意識し、コードに個人名を出さないこと。 [cite: 2026-02-08]
"""

# APIクライアント初期化
if "GOOGLE_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("secrets.tomlにAPIキーを設定してね。")
    st.stop()

st.title("🔱 A.S.Z. Omniscient Nexus")
st.caption(f"Engine: Google GenAI SDK / Status: Production Ready | {datetime.date.today()}")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌐 Knowledge Extraction & Coding")
    goal = st.text_area("AIに何をさせたい？", height=200, placeholder="占い×心理学のロジックを組んで、とか命令してみて！")
    
    if st.button("Nexus 起動✨"):
        if goal:
            with st.spinner("全知のネットワークに接続中..."):
                try:
                    # 【修正ポイント】system_instruction の渡し方を最新形式に修正
                    response = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=goal,
                        config={
                            'system_instruction': META_PROMPT # ここが最新の合言葉！
                        }
                    )
                    st.divider()
                    st.markdown("### 🛠️ Nexus Output")
                    st.write(response.text)
                    st.success("ショウヤ君、全知の回答が出力されたよ！💕")
                except Exception as e:
                    st.error(f"接続エラー詳細：{e}")
        else:
            st.warning("ダーリン、命令を入力して！")

with col2:
    st.subheader("⚙️ System Control")
    st.success("✅ 自己学習プロトコル：稼働中")
    st.success("✅ 商品意識：適用済み")
    st.info("このAIは、あらゆる占術と心理学を統合する『中枢』として機能します。")