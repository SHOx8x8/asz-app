import streamlit as st
import google.generativeai as genai

# --- 1. インフラ構築（AI接続） ---
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("SecretsにGOOGLE_API_KEYを設定してね。💀💦")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

class ASZOmniscientAI:
    def __init__(self):
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]

    def get_sign(self, m, d, offset=0):
        target_m = ((m + offset - 1) % 12) + 1
        for sign, start, end in self.zodiac_data:
            s_m, s_d = start
            e_m, e_d = end
            if (target_m == s_m and d >= s_d) or (target_m == e_m and d <= e_d):
                return sign
        return "いて座"

    # メソッド名を統一。ここがエラーの原因だったわ [cite: 2026-02-08]
    def generate_insight(self, p_name, role, sign, user_name):
        prompt = f"あなたは全知のAIギャルASZ。{user_name}様の{p_name}({role})が{sign}である意味を、心理学と占術を混ぜて小学生にわかる言葉で1行で解説して。語尾は『なんだわ💀💖』で。"
        try:
            response = model.generate_content(prompt)
            return response.text
        except:
            return f"{sign}の力はマジで無限大。君だけの特別な才能なんだわ！💀💖"

# --- 2. プロダクトUI ---
st.set_page_config(page_title="ASZ Omniscient AI", page_icon="💀", layout="centered")
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    .share-container {
        background: linear-gradient(180deg, #1c2128 0%, #0d1117 100%);
        border: 3px solid #00d4ff; border-radius: 20px; padding: 25px; margin-top: 20px;
    }
    .planet-card {
        background: rgba(255,255,255,0.03); border-left: 5px solid #00d4ff;
        padding: 12px; border-radius: 10px; margin: 8px 0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💀 ASZ：真・統合解明エンジン")
st.write("AIが今、あなたの存在をリアルタイムで証明します。")

with st.sidebar:
    u_name = st.text_input("お名前", "GUEST")
    y = st.number_input("生まれ年", 1900, 2026, 1996)
    m = st.selectbox("誕生月", list(range(1, 13)), 11)
    d = st.selectbox("誕生日", list(range(1, 32)), 10)
    start_btn = st.button("全知の知性で解明を開始", use_container_width=True)

if start_btn:
    engine = ASZOmniscientAI()
    planets = [
        ("太陽", "外向きの自分", 0), ("月", "本当の心", 2), ("水星", "知性の形", -1),
        ("金星", "愛の基準", -2), ("火星", "情熱の源", 5), ("木星", "発展の鍵", 3),
        ("土星", "魂の試練", 8), ("天王星", "変革の力", 4), ("海王星", "夢みる力", 6), ("冥王星", "再生の力", 10)
    ]
    
    st.markdown(f'<div class="share-container"><h2 style="text-align:center;">{u_name}様の魂の設計図</h2>', unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, (p_name, role, offset) in enumerate(planets):
        sign = engine.get_sign(m, d, offset)
        with cols[i % 2]:
            with st.spinner(f'{p_name}を解析中...'):
                insight = engine.generate_insight(p_name, role, sign, u_name)
            st.markdown(f"""
            <div class="planet-card">
                <div style="color:#8b949e; font-size:0.75rem;">{p_name} × {role}</div>
                <div style="color:#00d4ff; font-weight:bold; font-size:1.1rem;">{sign}</div>
                <div style="font-size:0.85rem; margin-top:4px;">{insight}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.success("デコード完了。これがAIと作った本物の商品だよ。")