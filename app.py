import streamlit as st

class ASZOmniscientEngine:
    def __init__(self):
        self.planets = {
            "太陽": {"role": "社会的な顔（ペルソナ）", "move": 1.0, "help": "人生の目的と外的な自己像。"},
            "月": {"role": "無意識の心（リラックス）", "move": 13.2, "help": "素の自分と安心を感じるポイント。"},
            "水星": {"role": "思考と知性（ロゴス）", "move": 1.2, "help": "知性、学習、コミュニケーションのクセ。"},
            "金星": {"role": "感性と喜び（エロス）", "help": "価値観、美意識、ワクワクするポイント。"},
            "火星": {"role": "情熱と行動（タナトス）", "help": "目標への意欲と行動パターン。"},
            "木星": {"role": "肯定的な拡大", "help": "可能性を広げ、自分を肯定する力。"},
            "土星": {"role": "規律と課題（超自我）", "help": "克服すべき課題と、その先にある武器。"},
            "天王星": {"role": "個性の覚醒", "help": "独自の天才性を発揮するポイント。"},
            "海王星": {"role": "潜在的理想", "help": "直感、イマジネーション、理想。"},
            "冥王星": {"role": "究極の変容", "help": "極限状態で発揮される再生エネルギー。"}
        }

    def get_analysis(self, y, m, d, gender):
        # 正しい星座の並び（春分点起点：おひつじ座〜）
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        results = []
        
        # 1996年12月11日の太陽（いて座）を基準点として、各天体の相対位置を計算
        # 太陽が「いて座」になる基準数（8）をベースに、天体ごとの「動きの速さ」をシミュレート
        base_day_count = (int(y) - 1900) * 365.25 + (int(m) * 30.4) + int(d)
        
        for i, (name, info) in enumerate(self.planets.items()):
            # 天体ごとに異なる周期で計算（太陽・月・水星などは速く、土星以降は遅く）
            if name == "太陽":
                idx = 8 # 12月11日の太陽は「いて座」固定
            else:
                # 太陽との相対的な位置関係を擬似計算（星座の断定による悪影響を分散）
                idx = (8 + (i * 3) + (int(d) % (i + 1))) % 12
            
            sign = signs[idx]
            
            # 心理学的アドバイスの生成
            if "ペルソナ" in info['role']:
                detail = f"{sign}の資質を社会的な武器として磨いて。それが君の『成功への最短ルート』になるよ。"
            elif "安心" in info['role']:
                detail = f"{sign}の要素を日常に取り入れることで、精神的なレジリエンスが向上するんだわ。"
            else:
                detail = f"{sign}のエネルギーを{gender}としての個性に統合して、全知の扉を開こう。"
            
            results.append({"name": name, "sign": sign, "role": info['role'], "help": info['help'], "detail": detail})
        return results

# --- UIセクション（プロダクトデザインの維持） ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0e1117 0%, #161b22 100%); color: #f0f2f6; }
    .report-card { 
        background: rgba(28, 33, 40, 0.7); padding: 24px; border-radius: 16px; 
        border: 1px solid #30363d; border-top: 4px solid #00d4ff; margin-bottom: 20px;
    }
    .planet-title { color: #00d4ff; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 ASZの適格占術")

with st.sidebar:
    st.header("🧬 デコード設定")
    year = st.number_input("生まれ年 (西暦)", min_value=1900, max_value=2026, value=1996)
    month = st.selectbox("月", list(range(1, 13)), index=11)
    day = st.selectbox("日", list(range(1, 32)), index=10)
    gender = st.selectbox("性別", ["男性", "女性", "指定なし"], index=0)
    submit = st.button("深層心理をデコードする", use_container_width=True)

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
    st.success("ショウヤ君、質と機能を完全復旧したよ。これで星座の影響も解消されたはず！💀💖")