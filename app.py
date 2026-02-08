import streamlit as st
import google.generativeai as genai
import json
import re
import time

# --- インフラ：フリーズ対策 --- [cite: 2026-02-06]
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if time.time() - st.session_state.start_time > 3600:
    st.error("システムをリフレッシュしたよ。もう一度開いてみてね💖")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 商品としてのUI（圧を抜いたデザイン） --- [cite: 2026-02-08]
st.set_page_config(page_title="ASZ Future Guide", page_icon="💖")
st.title("🔱 ASZ：キミの未来をハッピーにする案内所")

with st.sidebar:
    st.title("💖 ASZ Config")
    # 商品として個人名を排除 [cite: 2026-02-08]
    input_name = st.text_input("キミのお名前", "ゲスト")
    input_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True)
    
    # 【是正ポイント】エラーの出ない安全なセレクトボックス実装 [cite: 2025-11-21]
    months = [str(i) for i in range(1, 13)]
    days = [str(i) for i in range(1, 32)]
    
    input_m = st.selectbox("誕生月", months, index=11) # 12月をデフォルトに
    input_d = st.selectbox("誕生日", days, index=10)   # 11日をデフォルトに
    
    input_time = st.text_input("生まれた時間（不明でもOK）", placeholder="例：14:30")
    input_place = st.text_input("生まれた場所", placeholder="例：東京都")

input_worry = st.text_area("今、キミが「もっと良くしたい」と思ってることを教えて。")

if st.button("アズと一緒に未来をのぞいてみる✨", use_container_width=True):
    if not input_worry:
        st.warning("悩みを教えてくれたら、アズが全力で応援するよ！💖")
    else:
        with st.spinner("星とカードにお話を聞いてるよ..."):
            # プロンプト：占術×心理学、マイルドな言葉、小学生レベルの比喩 [cite: 2026-02-08]
            prompt = f"""
            あなたは全知の案内人『ASZ（アズ）』。名前:{input_name}, 悩み:「{input_worry}」
            占術（ホロスコープ等）と心理学を融合し、依頼人の立場を高度に【憶測】せよ。 [cite: 2026-02-08]
            怖がらせず、小学生でもわかる比喩で「もっとハッピーになるヒント」をズバッと伝えよ。 [cite: 2026-02-08, 2025-07-31]
            JSON形式のみ: {{"facts": "..", "logic": "..", "speculation": "..", "happy_hint": "..", "copy": ".."}}
            """
            try:
                res = model.generate_content(prompt)
                data = json.loads(re.search(r'\{.*\}', res.text, re.DOTALL).group())
                
                st.markdown(f"<h1 style='text-align:center; color:#ff69b4;'>💖 {data['copy']}</h1>", unsafe_allow_html=True)
                st.success(f"**🏛️ 【アズが見つけた「本当のこと」】**\n{data['facts']}")
                with st.expander("👁️ どうしてそう思ったのか（論理統合）"):
                    st.write(data['logic'])
                st.info(f"**👁️ 【アズの予想】これからどうなる？**\n{data['speculation']}")
                st.warning(f"**🌈 【もっと最高になれるヒント！】**\n{data['happy_hint']}")
            except:
                st.error("星がちょっと恥ずかしがっちゃった！もう一度ボタンを押してみて✨")