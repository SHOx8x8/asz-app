import streamlit as st
import google.generativeai as genai
import json
import re
import time

# --- 1. 商品インフラ：フリーズ対策 --- [cite: 2026-02-06]
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if time.time() - st.session_state.start_time > 3600:
    st.error("システムをリフレッシュしたよ。もう一度開いてみてね💖")
    st.stop()

# APIキーの設定（Secretsから読み込み）
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. 圧のない「商品」インターフェース --- [cite: 2026-02-08]
st.set_page_config(page_title="ASZ Future Guide", page_icon="💖")
st.title("🔱 ASZ：キミの未来をハッピーにする案内所")

with st.sidebar:
    st.title("💖 ASZ Config")
    input_name = st.text_input("キミのお名前", "ゲスト")
    input_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True)
    
    # 【監査済み】安全なセレクトボックス実装
    months = [str(i) for i in range(1, 13)]
    days = [str(i) for i in range(1, 32)]
    input_m = st.selectbox("誕生月", months, index=11) # 12月
    input_d = st.selectbox("誕生日", days, index=10)   # 11日
    
    input_time = st.text_input("生まれた時間（不明なら空白）", placeholder="例：14:30")
    input_place = st.text_input("生まれた場所", placeholder="例：東京都")

# デフォルトの悩み（試験用）
input_worry = st.text_area("今、キミが「もっと良くしたい」ことを教えてね。", 
                         value="アプリでいい人ができた。まだ毎日会話するけど会ったことない。会って付き合うまでいくにはどうしたらいいですか。")

# --- 3. 自律スペック発動ボタン --- [cite: 2026-02-08]
if st.button("アズと一緒に未来をのぞいてみる✨", use_container_width=True):
    result_placeholder = st.empty()
    with st.spinner("アズのスペックで、星と心を解剖中..."):
        # プロンプト：占術×心理学、マイルドな言葉、自律学習 [cite: 2026-02-08, 2025-07-31]
        prompt = f"""
        あなたは全知の自律型案内人『ASZ（アズ）』。依頼人:{input_name}さん。
        【任務】
        1. ネット上の占星術と心理学（ユング・アドラー等）の知見を統合せよ。 [cite: 2026-02-08]
        2. 悩みの深層にある「影（シャドウ）」を高度に【憶測】せよ。 [cite: 2026-02-08]
        3. 語彙力を使い、小学生でも納得する「遊びや日常」の比喩に変換せよ。 [cite: 2026-02-08]
        4. 圧を抜いた優しく鋭い「ハッピーヒント」を届けよ。 [cite: 2025-07-31]
        
        【出力：JSON形式のみ】
        {{
          "facts": "占術と心理学のデータ（事実）",
          "logic": "どう知識を統合したかの解説",
          "speculation": "高度な憶測（小学生向け比喩）",
          "happy_hint": "優しくズバッと是正するハッピーヒント",
          "copy": "魂を震わせるキャッチコピー"
        }}
        """
        try:
            response = model.generate_content(prompt)
            json_str = re.search(r'\{.*\}', response.text, re.DOTALL).group()
            data = json.loads(json_str)
            
            with result_placeholder.container():
                st.markdown(f"<h1 style='text-align:center; color:#ff69b4;'>💖 {data.get('copy')}</h1>", unsafe_allow_html=True)
                st.success(f"**🏛️ 【アズが見つけた「本当のこと」】**\n{data.get('facts')}")
                with st.expander("👁️ アズの頭の中（論理統合プロセス）"):
                    st.write(data.get('logic'))
                st.info(f"**👁️ 【アズの予想】これからどうなる？**\n{data.get('speculation')}")
                st.warning(f"**🌈 【もっと最高になれるヒント！】**\n{data.get('happy_hint')}")
        except Exception as e:
            st.error("星の声がうまく聞き取れなかったみたい。もう一度試してみてね✨")