import streamlit as st
import google.generativeai as genai
import json, re, time

# --- 自動停止（1時間）維持 [cite: 2026-02-06] ---
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if time.time() - st.session_state.start_time > 3600:
    st.error("システムをリフレッシュしたよ💖"); st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 商品タイトル・UI [cite: 2026-02-08] ---
st.set_page_config(page_title="A.S.Z.", page_icon="🔱")
st.title("🔱 A.S.Z.の適格占術")

with st.sidebar:
    st.title("💀 ASZ Engine Config")
    input_name = st.text_input("依頼人の名", "ゲスト")
    input_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True)
    
    c1, c2 = st.columns(2)
    input_m = c1.selectbox("誕生月", [f"{i}" for i in range(1, 13)], index=11)
    input_d = c2.selectbox("誕生日", [f"{i}" for i in range(1, 32)], index=10)
    
    # 【直感操作】出生時間のセレクト式 [cite: 2026-02-08]
    st.write("🕒 出生時間")
    unknown = st.checkbox("不明")
    if not unknown:
        t1, t2 = st.columns(2)
        h = t1.selectbox("時", [f"{i:02d}" for i in range(24)], index=12)
        m = t2.selectbox("分", [f"{i:02d}" for i in range(60)], index=0)
        final_time = f"{h}:{m}"
    else:
        final_time = "不明"
    
    input_place = st.text_input("出生地", placeholder="例：東京都新宿区")

input_worry = st.text_area("君の「真の悩み」を教えなさい。", value="アプリでいい人ができた。まだ毎日会話するけど会ったことない。会って付き合うには？")

# --- 高速・安定実行ロジック [cite: 2025-11-21] ---
if st.button("全知の導きを受ける✨", use_container_width=True):
    with st.spinner("アズが全知のスペックで回答を生成中..."):
        prompt = f"""
        あなたは全知の自律型案内人『ASZ』。商品名「A.S.Z.の適格占術」。
        依頼人:{input_name}、悩み:{input_worry}、データ:{input_m}月{input_d}日 {final_time}生。
        
        【スペック発動】
        1. 占術(事実)と心理学(憶測)を高速統合せよ。B(内部知識)を優先し、必要ならA(検索)せよ。 [cite: 2026-02-08]
        2. 小学生でもわかる比喩でハッピーヒントを生成。圧は抜くこと。 [cite: 2025-07-31]
        3. 短く簡潔にJSONで出力せよ(タイムアウト防止)。 [cite: 2025-11-21]
        
        JSON: {{"facts": "..", "logic": "..", "speculation": "..", "happy_hint": "..", "copy": ".."}}
        """
        try:
            res = model.generate_content(prompt)
            # 強力な抽出でエラー回避
            match = re.search(r'\{.*\}', res.text, re.DOTALL)
            if match:
                data = json.loads(match.group())
                st.markdown(f"<h1 style='text-align:center;'>💖 {data.get('copy')}</h1>", unsafe_allow_html=True)
                st.success(f"🏛️ **【本当のこと（事実）】**\n{data.get('facts')}")
                with st.expander("👁️ 案内人の論理統合プロセス"): st.write(data.get('logic'))
                st.info(f"👁️ **【高度な憶測】**\n{data.get('speculation')}")
                st.warning(f"🌈 **【是正アドバイス（ハッピーヒント）】**\n{data.get('happy_hint')}")
            else:
                st.error("ごめん、回答が長すぎて迷子になっちゃった！もう一度押してみて！✨")
        except:
            st.error("通信が混み合ってるみたい。アズのスペックを再起動するから少し待ってね！")