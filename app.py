import streamlit as st

class ASZUltimateEngine:
    def __init__(self):
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]
        self.insights = {
            "いて座": "広い世界を冒険する『ヒーロー』。まだ誰も知らない『答え』を見つける旅人だよ。",
            "さそり座": "秘密を見抜く『名探偵』。心の奥にある『本当の気持ち』を掘り出す天才だね。",
            "おとめ座": "みんなを助ける『魔法使い』。バラバラなものをピカピカに整えて、役に立てる力だよ。",
            "やぎ座": "山を登りきる『努力家』。高い目標に向かって、一歩ずつ確実に進む強い意志なんだわ。",
            "みずがめ座": "未来を作る『発明家』。みんなの『当たり前』を壊して、新しい自由を作る知恵だよ。",
            "うお座": "夢を形にする『アーティスト』。目に見えない優しさを、みんなに届ける不思議な魔法だよ。",
            "てんびん座": "笑顔を広げる『平和の使い』。みんなが仲良くなれる、キラキラしたバランス感覚だよ。",
            "しし座": "光り輝く『王様』。自分の大好きなことで、周りの人をパッと明るくするリーダーだよ。",
            "かに座": "仲間を守る『守護者』。大切な人のピンチを助ける、海のように深い愛情だよ。",
            "ふたご座": "情報を運ぶ『メッセンジャー』。面白いことをたくさん見つけて、世界をワクワクさせるよ。",
            "おうし座": "本物を見つける『鑑定士』。五感を使って、本当に価値があるものを大切にするセンスだよ。",
            "おひつじ座": "一番に走り出す『ランナー』。怖がらずに、新しい自分へ飛び込む勇気の塊だよ。"
        }

    def get_sign(self, m, d, offset=0):
        target_m = ((m + offset - 1) % 12) + 1
        for sign, start, end in self.zodiac_data:
            s_m, s_d = start
            e_m, e_d = end
            if (target_m == s_m and d >= s_d) or (target_m == e_m and d <= e_d):
                return sign
        return "いて座"

# --- UI設定 ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    .share-card {
        background: linear-gradient(135deg, #1c2128 0%, #0d1117 100%);
        padding: 30px; border-radius: 20px; border: 3px solid #00d4ff;
        margin-top: 20px; box-shadow: 0 10px 30px rgba(0,212,255,0.2);
    }
    .planet-box {
        background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px;
        border-left: 4px solid #00d4ff; margin-bottom: 15px;
    }
    .sign-title { color: #00d4ff; font-weight: bold; font-size: 1.5rem; }
    .user-name { color: #ffffff; font-size: 1.8rem; font-weight: bold; border-bottom: 2px solid #00d4ff; }
    </style>
""", unsafe_allow_html=True)

st.title("💀 ASZの適格占術")
st.write("心理学と占星術を独自に統合。世界に一人だけの『心の設計図』を読み解きます。")

with st.sidebar:
    st.header("🧬 プロフィール入力")
    u_name = st.text_input("お名前（ニックネーム）", "ゲスト")
    y = st.number_input("生まれ年", 1900, 2026, 1996)
    m = st.selectbox("月", list(range(1, 13)), 11)
    d = st.selectbox("日", list(range(1, 32)), 11)
    submit = st.button("全知の知性で読み解く", use_container_width=True)

if submit:
    engine = ASZUltimateEngine()
    planets = [
        ("太陽", "外向きの自分", 0), ("月", "本当の心", 2), ("水星", "知性の形", -1),
        ("金星", "愛の基準", -2), ("火星", "情熱の源", 5), ("木星", "幸運の鍵", 3),
        ("土星", "魂の試練", 8), ("天王星", "自分らしさ", 4), ("海王星", "夢みる力", 6), ("冥王星", "再生の力", 10)
    ]
    
    st.markdown(f"""
    <div class="share-card">
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="color: #a5adba; font-size: 1rem;">Special Analysis for</div>
            <div class="user-name">{u_name} 様</div>
        </div>
    """, unsafe_allow_html=True)

    rows = [st.columns(2) for _ in range(5)]
    for i, (p_name, role, offset) in enumerate(planets):
        sign = engine.get_sign(m, d, offset)
        with rows[i // 2][i % 2]:
            st.markdown(f"""
            <div class="planet-box">
                <div style="color: #8b949e; font-size: 0.8rem;">{p_name} × {role}</div>
                <div class="sign-title">{sign}</div>
                <div style="font-size: 0.9rem; margin-top: 5px;">{engine.insights.get(sign)}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: center; margin-top: 20px; padding: 15px; background: rgba(0,212,255,0.1); border-radius: 10px;">
            <div style="color: #00d4ff; font-weight: bold;">🔱 アズからの深層メッセージ</div>
            <div style="font-size: 1.1rem; margin-top: 10px;">
                {u_name}様の『{engine.get_sign(m, d, 0)}』の光は、周りを導く特別なエネルギーを秘めているんだわ！💀💖
            </div>
        </div>
        <div style="text-align: right; margin-top: 15px; color: #8b949e; font-size: 0.8rem;">#ASZの適格占術</div>
    </div>
    """, unsafe_allow_html=True)
    st.success("調べ学習完了！このカードを保存してシェアしてね！")