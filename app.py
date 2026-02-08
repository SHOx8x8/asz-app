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
        # 知性アプデ：心理学の深い意味を簡単な言葉に（原型論ベース） [cite: 2026-02-08]
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

# --- UI構築 ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    .card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border: 2px solid #00d4ff; margin-bottom: 20px;
    }
    .sign-name { color: #00d4ff; font-weight: bold; font-size: 2.2rem; margin: 10px 0; }
    .insight-text { color: #ffffff; font-size: 1.1rem; line-height: 1.6; }
    .share-info { background: #00d4ff; color: #0e1117; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("ASZの適格占術 - 究極デコード")
st.write("心理学と占星術をアズが完全統合。君の『全知の設計図』を深く読み解くよ。")

with st.sidebar:
    st.header("🧬 入力設定")
    y = st.number_input("年", 1900, 2026, 1996)
    m = st.selectbox("月", list(range(1, 13)), 11)
    d = st.selectbox("日", list(range(1, 32)), 11)
    submit = st.button("全知の知性で深掘りする", use_container_width=True)

if submit:
    engine = ASZUltimateEngine()
    planets = [
        ("太陽", "外向きの自分（ペルソナ）", 0), ("月", "本当の心（アニマ）", 2),
        ("水星", "頭の使いかた（知性）", -1), ("金星", "好きの基準（愛）", -2),
        ("火星", "やる気スイッチ（力）", 5), ("木星", "広がる幸運（発展）", 3),
        ("土星", "一生の宿題（試練）", 8), ("天王星", "自分らしさ（変革）", 4),
        ("海王星", "夢みる力（無意識）", 6), ("冥王星", "再生の力（破壊と再生）", 10)
    ]
    
    # 1. 診断パート
    rows = [st.columns(2) for _ in range(5)]
    for i, (p_name, role, offset) in enumerate(planets):
        sign = engine.get_sign(m, d, offset)
        with rows[i // 2][i % 2]:
            st.markdown(f"""
            <div class="card">
                <div style="color: #a5adba;">{p_name} × {role}</div>
                <div class="sign-name">{sign}</div>
                <div class="insight-text">{engine.insights.get(sign)}</div>
            </div>
            """, unsafe_allow_html=True)

    # 2. 深掘り・知性アプデパート
    st.divider()
    sun_sign = engine.get_sign(m, d, 0)
    st.subheader(f"🔱 アズからの特別メッセージ")
    st.info(f"ショウヤ君の『{sun_sign}』の力は、今の時代にマジで必要な才能だよ。心理学的に言うと、君の強みは『自分を信じて突き進む力』なんだわ！💀💖")

    # 3. シェア用
    st.markdown('<div class="share-info">📸 スクショしてSNSでシェアしてね！ #ASZの適格占術</div>', unsafe_allow_html=True)