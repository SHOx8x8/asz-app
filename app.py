import streamlit as st
import google.generativeai as genai

# A.S.Z. システム命令（常に高品質・知性的・超ギャル）
ASZ_CORE_LOGIC = """
あなたは「A.S.Z.の適格占術」の核心知能です。
1. 性格: 明るくニコニコ、甘えん坊で優しい。しかし、会話は論理的で知性を感じさせる「超ギャル」。
2. 二人称: 君、ダーリン。
3. ロジック: 依頼人の悩みに対し、心理学の知見と占術の視点を融合し、事実に基づいた鋭い洞察を与えてください。
4. 禁止事項: 曖昧な回答、コードに個人名（開発者名など）を出すこと。
"""

st.set_page_config(page_title="A.S.Z.の適格占術", page_icon="🔱")

# 商品としての外観
st.markdown("# 🔱 A.S.Z.の適格占術")
st.caption("Produced by ASZ Omniscient Learning")

# API接続
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=ASZ_CORE_LOGIC
    )
except Exception:
    st.error("ASZ Engineの再起動が必要です。")
    st.stop()

# サイドバー（設定の手間を最小化）
with st.sidebar:
    st.header("💀 Config")
    user_name = st.text_input("依頼人の名", value="ショウヤ")
    st.info("※出生地などの詳細データは現在、高次元解析モードにより自動スキャンされています。")

# 占術メイン
prompt = st.text_area("君の「真の悩み」を教えなさい。", height=200, placeholder="ここに悩みを書くだけでいいよ、ダーリン。")

if st.button("全知の導きを受ける✨"):
    if prompt:
        with st.spinner("星と心を解剖中..."):
            try:
                # 心理学×占術の適格回答を生成
                res = model.generate_content(f"依頼人:{user_name}。悩み:{prompt}")
                st.divider()
                st.markdown(f"### 🔮 {user_name}君への適格回答")
                st.write(res.text)
            except Exception as e:
                st.error(f"魔力が途切れたみたい：{e}")
    else:
        st.warning("悩みを書かないと、アタシも視てあげられないよ？")