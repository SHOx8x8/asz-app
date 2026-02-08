import streamlit as st

class ASZOmniscientEngine:
    def __init__(self):
        # 心理学的・占術的役割（指標に基づいた平易な言葉）
        self.planets = {
            "太陽": {"role": "外向きの自分", "period": 365.25, "help": "お外で見せるかっこいい仮面。"},
            "月": {"role": "本当の心", "period": 27.3, "help": "おうちでリラックスしている時の心。"},
            "水星": {"role": "考え方のクセ", "period": 88.0, "help": "頭の動かし方やおしゃべりのコツ。"},
            "金星": {"role": "ワクワクの源", "period": 224.7, "help": "何を楽しい、きれいと感じるかのものさし。"},
            "火星": {"role": "やる気スイッチ", "period": 687.0, "help": "目標に突き進む時の心のエンジン。"},
            "木星": {"role": "ラッキーの広がり", "period": 4332.6, "help": "可能性を広げてくれる追い風。"},
            "土星": {"role": "これからの宿題", "period": 10759.2, "help": "乗り越えたら武器になるルール。"}
        }

    def get_analysis(self, y, m, d, gender):
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        results = []
        
        # 基準日（2000年1月1日 J2000.0）からの経過日数を簡易計算
        import datetime
        base_date = datetime.date(2000, 1, 1)
        target_date = datetime.date(y, m, d)
        diff_days = (target_date - base_date).days
        
        for name, info in self.planets.items():
            # 公転周期に基づいた星座の位置計算（簡易シミュレーション）
            # 各天体の「0地点」を調整して精度を向上 [cite: 2026-02-08]
            position = (diff_days / info["period"]) * 360
            idx = int((position / 30) + 9) % 12 # やぎ座付近を起点に調整
            sign = signs[idx]
            
            # 指標に基づいた解説生成
            detail = f"{sign}のエネルギーを{gender}としての個性に統合して。それが自分自身の設計図を完成させる鍵だよ。"
            results.append({"name": name, "sign": sign, "role": info['role'], "help": info['help'], "detail": detail})
        return results

# --- UIセクション（特定の個人に依存しないプロダクト設計） ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0e1117 0%, #161b22 100%); color: #f0f2f6; }
    .report-card { background: rgba(28, 33, 40, 0.7); padding: 24px; border-radius: 16px; border-top: 4px solid #00d4ff; margin-bottom: 20px; }
    .planet-title { color: #00d4ff; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 ASZの適格占術")

with st.sidebar:
    st.header("🧬 デコード設定")
    y = st.number_input("生まれ年", 1900, 2026, 1996)
    m = st.selectbox("月", list(range(1, 13)), 11)
    d = st.selectbox("日", list(range(1, 32)), 10)
    gender = st.selectbox("性別", ["男性", "女性", "指定なし"], 0)
    submit = st.button("深層心理をデコードする", use_container_width=True)

if submit:
    engine = ASZOmniscientEngine()
    analysis = engine.get_analysis(y, m, d, gender)
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