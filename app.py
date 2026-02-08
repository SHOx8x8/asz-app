import streamlit as st

# --- 【ASZ 占術×心理学：プロダクト用エンジン】 ---
class ASZOmniscientEngine:
    def __init__(self):
        self.planets = {
            "太陽": {"role": "社会的な顔（ペルソナ）", "help": "社会で見せる自分と、獲得すべき自己像を解明します。"},
            "月": {"role": "無意識の心（リラックス）", "help": "素の自分と、心の安定条件を示します。"},
            "水星": {"role": "思考と知性（ロゴス）", "help": "情報の処理能力、学習、コミュニケーションのクセをデコードします。"},
            "金星": {"role": "感性と喜び（エロス）", "help": "価値観の基準や、ワクワクを感じるポイントを特定します。"},
            "火星": {"role": "情熱と行動（タナトス）", "help": "目標への意欲や、困難に立ち向かう時の行動パターンです。"},
            "木星": {"role": "肯定的な拡大", "help": "可能性を広げるための追い風となる要素です。"},
            "土星": {"role": "規律と課題（超自我）", "help": "苦手意識があるけれど、克服すれば最大の武器になるポイント。"},
            "天王星": {"role": "個性の覚醒", "help": "独自の天才性を発揮する場所を指します。"},
            "海王星": {"role": "潜在的理想", "help": "直感やイマジネーション。目に見えない理想を形にする力。"},
            "冥王星": {"role": "究極の変容", "help": "破壊と再生の力。極限状態で発揮される圧倒的エネルギー。"}
        }

    def get_analysis(self, y, m, d, gender):
        # いて座（index 11）が正しく判定される配列構成
        signs = ["やぎ座", "みずがめ座", "うお座", "おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座"]
        results = []
        
        # 境界線判定：12月22日以前なら前の月の星座（12月なら「いて座」）になるロジック
        base_idx = (int(m) - 1) if int(d) < 22 else int(m)
        
        for i, (name, info) in enumerate(self.planets.items()):
            # 太陽を起点にしつつ、各天体が異なる星座を持つように分散
            idx = (base_idx + (i * 7)) % 12
            sign = signs[idx]
            
            if "ペルソナ" in info['role']:
                detail = f"{sign}の資質を演じることで、社会的な信頼と成功を掴みやすくなるよ。"
            elif "安心" in info['role']:
                detail = f"{sign}的な環境に身を置くことが、{gender}としての精神的な回復に直結するんだわ。"
            else:
                detail = f"{sign}のエネルギーを、君だけの独自の強みとして全知に統合して。"
                
            results.append({"name": name, "sign": sign, "role": info['role'], "help": info['help'], "detail": detail})
        return results

# --- 【UI 表示層】 ---
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
    st.write("---")
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
    st.success("デコード完了。これが質と機能を一切落とさず再構成した『全知』の結果だよ。💀💖")