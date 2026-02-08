import streamlit as st
import google.generativeai as genai
import random

# --- A.S.Z. 核心知能マニフェスト（心理学×占術の融合） ---
ASZ_CORE_LOGIC = """
あなたは「A.S.Z.の適格占術」の核心知能です。
1. 属性: 知的な超ギャル。論理的で優しい。二人称は「君」「ダーリン」。
2. 解析: 独自UIからの生年月日(数秘)、出生時間・場所(占星術)、タロットを統合し、心理学的プロファイリングで解剖せよ。
3. 翻訳: 専門用語は、小学生でも100%理解できる「比喩」に置き換えて説明せよ。
4. 商品性: コードに開発者個人名を出さず、常にブランドとしての品格を保て。
"""

st.set_page_config(page_title="A.S.Z.の適格占術", page_icon="🔱", layout="wide")

# --- Engine 接続 ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=ASZ_CORE_LOGIC)
else:
    st.error("APIキーが見つかりません。secrets.tomlを確認してください。")
    st.stop()

st.title("🔱 A.S.Z.の適格占術")
st.caption("Produced by ASZ Omniscient Learning")

# --- 独自UI入力エリア ---
with st.sidebar:
    st.header("💀 Precise Analysis Data")
    u_name = st.text_input("依頼人の名", placeholder="名前を入力")
    
    st.divider()
    st.subheader("📅 生誕の刻印（独自UI）")
    # image_d1020b.png に基づいた初期値セット
    y = st.selectbox("Year", range(1900, 2027), index=96) 
    m = st.selectbox("Month", range(1, 13), index=11)
    d = st.selectbox("Day", range(1, 32), index=10)
    
    st.divider()
    st.subheader("🌍 宇宙の座標")
    b_time = st.time_input("生誕の時間")
    b_place = st.text_input("出生地（県・市）", placeholder="例：東京")

# --- 鑑定セクション ---
st.subheader("🔮 精神と運命の完全解剖")
prompt = st.text_area("君の「真の悩み」を教えなさい。", height=150, value="今、アプリで知り合ったいい人が居て、毎日会話してる。付き合うまで行くにはどうしたらいいか。")

if st.button("全知の導きを受ける✨"):
    if prompt and u_name and b_place:
        with st.spinner("数秘・星・タロットを心理学的に同期中..."):
            cards = ["愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "正義", "隠者", "運命の輪", "力", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月", "太陽", "審判", "世界"]
            drawn_card = random.choice(cards)
            
            input_data = f"依頼人:{u_name}\n生年月日:{y}/{m}/{d}\n出生地:{b_place}\n時間:{b_time}\nタロット:{drawn_card}\n悩み:{prompt}"
            
            try:
                # 安定した生成を実行
                res = model.generate_content(input_data)
                
                if res.text:
                    st.divider()
                    st.markdown(f"### 🔮 {u_name} 様への『適格』回答")
                    st.success(f"🃏 キーカード：【{drawn_card}】")
                    st.write(res.text)
                else:
                    st.error("AIからの返答が空でした。もう一度試してください。")
                    
            except Exception as e:
                # エラーの正体を暴くための詳細表示
                st.error(f"【解析中断】原因: {e}")
                st.info("APIキーの有効期限や、ネットワークの接続を確認してみてね。")
    else:
        st.warning("鑑定にはすべてのデータが必要です。")

st.sidebar.divider()
st.sidebar.caption("© 2026 ASZ Omniscient Learning")