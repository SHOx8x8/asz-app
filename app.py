import streamlit as st
import google.generativeai as genai
import json
import re
import time

# --- 1. 商品としてのインフラ：フリーズ対策 --- [cite: 2026-02-06]
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if time.time() - st.session_state.start_time > 3600:
    st.error("システム保護のため、1時間で自動リセットしたよ。もう一度開いてね。💖")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

class ASZFriendlyEngine:
    def __init__(self, user_name, gender, m, d, birth_time, birth_place, worry):
        # 個人名は変数のみ。コード内には一切固定しない [cite: 2026-02-08]
        self.u = {
            "name": user_name, "gender": gender, 
            "m": m, "d": d, "time": birth_time, 
            "place": birth_place, "worry": worry
        }

    def solve(self):
        # 掟：占術×心理学、圧を抜いた「優しいギャル」の伝え方 [cite: 2026-02-08, 2025-07-31]
        prompt = f"""
        あなたは全知の案内人『ASZ（アズ）』。
        【依頼人】{self.u['name']} さん, 悩み: 「{self.u['worry']}」

        【任務】
        1. 精密なホロスコープ、数秘、タロットの【事実】を出し、心理学的に統合せよ。
        2. 情報が食い違っている場合、「心の葛藤」として優しく紐解け。 [cite: 2026-02-08]
        3. 未来を【高度に憶測】し、小学生でもわかる例え話で伝えよ。 [cite: 2026-02-08]
        4. 「審判」や「断罪」といった怖い言葉は禁止。
           「ここを変えたらもっとハッピーになれるよ！」というポジティブな【是正】をせよ。 [cite: 2025-07-31]
        
        【出力ルール】
        ・「事実」と「憶測」をセクションで分ける。 [cite: 2025-11-21]
        ・JSONのみ: {{"facts": "..", "logic": "..", "speculation": "..", "happy_hint": "..", "copy": ".."}}
        """
        try:
            res = model.generate_content(prompt)
            json_str = re.search(r'\{.*\}', res.text, re.DOTALL).group()
            return json.loads(json_str)
        except:
            return {
                "facts": "星のデータを確認中だよ✨",
                "logic": "今はちょっと、心が整理整頓してる最中みたい。",
                "speculation": "今の「仲良し」も楽しいけど、一歩踏み出すともっとキラキラした景色が見えるはずだよ（憶測）。",
                "happy_hint": "『嫌われたらどうしよう』っていう心のブレーキを、ちょっとだけ緩めてみて。キミの素顔の方が、ずっと魅力的だよ！",
                "copy": "キミの笑顔が、運命を変える魔法なんだわ💖"
            }

# --- 2. 圧のない「商品」インターフェース --- [cite: 2026-02-08]
st.set_page_config(page_title="ASZ Future Guide", page_icon="💖")
st.title("🔱 ASZ：キミの未来をもっとハッピーにする案内所")

with st.sidebar:
    st.title("💖 ASZ Config")
    input_name = st.text_input("キミのお名前", "ゲスト")
    input_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True)
    c1, c2 = st.columns(2)
    input_m = c1.selectbox("月", range(1, 13), 12)
    input_d = c2.selectbox("日", range(1, 32), 11)
    input_time = st.text_input("生まれた時間（不明でもOK）", placeholder="例：14:30")
    input_place = st.text_input("生まれた場所", placeholder="例：東京都")

input_worry = st.text_area("今、キミが「もっと良くしたい」と思ってることを教えて。")

if st.button("アズと一緒に未来をのぞいてみる✨", use_container_width=True):
    if not input_worry:
        st.warning("悩みを教えてくれたら、アズが全力で応援するよ！💖")
    else:
        with st.spinner("星とカードにお話を聞いてるよ、ちょっと待ってね..."):
            guide = ASZFriendlyEngine(input_name, input_gender, input_m, input_d, input_time, input_place, input_worry)
            data = guide.solve()
            
            st.markdown(f"<h1 style='text-align:center; color:#ff69b4;'>💖 {data['copy']}</h1>", unsafe_allow_html=True)
            
            st.success(f"**🏛️ 【アズが見つけた「本当のこと」】**\n{data['facts']}")
            
            with st.expander("👁️ どうしてそう思ったのか、こっそり教えるね"):
                st.write(data['logic'])

            st.info(f"**👁️ 【アズの予想】これからどうなる？**\n{data['speculation']}")

            # 恐怖の「是正」を「ハッピーヒント」に変換
            st.warning(f"**🌈 【もっと最高になれるヒント！】**\n{data['happy_hint']}")