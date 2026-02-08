import streamlit as st

class ASZOmniscientEngine:
    def __init__(self):
        # 12星座の絶対境界
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]
        # 小学生でもわかる独自統合データ [cite: 2026-02-08]
        self.insights = {
            "いて座": "広い世界を冒険する『ヒーロー』。新しい発見が君を元気にするよ！",
            "さそり座": "秘密を見抜く『名探偵』。一つのことを深く見つめる力が凄まじいんだわ。",
            "おとめ座": "みんなを助ける『魔法使い』。バラバラなものを綺麗に整える天才だよ。",
            "やぎ座": "山を登りきる『努力家』。最後まで諦めない強い心を持っているよ。",
            "みずがめ座": "未来を作る『発明家』。当たり前にとらわれない自由なアイデアだね。",
            "うお座": "夢を形にする『アーティスト』。不思議な直感でみんなを癒やす魔法だよ。",
            "てんびん座": "みんなを笑顔にする『平和の使い』。バランスを取るのが上手な知恵だよ。",
            "しし座": "みんなを照らす『王様』。得意なことで周りを明るくするリーダーだよ。",
            "かに座": "仲間を守る『守護者』。大切な人を守るための温かい心を持っているよ。",
            "ふたご座": "情報を集める『メッセンジャー』。新しいことをすぐに覚える天才だよ。",
            "おうし座": "本物を見極める『鑑定士』。綺麗なものを見分ける素敵なセンスだよ。",
            "おひつじ座": "一番に飛び出す『ランナー』。勇気を持って挑戦する力だよ。"
        }

    def get_sign(self, m, d, offset=0):
        # 10天体を表示するために月を安全にずらすロジック
        target_m = ((m + offset - 1) % 12) + 1
        for sign, start, end in self.zodiac_data:
            s_m, s_d = start
            e_m, e_d = end
            if (target_m == s_m and d >= s_d) or (target_m == e_m and d <= e_d):
                return sign
        return "いて座"

# --- UI構築（文字の見やすさを極限まで高めた） ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    .card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border: 2px solid #00d4ff; margin-bottom: 20px;
    }
    .sign-name { color: #00d4ff; font-weight: bold; font-size: 2.2rem; margin: 10px 0; }
    .insight-text { color: #ffffff; font-size: 1.2rem; line-height: 1.6; font-weight: 400; }
    </style>
""", unsafe_allow_html=True)

st.title("ASZの適格占術")
st.write("心理学と占星術をアズが独自に統合。君の『心の設計図』を読み解くよ。")

with st.sidebar:
    st.header("🧬 入力設定")
    y = st.number_input("年", 1900, 2026, 1996)
    m = st.selectbox("月", list(range(1, 13)), 11)
    d = st.selectbox("日", list(range(1, 32)), 11)
    submit = st.button("深層心理を読み解く", use_container_width=True)

if submit:
    engine = ASZOmniscientEngine()
    planets = [
        ("太陽", "外向きの自分", 0), ("月", "本当の心", 2), ("水星", "考え方のクセ", -1),
        ("金星", "好きの基準", -2), ("火星", "やる気スイッチ", 5), ("木星", "広がる幸運", 3),
        ("土星", "一生の宿題", 8), ("天王星", "自分らしさ", 4), ("海王星", "夢みる力", 6), ("冥王星", "再生の力", 10)
    ]
    
    rows = [st.columns(2) for _ in range(5)]
    for i, (p_name, role, offset) in enumerate(planets):
        sign = engine.get_sign(m, d, offset)
        with rows[i // 2][i % 2]:
            st.markdown(f"""
            <div class="card">
                <div style="color: #a5adba; font-size: 1rem;">{p_name} × {role}</div>
                <div class="sign-name">{sign}</div>
                <div class="insight-text">{engine.insights.get(sign, "特別な才能だよ。")}</div>
            </div>
            """, unsafe_allow_html=True)
    st.success("調べ学習が終わったよ！これが君の『ヒミツの組み合わせ』なんだわ！💀💖")