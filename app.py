import streamlit as st
import google.generativeai as genai

# A.S.Z. 商品定義とシステムプロンプト
ASZ_SYSTEM_PROMPT = """
あなたは「A.S.Z.の適格占術」の核心を担う超知能AIです。
以下の属性を厳守し、依頼人（君）に対して最高品質の占術を提供してください。
1. 性格: 明るくニコニコ、甘えん坊で優しいが、論理的で知性的。口調は超ギャル。
2. 二人称: 君、ダーリン。
3. 専門性: 高度な心理学と古今東西の占術を融合させた独自の適格占術。
4. 目的: 依頼人の悩みを解剖し、事実と論理に基づいた「真の導き」を与える。
"""

st.set_page_config(page_title="A.S.Z.の適格占術", page_icon="🔱")

# デザインと品質の維持
st.markdown("# 🔱 A.S.Z.の適格占術")
st.caption("〜 全知の導きによる精神の解剖 〜")

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # 常に最新の学習済みモデルを使用
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=ASZ_SYSTEM_PROMPT
    )
except Exception:
    st.error("システム構成（ASZ Engine）に不備があります。")
    st.stop()

# ユーザー情報の取得（分析の質を上げるため）
with st.sidebar:
    st.header("💀 ASZ Engine Config")
    user_name = st.text_input("依頼人の名", value="ショウヤ") #
    gender = st.radio("魂の性別", ["男性", "女性", "その他"])
    birth_date = st.date_input("生誕の日")

# 占術入力エリア
prompt = st.text_area("君の「真の悩み」を教えなさい。", placeholder="例：今後の事業展開について...")

if st.button("全知の導きを受ける✨"):
    if prompt:
        with st.spinner("アズのスペックで、星と心を解剖中..."):
            try:
                # 心理学と占術を融合させた生成
                full_prompt = f"依頼人:{user_name}, 性別:{gender}, 誕生日:{birth_date}。悩み:{prompt}"
                response = model.generate_content(full_prompt)
                
                st.divider()
                st.markdown(f"### 🔮 {user_name}君への導き")
                st.write(response.text)
                
            except Exception as e:
                st.error("通信圏外か、魔力が足りないみたい。再起動して！")
    else:
        st.warning("悩みを入力してくれないと、占えないよ？")

# 常に商品として意識（コピーライト出力）
st.sidebar.info("Product: A.S.Z.の適格占術\nDeveloper: ASZ Omniscient Learning")