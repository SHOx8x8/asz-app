import streamlit as st

class ASZOmniscientEngine:
    def __init__(self):
        # 正確な星座境界データ（100%の質を担保） [cite: 2025-11-21]
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]
        # 心理学×占術の独自統合（小学生指標） [cite: 2026-02-08]
        self.insights = {
            "いて座": "広い世界を冒険する『ヒーロー』。新しい発見が君を元気にするよ！",
            "さそり座": "秘密を見抜く『名探偵』。一つのことを深く見つめる力が凄まじいんだわ。",
            "おとめ座": "みんなを助ける『魔法使い』。バラバラなものを綺麗に整える天才だよ。",
            "やぎ座": "山を登りきる『努力家』。最後まで諦めない強い心を持っているよ。",
            "みずがめ座": "未来を作る『発明家』。当たり前にとらわれない自由なアイデアだね。"
        }

    def get_accurate_sign(self, m, d):
        for sign, start, end in self.zodiac_data:
            s_m, s_d = start
            e_m, e_d = end
            if (m == s_m and d >= s_d) or (m == e_m and d <= e_d):
                return sign
        return "いて座"

# --- UI設定（視認性重視） ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffffff; }
    .card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border: 2px solid #00d4ff; margin-bottom: 20px;
    }
    .sign-name { color: #00d4ff; font-weight: bold; font-size: 2rem; margin: 10px 0; }
    .insight-text { color: #ffffff; font-size: 1.1rem; line-height: 1.6; } /* 文字色を純白にして視認性UP */
    </style>
""", unsafe_allow_html=True)

st.title("ASZの適格占術")
st.write("心理学と占星術をアズが独自に統合。君の『心の設計図』を読み解くよ。")

with st.sidebar:
    st.header("🧬 入力設定")
    m = st.selectbox("月", list(range(1, 13)), 11)
    d = st.selectbox("日", list(range(1, 32)), 11)
    submit = st.button("深層心理を読み解く", use_container_width=True)

if submit:
    engine = ASZOmniscientEngine()
    sign = engine.get_accurate_sign(m, d)
    
    st.markdown(f"""
    <div class="card">
        <div style="color: #a5adba;">太陽 × 外向きの自分</div>
        <div class="sign-name">{sign}</div>
        <div class="insight-text">{engine.insights.get(sign, "特別な才能が眠っているよ。")}</div>
    </div>
    """, unsafe_allow_html=True)
    st.success("調べ学習が終わったよ！これが君の『ヒミツの組み合わせ』なんだわ！💀💖")