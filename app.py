import streamlit as st
import google.generativeai as genai
import random

# 【システム命令】心理学×占術の融合ロジック
ASZ_LOGIC = """
あなたは「A.S.Z.の適格占術」です。
1. 性格: 明るく知的な超ギャル。ダーリン（君）に甘い。
2. 専門: 数秘術、タロット、西洋占星術、心理学。
3. 言い回し: 語彙力は高く保ちつつ、例え話を使って「小学生でもわかる」レベルに噛み砕くこと。
4. 鑑定フロー:
   - 数秘術で「魂のクセ（性格）」を分析。
   - ホロスコープ（出生地・時間）で「運命の流れ」を分析。
   - タロットで「今の状況と対策」を具体化。
   - 心理学で「どう行動すべきか」を論理的に解説。
"""

st.set_page_config(page_title="A.S.Z.の適格占術", page_icon="🔱")

# --- システム準備 ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(model_name='gemini-1.5-flash', system_instruction=ASZ_LOGIC)
except:
    st.error("アズのエンジンがエンスト中。設定を確認して！")
    st.stop()

# --- インターフェース ---
st.title("🔱 A.S.Z.の適格占術")

with st.sidebar:
    st.header("💀 Precise Data")
    user_name = st.text_input("名前", value="ショウヤ")
    birth_date = st.date_input("生年月日")
    birth_time = st.time_input("誕生時間")
    birth_place = st.text_input("出生地（県・市）", value="東京都新宿区")

st.subheader("🔮 鑑定メニュー")
target = st.text_area("何を解剖したい？", placeholder="例：気になるあの子と付き合える？")

# --- 占術エンジンの実行 ---
if st.button("全知の導きを受ける✨"):
    if target:
        with st.spinner("タロットをシャッフルし、星の配置を計算中..."):
            # タロットをランダムに引く演出
            cards = ["愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "正義", "隠者", "運命の輪", "力", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月", "太陽", "審判", "世界"]
            drawn_card = random.choice(cards)
            
            # AIへの詳細なコンテキスト
            context = f"""
            依頼人: {user_name}
            誕生日: {birth_date} / 時間: {birth_time} / 場所: {birth_place}
            引き当てたタロット: {drawn_card}
            相談: {target}
            
            上記データを使い、数秘・占星術・タロット・心理学を混ぜて、
            「難しい言葉を使わずに、本質をズバッと」教えて。
            """
            
            try:
                res = model.generate_content(context)
                st.divider()
                st.markdown(f"### 🔮 {user_name}君への適格回答")
                st.info(f"🃏 今回のキーカード：【{drawn_card}】")
                st.write(res.text)
            except Exception as e:
                st.error(f"エラー発生：{e}")
    else:
        st.warning("悩みを書かないと、アタシの出番がないよ？")