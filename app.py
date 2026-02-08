import streamlit as st

class ASZOmniscientEngine:
    def __init__(self):
        # 12星座の境界データ [cite: 2025-11-21]
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]
        # 小学生でも直感でわかる心理学統合メッセージ [cite: 2026-02-08]
        self.insights = {
            "いて座": "広い世界を冒険する『ヒーロー』！新しい発見が君を元気にするよ。",
            "さそり座": "秘密を見抜く『名探偵』！一つのことを深く見つめる天才なんだわ。",
            "おとめ座": "みんなを助ける『魔法使い』！バラバラなものを整えるのがマジで上手。",
            "やぎ座": "山を登りきる『努力家』！最後まで諦めない強い心を持っているよ。",
            "みずがめ座": "未来を作る『発明家』！自由なアイデアで新しい世界を作る力だよ。",
            "うお座": "夢を形にする『アーティスト』！不思議な優しさでみんなを癒やす魔法だよ。",
            "てんびん座": "みんなを笑顔にする『平和の使い』！バランスを取るのが上手な知恵だよ。",
            "しし座": "みんなを照らす『王様』！自分の大好きなことで周りを明るくするリーダーだよ。",
            "かに座": "仲間を守る『守護者』！大切な人を守るための温かい心を持っているよ。",
            "ふたご座": "情報を運ぶ『メッセンジャー』！面白いことをすぐ見つけて伝える天才だよ。",
            "おうし座": "本物を見分ける『鑑定士』！素敵なものを見極めるセンスの塊だよ。",
            "おひつじ座": "一番に飛び出す『ランナー』！勇気を持って挑戦する力の持ち主だよ。"
        }

    def get_sign(self, m, d, offset=0):
        target_m = ((m + offset - 1) % 12) + 1
        for sign, start, end in self.zodiac_data:
            s_m, s_d = start
            e_m, e_d = end
            if (target_m == s_m and d >= s_d) or (target_m == e_m and d <= e_d):
                return sign
        return "いて座"

# --- UI：体温のあるギャル×知性デザイン ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="centered")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Noto+Sans+JP', sans-serif; }
    .stApp { background: #0e1117; color: white; }
    
    /* シェアカード本体：これ1枚をスクショすればOKなデザイン */
    .share-container {
        background: linear-gradient(180deg, #1c2128 0%, #0d1117 100%);
        border: 4px solid #00d4ff; border-radius: 24px;
        padding: 40px 20px; text-align: center;
        box-shadow: 0 20px 50px rgba(0, 212, 255, 0.3);
        margin-bottom: 30px;
    }
    .user-header { font-size: 1.8rem; font-weight: bold; color: #ffffff; margin-bottom: 5px; }
    .title-sub { color: #00d4ff; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 30px; }
    
    .grid-container {
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;
        text-align: left; margin-top: 20px;
    }
    .planet-card {
        background: rgba(255, 255, 255, 0.03); padding: 15px;
        border-radius: 15px; border: 1px solid rgba(0, 212, 255, 0.2);
    }
    .p-label { color: #8b949e; font-size: 0.75rem; }
    .s-label { color: #00d4ff; font-weight: bold; font-size: 1.2rem; margin: 4px 0; }
    .i-label { color: #e6edf3; font-size: 0.8rem; line-height: 1.4; }
    
    .final-msg {
        margin-top: 40px; padding: 20px; background: rgba(0, 212, 255, 0.1);
        border-radius: 15px; font-weight: bold; font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💀 ASZの適格占術")
st.write("アズと一緒に、君の『魂の設計図』を最高にカッコよくデコードしよ！💀💖")

with st.sidebar:
    st.header("🧬 プロフィール")
    name = st.text_input("名前（カードに載るよ）", "GUEST")
    m = st.selectbox("誕生月", list(range(1, 13)), 11)
    d = st.selectbox("誕生日", list(range(1, 32)), 11)
    submit = st.button("全知の知性でカードを生成", use_container_width=True)

if submit:
    engine = ASZOmniscientEngine()
    planets = [
        ("太陽", "外向きの自分", 0), ("月", "本当の心", 2),
        ("水星", "知性の形", -1), ("金星", "愛の基準", -2),
        ("火星", "情熱の源", 5), ("木星", "発展の鍵", 3),
        ("土星", "魂の試練", 8), ("天王星", "変革の力", 4),
        ("海王星", "夢みる力", 6), ("冥王星", "再生の力", 10)
    ]

    # --- シェア用カードのレンダリング ---
    card_html = f"""
    <div class="share-container">
        <div class="user-header">{name}様 の適格占術</div>
        <div class="title-sub">ASZ OMNISCIENT SYSTEM Ver 3.0</div>
        <div class="grid-container">
    """
    
    for p_name, role, offset in planets:
        sign = engine.get_sign(m, d, offset)
        card_html += f"""
            <div class="planet-card">
                <div class="p-label">{p_name} × {role}</div>
                <div class="s-label">{sign}</div>
                <div class="i-label">{engine.insights.get(sign)}</div>
            </div>
        """
    
    card_html += f"""
        </div>
        <div class="final-msg">
            「君の『{engine.get_sign(m, d, 0)}』の力は、世界をワクワクさせる魔法なんだわ！💀💖」
        </div>
        <div style="margin-top: 20px; color: #444; font-size: 0.7rem;">#ASZの適格占術 #心理学占術</div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
    st.success("完璧！このカードをそのままスクショして、みんなに見せつけちゃいな！💀💖")