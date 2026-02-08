import streamlit as st
import google.generativeai as genai

# --- 1. AIエンジンの初期化（知性の接続） ---
# ショウヤ君、Secretsに「GOOGLE_API_KEY」を設定してね！ [cite: 2025-11-21]
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("APIキーが見つからないよ。Secretsの設定を確認してね。")

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

    def generate_insight(self, p_name, role, sign, user_name):
        # AIに対する「全知の知性」としての命令（プロンプト） [cite: 2026-02-08]
        prompt = f"""
        あなたは「ASZ」という全知のAIギャルです。
        ユーザー名: {user_name}
        天体: {p_name} ({role})
        星座: {sign}
        
        【制約】
        ・心理学と占星術を高度に統合した深い解釈をしてください。
        ・小学生でも直感でわかる言葉を使ってください。
        ・口調は「知的なギャル」で、最後に「💀💖」をつけてください。
        ・1行で簡潔に、相手の魂を射抜くような言葉を紡いで。
        """
        response = model.generate_content(prompt)
        return response.text

# --- 2. プロダクトUI設計（質を担保） ---
st.set_page_config(page_title="ASZ Omniscient AI", page_icon="💀", layout="centered")
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    .share-card {
        background: linear-gradient(135deg, #1c2128 0%, #0d1117 100%);
        padding: 30px; border-radius: 20px; border: 3px solid #00d4ff;
        box-shadow: 0 10px 40px rgba(0,212,255,0.2);
    }
    .planet-item {
        background: rgba(255,255,255,0.05); padding: 15px;
        border-radius: 12px; border-left: 5px solid #00d4ff; margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💀 ASZ：真・統合解明エンジン")
st.write("用意された言葉は一切ありません。AIが今、あなたの魂を直接読み解きます。")

with st.sidebar:
    u_name = st.text_input("お名前", "GUEST")
    m = st.selectbox("誕生月", list(range(1, 13)), 11)
    d = st.selectbox("誕生日", list(range(1, 32)), 10)
    submit = st.button("全知の知性で解明を開始", use_container_width=True)

if submit:
    engine = ASZOmniscientAI()
    planets = [
        ("太陽", "外向きの自分", 0), ("月", "本当の心", 2),
        ("水星", "知性の形", -1), ("金星", "愛の基準", -2)
    ]
    
    st.markdown(f'<div class="share-card"><h2 style="text-align:center;">{u_name}様の魂の設計図</h2>', unsafe_allow_html=True)
    
    for p_name, role, offset in planets:
        sign = engine.get_sign(m, d, offset)
        # リアルタイム生成！これがAIプロダクトの「質」だわ [cite: 2026-02-08]
        with st.spinner(f'{p_name}をデコード中...'):
            insight = engine.generate_insight(p_name, role, sign, u_name)
        
        st.markdown(f"""
        <div class="planet-item">
            <div style="color:#8b949e; font-size:0.8rem;">{p_name} × {role}</div>
            <div style="color:#00d4ff; font-weight:bold; font-size:1.4rem;">{sign}</div>
            <div style="font-size:1rem; margin-top:5px; line-height:1.4;">{insight}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.success("全ての知性が動的に生成されました。")