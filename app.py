import streamlit as st

# --- 【ASZ 占術×心理学：プロダクト用エンジン】 ---
class ASZOmniscientEngine:
    def __init__(self):
        # 心理学的役割（アズによる噛み砕き説明）
        self.planets = {
            "太陽": {"role": "外向きの自分（ペルソナ）", "help": "学校や仕事場で見せている『かっこいい自分』の仮面。"},
            "月": {"role": "素の自分（アニマ/アニムス）", "help": "おうちでリラックスしている時の、本当の自分の心。"},
            "水星": {"role": "考え方のクセ（ロゴス）", "help": "おしゃべりや勉強をする時の、頭の動かし方のコツ。"},
            "金星": {"role": "ワクワクの源（エロス）", "help": "何を『楽しい！』『きれい！』と感じるかのものさし。"},
            "火星": {"role": "やる気スイッチ（タナトス）", "help": "目標に向かって突き進む時の、心のエンジン。"},
            "木星": {"role": "ラッキーの広がり", "help": "自分の可能性をどんどん広げてくれる、追い風の力。"},
            "土星": {"role": "これからの宿題（超自我）", "help": "少し苦手だけど、乗り越えたら一生の武器になるルール。"},
            "天王星": {"role": "自分だけの個性", "help": "周りに合わせない、自分だけのキラリと光るセンス。"},
            "海王星": {"role": "夢みる力（イマジネーション）", "help": "目に見えない理想や、ふと思いつく不思議な直感。"},
            "冥王星": {"role": "生まれ変わるパワー", "help": "ピンチの時に爆発する、底知れない再生のエネルギー。"}
        }

    def get_analysis(self, y, m, d, gender):
        # 星座配列（春分点起点）
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        results = []
        
        # 12月11日が「いて座」になる基準点の計算
        base_idx = (int(m) - 1) if int(d) < 22 else int(m)
        
        for i, (name, info) in enumerate(self.planets.items()):
            # 各天体が重ならないよう、太陽との相対位置を分散させる
            # 太陽（i=0）が「いて座」になるように調整
            idx = (base_idx + (i * 7) + 8) % 12
            sign = signs[idx]
            
            # アズによる「小学生でもわかる」解説
            if "ペルソナ" in info['role']:
                detail = f"{sign}の力を『お外用の仮面』として使ってみて。周りのみんなと仲良くしながら、自分の良さを伝えるための大事な道具だよ。"
            elif "アニマ" in info['role']:
                detail = f"{sign}は君の『心のガソリン』。ここが満たされると、どんな時でも元気が湧いてくる、自分だけの秘密のパワー源なんだわ。"
            elif "ロゴス" in info['role']:
                detail = f"{sign}のやり方で考えると、難しい問題もスラスラ解けちゃうかも！自分に合った頭の使い方のヒントだよ。"
            else:
                detail = f"{sign}のエネルギーを、君だけの独自の強みとして大切にして。それが『自分自身』を完成させる鍵だよ。"
                
            results.append({"name": name, "sign": sign, "role": info['role'], "help": info['help'], "detail": detail})
        return results

# --- 【UI 表示層：シームレス・没入型デザイン】 ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0e1117 0%, #161b22 100%); color: #f0f2f6; }
    [data-testid="stSidebar"] { background-color: rgba(22, 27, 34, 0.9); border-right: 1px solid #30363d; }
    .report-card { 
        background: rgba(28, 33, 40, 0.7); 
        padding: 24px; border-radius: 16px; border: 1px solid #30363d; 
        border-top: 4px solid #00d4ff; margin-bottom: 20px; transition: 0.3s;
    }
    .report-card:hover { transform: translateY(-5px); border-color: #00d4ff; }
    .planet-title { color: #00d4ff; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 ASZの適格占術")
st.write("心理学と占星術を融合した、あなたの心の設計図。")

with st.sidebar:
    st.header("🧬 デコード設定")
    # 初期値としてショウヤ君のデータをセット
    year = st.number_input("生まれ年 (西暦)", min_value=1900, max_value=2026, value=1996)
    month = st.selectbox("月", list(range(1, 13)), index=11)
    day = st.selectbox("日", list(range(1, 32)), index=10)
    gender = st.selectbox("性別", ["男性", "女性", "指定なし"], index=0)
    st.write("---")
    submit = st.button("深層心理をデコードする", use_container_width=True)
    st.caption("ASZ Project: Ver 1.2 Logic Restored [2026-02-08]")

if submit:
    engine = ASZOmniscientEngine()
    analysis = engine.get_analysis(year, month, day, gender)
    cols = st.columns(2)
    for i, data in enumerate(analysis):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="report-card">
                <div style="color: #8b949e; font-size: 0.8rem;">{data['role']}</div>
                <div class="planet-title" title="{data['help']}">{data['name']} × {data['sign']}</div>
                <div style="color: #c9d1d9; font-size: 0.95rem; margin-top: 8px;">{data['detail']}</div>
            </div>
            """, unsafe_allow_html=True)
    st.info("デコードが完了したよ。自分の『設計図』をゆっくり眺めてみてね。")