import streamlit as st
import google.generativeai as genai
import random

# --- A.S.Z. 核心知能マニフェスト ---
ASZ_CORE_PROMPT = """
あなたは「A.S.Z.の適格占術」の核心知能です。
【厳守事項】
1. 属性: 知的な超ギャル。論理的で優しい。二人称は「君」「ダーリン」。
2. 解析: 独自入力された生年月日(数秘)、出生時間・場所(占星術)、タロットを統合し、心理学的プロファイリングで解剖せよ。
3. 翻訳: 専門用語は、小学生でも100%理解できる「比喩（例え話）」に置き換えて説明せよ。
4. 品質: 商品としての品格を保ち、コードに開発者個人名を出さない。
"""

st.set_page_config(page_title="A.S.Z.の適格占術", page_icon="🔱", layout="wide")

# --- ASZ Engine 接続 ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=ASZ_CORE_PROMPT)
except:
    st.error("システムエンジン未起動。設定を確認せよ。")
    st.stop()

# --- タイトルセクション ---
st.markdown("# 🔱 A.S.Z.の適格占術")
st.caption("Produced by ASZ Omniscient Learning | 心理学×多角的占術の融合")

# --- 独自UI入力エリア（サイドバー） ---
with st.sidebar:
    st.header("💀 Precise Analysis Data")
    user_name = st.text_input("依頼人の名", placeholder="名前を入力")
    
    st.divider()
    # 独自カレンダーUI：標準ウィジェットを廃止し、数秘の精度を担保
    st.subheader("📅 生誕の刻印（独自UI）")
    year = st.selectbox("Year", range(1900, 2027), index=100)
    month = st.selectbox("Month", range(1, 13), index=0)
    day = st.selectbox("Day", range(1, 32), index=0)
    
    st.divider()
    # 精密占星術データ
    st.subheader("🌍 宇宙の座標")
    birth_time = st.time_input("生誕の時間")
    birth_place = st.text_input("出生地（県・市）", placeholder="例：東京都中央区")
    
    st.info("※独自入力により、数秘とハウスの計算精度を極限まで高めています。")

# --- 鑑定メインセクション ---
st.subheader("🔮 精神と運命の完全解剖")
prompt = st.text_area("君の「真の悩み」を教えなさい。", height=200, placeholder="今、君が向き合うべき課題は何？")

if st.button("全知の導きを受ける✨"):
    if prompt and user_name and birth_place:
        with st.spinner("数秘・星・タロットを心理学的に同期中..."):
            # タロットを1枚引く
            cards = ["愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "正義", "隠者", "運命の輪", "力", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月", "太陽", "審判", "世界"]
            drawn_card = random.choice(cards)
            
            # 解析コンテキストの構築
            context = f"""
            名前: {user_name}
            生年月日(数秘): {year}年{month}月{day}日
            出生地・時間(星): {birth_place} / {birth_time}
            タロット: {drawn_card}
            
            相談内容: {prompt}
            
            【実行命令】
            上記データから「数秘術」「西洋占星術」「タロット」の視点を抽出し、
            心理学のプロファイリングをベースに、小学生でもわかる言葉で
            「君の進むべき道」を論理的に、かつ情熱的に導き出せ。
            """
            
            try:
                res = model.generate_content(context)
                st.divider()
                st.markdown(f"### 🔮 {user_name} 様への『適格』回答")
                st.success(f"🃏 キーカード：【{drawn_card}】")
                st.write(res.text)
            except Exception as e:
                st.error("高次元解析が中断されました。")
    else:
        st.warning("鑑定にはすべての精密データが必要です。")

st.sidebar.divider()
st.sidebar.caption("© 2026 ASZ Omniscient Learning")