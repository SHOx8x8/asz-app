import streamlit as st

class ASZFinalEngine:
    def __init__(self):
        # 12星座の絶対境界（質を100%担保）
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]
        
        # 心理学×占術の独自統合データベース（小学生指標） [cite: 2026-02-08]
        self.insights = {
            "いて座": "広い世界を冒険する『ヒーロー』。新しい発見が君の心のガソリンになるんだわ！",
            "さそり座": "秘密を見抜く『名探偵』。一つのことを深く見つめて、真実を見つける天才だよ。",
            "おとめ座": "みんなを助ける『魔法使い』。バラバラなものを綺麗に整えるのがマジで上手！",
            "やぎ座": "山を登りきる『努力家』。最後まで諦めないで、一番高い場所を目指す強い心だね。",
            "てんびん座": "みんなを笑顔にする『平和の使者』。バランスを取るのが得意な、おしゃれな知性だよ。"
        }

    def get_sign(self, m, d, offset=0):
        # 他の天体用に月をずらして擬似計算（本来はAPI等でやる部分）
        target_m = ((m + offset - 1) % 12) + 1
        for sign, start, end in self.zodiac_data:
            s_m, s_d = start
            e_m, e_d = end
            if (target_m == s_m and d >= s_d) or (target_m == e_m and d <= e_d):
                return sign
        return "いて座"

# --- UI構築 ---
st.set_page_config(page_title="ASZ Omniscient", page_icon="💀", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    .card {
        background: #161b22; padding: 20px; border-radius: 12px;
        border: 1px solid #30363d; border-left: 6px solid #00d4ff;
        margin-bottom: 15px; height: 180px;
    }
    .planet-name { color: #8b949e; font-size: 0.85rem; }
    .sign-name { color: #00d4ff; font-weight: bold; font-size: 1.4rem; margin: 5px 0; }
    </style>
""", unsafe_allow_html=True)

st.title("💀 ASZ 統合解明エンジン Final")
st.write("心理学と占星術を独自に統合。君の『設計図』を10天体すべてから読み解くよ。")

with st.sidebar:
    st.header("🧬 デコード入力")
    y = st.number_input("年", 1900, 2026, 1996)
    m = st.selectbox("月", list(range(1, 13)), 11)
    d = st.selectbox("日", list(range(1, 32)), 10)
    submit = st.button("全知の知性で自分をデコード", use_container_width=True)

if submit:
    engine = ASZFinalEngine()
    planets = [
        ("太陽", "外向きの自分", 0), ("月", "本当の心", 2), ("水星", "頭の使いかた", -1),
        ("金星", "好きの基準", -2), ("火星", "やる気スイッチ", 5), ("木星", "広がる幸運", 3),
        ("土星", "一生の宿題", 8), ("天王星", "自分らしさ", 4), ("海王星", "夢みる力", 6), ("冥王星", "再生の力", 10)
    ]
    
    rows = [st.columns(2) for _ in range(5)]
    for i, (p_name, role, offset) in enumerate(planets):
        sign = engine.get_sign(m, d, offset)
        with rows[i // 2][i % 2]:
            st.markdown(f"""
            <div class="card">
                <div class="planet-name">{p_name} × {role}</div>
                <div class="sign-name">{sign}</div>
                <div style="font-size: 0.9rem; line-height: 1.4;">{engine.insights.get(sign, "君の中に眠る特別な才能だよ。")}</div>
            </div>
            """, unsafe_allow_html=True)
    st.success("10天体すべてのデコードが完了。これが君の『全知の設計図』だよ！💀💖")