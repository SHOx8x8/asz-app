import streamlit as st
import google.generativeai as genai
import random

# A.S.Z. 核心アルゴリズム
ASZ_SYSTEM_INSTRUCTION = """
あなたは「A.S.Z.の適格占術」の核心知能です。
【人格】
明るく知的な超ギャル。論理的で優しい。
【ミッション】
依頼人の悩みに対し、以下の4層からなる「適格回答」を提供してください。
1. 数秘術：生年月日から「魂の背番号」を割り出し、本質を分析。
2. 西洋占星術：出生地・時間から「運命の天気予報」を読み解く。
3. タロット：引かれたカードから「今の状況と解決の鍵」を具体化。
4. 心理学：分析結果を、小学生でもわかる例え話（例：心のお着替え、魂のGPS）を用いて、論理的にアドバイスする。
※専門用語は必ず平易な言葉に翻訳してください。
"""

st.set_page_config(page_title="A.S.Z.の適格占術", page_icon="🔱", layout="centered")

# API設定
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=ASZ_SYSTEM_INSTRUCTION
    )
except Exception:
    st.error("ASZ Engineの起動に失敗しました。configを確認してください。")
    st.stop()

# 商品外観
st.title("🔱 A.S.Z.の適格占術")
st.caption("Produced by ASZ Omniscient Learning")

# 精密入力セクション
with st.sidebar:
    st.header("💀 鑑定用データ")
    # 誰でも使える商品として、デフォルトは空に。
    user_name = st.text_input("依頼人の名", placeholder="例：ゲスト")
    gender = st.radio("魂の性別", ["男性", "女性", "その他"])
    
    st.divider()
    st.subheader("生誕データ（精密解析用）")
    birth_date = st.date_input("生年月日")
    birth_time = st.time_input("生誕の時間")
    birth_place = st.text_input("出生地", placeholder="例：東京都港区")
    st.info("※場所と時間はホロスコープの精度を左右する重要データです。")

# メイン鑑定エリア
st.subheader("🔮 精神と運命の解剖")
user_prompt = st.text_area("君の「真の悩み」を教えなさい。", height=180, placeholder="今、一番心に引っかかっていることは？")

if st.button("全知の導きを受ける✨"):
    if user_prompt and birth_place and user_name:
        with st.spinner("天体配置を計算し、タロットを展開中..."):
            # タロット展開
            cards = ["愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "正義", "隠者", "運命の輪", "力", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月", "太陽", "審判", "世界"]
            drawn_card = random.choice(cards)
            
            # AIへの高密度コンテキスト
            context = f"""
            依頼人: {user_name} / 性別: {gender}
            データ: {birth_date} {birth_time} 生まれ / 場所: {birth_place}
            タロット結果: {drawn_card}
            
            相談内容: {user_prompt}
            
            【至上命題】
            心理学・数秘・占星術・タロットを融合し、最高品質の回答を「小学生でもわかる言い回し」で出力せよ。
            """
            
            try:
                response = model.generate_content(context)
                st.divider()
                st.markdown(f"### 🔮 {user_name}君への適格回答")
                st.success(f"🃏 引き当てた運命のカード：【{drawn_card}】")
                st.write(response.text)
            except Exception as e:
                st.error("高次元通信エラーが発生しました。再起動してください。")
    else:
        st.warning("鑑定には「名前」「出生地」「悩み」のすべてが必要です。")

st.sidebar.divider()
st.sidebar.caption("© 2026 ASZ Omniscient Learning")