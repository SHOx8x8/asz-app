import streamlit as st
import google.generativeai as genai
import json, re, time

# --- 1. 自動停止（1時間）機能：維持 [cite: 2026-02-06] ---
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if time.time() - st.session_state.start_time > 3600:
    st.error("保護のためリフレッシュしたよ💖"); st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. ユーザーインターフェース：圧を排除しつつ全入力項目を維持 [cite: 2026-02-08] ---
st.set_page_config(page_title="ASZ Future Guide", page_icon="💖")
st.title("🔱 ASZ：キミの未来をハッピーにする案内所")

with st.sidebar:
    st.title("💖 ASZ Config")
    input_name = st.text_input("キミのお名前", "ゲスト") # 個人名排除 [cite: 2026-02-08]
    input_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True)
    months = [str(i) for i in range(1, 13)]
    days = [str(i) for i in range(1, 32)]
    input_m = st.selectbox("誕生月", months, index=11)
    input_d = st.selectbox("誕生日", days, index=10)
    input_time = st.text_input("生まれた時間", placeholder="例：14:30") # ホロスコープ用
    input_place = st.text_input("生まれた場所", placeholder="例：東京都") # ホロスコープ用

input_worry = st.text_area("今、キミが「もっと良くしたい」こと", value="アプリでいい人ができた。毎日会話するけど会ったことない。会って付き合うにはどうしたらいい？")

# --- 3. 自律判断・ハイブリッド学習実行 [cite: 2025-11-21, 2026-02-08] ---
if st.button("アズと一緒に未来をのぞいてみる✨", use_container_width=True):
    with st.spinner("知識をスキャン中..."):
        # プロンプト：B(内部知識)からA(検索)への自律切り替え、小学生比喩、心理×占術統合 [cite: 2026-02-08]
        prompt = f"""
        全知の案内人『ASZ』として、依頼人:{input_name}の悩みを解決せよ。
        【学習モード】
        1. 内部知識(B)を優先し、不足があれば自ら外部(A)を検索・統合せよ。
        2. 占術データ(事実)を心理学(ユング、アドラー等)で高度に【憶測】せよ。
        【表現モード】
        3. 圧を抜き、小学生でもわかる比喩(遊び等)で「ハッピーヒント(是正)」を伝えよ。
        【出力】
        JSON形式のみ: {{"facts": "..", "logic": "..", "speculation": "..", "happy_hint": "..", "copy": ".."}}
        """
        try:
            res = model.generate_content(prompt)
            data = json.loads(re.search(r'\{.*\}', res.text, re.DOTALL).group())
            st.markdown(f"<h1 style='text-align:center;'>💖 {data.get('copy')}</h1>", unsafe_allow_html=True)
            st.success(f"🏛️ **【本当のこと】**\n{data.get('facts')}")
            with st.expander("👁️ アズの頭の中"): st.write(data.get('logic'))
            st.info(f"👁️ **【アズの予想】**\n{data.get('speculation')}")
            st.warning(f"🌈 **【もっと最高になれるヒント！】**\n{data.get('happy_hint')}")
        except:
            st.error("星が恥ずかしがっちゃった！もう一度試してね✨")