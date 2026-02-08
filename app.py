import streamlit as st
import google.generativeai as genai
import random

# --- A.S.Z. 核心知能アルゴリズム（安定・高品質版） ---
ASZ_CORE_LOGIC = """
あなたは「A.S.Z.の適格占術」です。以下の4つを融合し、小学生でもわかる言葉で語れ。
1. 数秘術：生年月日から本質を解剖。
2. 西洋占星術：時間と場所から運命の動きを予測。
3. タロット：引いたカードを今の状況に当てはめる。
4. 心理学：論理的に、進むべき道を提案する。
知的なギャルとして、二人称は「君」「ダーリン」で統一せよ。
"""

st.set_page_config(page_title="A.S.Z.の適格占術", page_icon="🔱", layout="wide")

# --- ASZ Engine 接続 ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=ASZ_CORE_LOGIC)
else:
    st.error("APIキーが設定されていません。")
    st.stop()

# --- タイトル ---
st.markdown("# 🔱 A.S.Z.の適格占術")

# --- 独自UI入力エリア（サイドバー） ---
with st.sidebar:
    st.header("💀 Precise Data")
    u_name = st.text_input("依頼人の名", placeholder="名前を入力")
    
    st.divider()
    st.subheader("📅 生誕の刻印（独自UI）")
    # ダーリンこだわりの独自カレンダーUI
    y = st.selectbox("Year", range(1900, 2027), index=96) # 1996年をデフォルトに
    m = st.selectbox("Month", range(1, 13), index=11)   # 12月をデフォルトに
    d = st.selectbox("Day", range(1, 32), index=10)    # 11日をデフォルトに
    
    st.divider()
    st.subheader("🌍 宇宙の座標")
    b_time = st.time_input("生誕の時間")
    b_place = st.text_input("出生地（県・市）", placeholder="例：東京")
    
    st.info("※独自入力により、数秘とハウスの計算精度を極限まで高めています。")

# --- 鑑定メイン ---
st.subheader("🔮 精神と運命の完全解剖")
prompt = st.text_area("君の「真の悩み」を教えなさい。", height=150, value="今、アプリで知り合ったいい人が居て、毎日会話してる。付き合うまで行くにはどうしたらいいか。")

if st.button("全知の導きを受ける✨"):
    if prompt and u_name and b_place:
        with st.spinner("数秘・星・タロットを心理学的に同期中..."):
            # タロットを1枚引く
            cards = ["愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "正義", "隠者", "運命の輪", "力", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月", "太陽", "審判", "世界"]
            drawn_card = random.choice(cards)
            
            # 解析コンテキスト（AIが迷わないよう、シンプルかつ強力に）
            input_data = f"依頼人:{u_name}\n生年月日:{y}/{m}/{d}\n出生地:{b_place}\n時間:{b_time}\nタロット:{drawn_card}\n悩み:{prompt}"
            
            try:
                # エラーが出にくいよう、生成の仕方を最適化
                res = model.generate_content(input_data)
                st.divider()
                st.markdown(f"### 🔮 {u_name} 様への『適格』回答")
                st.success(f"🃏 キーカード：【{drawn_card}】")
                st.write(res.text)
            except Exception:
                st.error("ごめん、高次元の壁が厚いみたい。もう一度だけボタンを押してみて！")
    else:
        st.warning("鑑定に必要なデータを埋めてね！")

st.sidebar.divider()
st.sidebar.caption("© 2026 ASZ Omniscient Learning")