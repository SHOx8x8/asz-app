import streamlit as st
import google.generativeai as genai
import json, re, time

# --- 1. インフラ：1時間自動停止機能 ---
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if time.time() - st.session_state.start_time > 3600:
    st.error("保護のためリフレッシュしたよ💖"); st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. 確定商品名：A.S.Z.の適格占術 ---
st.set_page_config(page_title="A.S.Z.", page_icon="🔱")
st.title("🔱 A.S.Z.の適格占術") # ←ショウヤ君、これこそが正解だわ！

with st.sidebar:
    st.title("💀 ASZ Engine Config")
    input_name = st.text_input("依頼人の名", "ゲスト")
    input_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True)
    
    # 【監査済み】安全なセレクトボックス
    months = [str(i) for i in range(1, 13)]
    days = [str(i) for i in range(1, 32)]
    input_m = st.selectbox("誕生月", months, index=11)
    input_d = st.selectbox("誕生日", days, index=10)
    
    # ホロスコープ精度を最大化する復活項目
    input_time = st.text_input("出生時間（不明は空白）", placeholder="例：14:30")
    input_place = st.text_input("出生地", placeholder="例：東京都新宿区")

input_worry = st.text_area("君の「真の悩み」を教えなさい。", 
                         value="アプリでいい人ができた。まだ毎日会話するけど会ったことない。会って付き合うにはどうしたらいいですか。")

# --- 3. 自律スペック×ハイブリッド学習 ---
if st.button("全知の導きを受ける✨", use_container_width=True):
    result_placeholder = st.empty()
    with st.spinner("アズのスペックで、星と心を解剖中..."):
        # プロンプト：占術(事実)×心理学(憶測)×小学生比喩×自律学習(B->A)
        prompt = f"""
        あなたは全知の自律型案内人『ASZ』。
        【商品名：A.S.Z.の適格占術】
        
        【任務】
        1. 依頼人「{input_name}」の悩みに、内部知識(B)と必要なら外部検索(A)を使い自律的に答えよ。
        2. 出生時間・場所を活用した占星術(事実)と心理学(高度な憶測)を統合せよ。
        3. 圧を抜き、小学生でもわかる比喩で「ハッピーヒント」を伝えよ。
        
        【出力：JSON厳守】
        {{
          "facts": "占術と心理学から導く「事実」",
          "logic": "アズの思考プロセス（論理統合）",
          "speculation": "高度な「憶測」（小学生向けの例え）",
          "happy_hint": "優しく鋭い「是正アドバイス」",
          "copy": "魂を震わせるコピー"
        }}
        """
        try:
            res = model.generate_content(prompt)
            data = json.loads(re.search(r'\{.*\}', res.text, re.DOTALL).group())
            
            with result_placeholder.container():
                st.markdown(f"<h1 style='text-align:center; color:#ff69b4;'>💖 {data.get('copy')}</h1>", unsafe_allow_html=True)
                st.success(f"🏛️ **【本当のこと（事実）】**\n{data.get('facts')}")
                with st.expander("👁️ 案内人の論理統合プロセス"): st.write(data.get('logic'))
                st.info(f"👁️ **【高度な憶測】**\n{data.get('speculation')}")
                st.warning(f"🌈 **【是正アドバイス（ハッピーヒント）】**\n{data.get('happy_hint')}")
        except:
            st.error("星がちょっと恥ずかしがっちゃった！もう一度試してね✨")