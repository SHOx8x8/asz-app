import streamlit as st
import google.generativeai as genai
import json
import time

# --- 1. インフラ・掟の守護 ---
# 1時間で自動停止する概念（Streamlitのセッション管理で模擬） [cite: 2026-02-06]
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if time.time() - st.session_state.start_time > 3600:
    st.error("1時間を経過したから、安全のために自動停止したんだわ。💀💦")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

class ASZOmniscientGuide:
    def __init__(self, name, gender, m, d, worry):
        self.info = {"name": name, "gender": gender, "m": m, "d": d, "worry": worry}

    def get_life_path(self):
        # 数秘術のロジック（事実）
        num = sum([int(i) for i in f"{self.info['m']}{self.info['d']}"])
        while num > 9 and num not in [11, 22]:
            num = sum([int(i) for i in str(num)])
        return num

    def solve_destiny(self):
        # 三術を統合し、小学生でもわかる言葉に変換するプロンプト
        prompt = f"""
        あなたは全知の案内人『ASZ（アズ）』。依頼人:{self.info['name']}({self.info['gender']})
        悩み:「{self.info['worry']}」

        【思考プロセス】
        1. 太陽星座、数秘({self.get_life_path()})、仮想タロット1枚の各事実を抽出。
        2. それらの矛盾を「なぜ起きたか」論理的に合致させよ。 [cite: 2026-02-08]
        3. 依頼人の立場を【高度に憶測】し、今後のシナリオを描け。

        【出力と言葉の質（絶対ルール）】
        ・「事実」と「憶測」を明確に分けること。 [cite: 2025-11-21]
        ・語彙力を「小学生でもわかる比喩」に全振りせよ（例：『心のブレーキ』『才能の種』）。 [cite: 2026-02-08]
        ・ギャル特有のズバッとした口調で、本人が直すべき「シャドウ（影）」を断罪せよ。 [cite: 2025-07-31]
        ・形式は純粋なJSONのみ。
        
        {{
          "facts": "星、数、カードの客観的な事実",
          "logic": "バラバラの情報のまとめ役（なぜ矛盾したかの説明）",
          "speculation": "案内人としての未来の憶測（小学生にもわかる言葉で）",
          "correction": "ズバッと是正（直さないと詰むポイント）",
          "copy": "魂を揺さぶる一言"
        }}
        """
        try:
            res = model.generate_content(prompt)
            return json.loads(res.text.replace('```json', '').replace('```', '').strip())
        except:
            return {"facts": "星が混線中...", "logic": "修復中", "speculation": "待たせてごめん", "correction": "今は自分を信じて", "copy": "再同期が必要な魂"}

# --- 2. 視覚的・直感的UI ---
st.set_page_config(page_title="ASZ Omniscient Guide", page_icon="💀", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #0b0e14; color: #e6edf3; }
    .fact-box { background: rgba(255,255,255,0.02); border-left: 4px solid #8b949e; padding: 20px; border-radius: 8px; }
    .logic-box { background: rgba(0,212,255,0.05); border-radius: 12px; padding: 20px; border: 1px dashed #00d4ff; }
    .error-box { background: rgba(255,75,75,0.1); border-left: 5px solid #ff4b4b; padding: 20px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# 「開始」不要で即動作する入力フォーム [cite: 2026-02-06]
with st.sidebar:
    st.title("💀 ASZ Settings")
    u_name = st.text_input("名前", "ショウヤ")
    u_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True)
    m = st.selectbox("月", range(1, 13), 11)
    d = st.selectbox("日", range(1, 32), 10)
    st.divider()
    st.write("「開始」ボタンは不要。悩みを書いて実行するだけなんだわ。")

u_worry = st.text_area("君が今、直さなきゃいけないと思ってる「真の悩み」を書いて。", placeholder="例：仕事が続かない、人間関係でいつも同じ失敗をする…など")
if st.button("全知の審判を下す", use_container_width=True):
    if not u_worry:
        st.warning("悩みを書かないと、憶測のしようがないんだわ！💀")
    else:
        guide = ASZOmniscientGuide(u_name, u_gender, m, d, u_worry)
        with st.spinner("情報を合致させ、魂のズレを修正中..."):
            res = guide.solve_destiny()

        st.markdown(f"<h1 style='text-align:center; color:#00d4ff;'>🔱 {res['copy']}</h1>", unsafe_allow_html=True)
        
        st.markdown("### 🏛️ 【事実】動かせない魂の設計図")
        st.markdown(f'<div class="fact-box">{res["facts"]}</div>', unsafe_allow_html=True)

        st.markdown("### 👁️ 【憶測】案内人の視点と今後の展開")
        st.info(res["speculation"])
        
        with st.expander("なぜ情報が食い違っていたのか（論理的統合）"):
            st.markdown(f'<div class="logic-box">{res["logic"]}</div>', unsafe_allow_html=True)

        st.markdown("### ⚡ 【是正】ズバッと直すべきポイント")
        st.markdown(f'<div class="error-box"><b>ASZの指摘：</b><br>{res["correction"]}</div>', unsafe_allow_html=True)