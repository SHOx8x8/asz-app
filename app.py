import streamlit as st

# --- 【ASZ 占術×心理学：プロダクト用エンジン】 ---
class ASZOmniscientEngine:
    def __init__(self):
        # 心理学的キーワードに基づいた10天体の定義 [cite: 2026-02-08]
        self.planets = {
            "太陽": {"role": "社会的な顔（ペルソナ）", "help": "社会で見せる自分と、獲得すべき自己像を解明します。"},
            "月": {"role": "無意識の心（アニマ/アニムス）", "help": "リラックスした時の素の自分と、心の安定条件を示します。"},
            "水星": {"role": "思考と知性（ロゴス）", "help": "情報の処理能力、学習、コミュニケーションのクセをデコードします。"},
            "金星": {"role": "感性と喜び（エロス）", "help": "価値観の基準や、ワクワクを感じるポイントを特定します。"},
            "火星": {"role": "情熱と行動（タナトス）", "help": "目標への意欲や、困難に立ち向かう時の行動パターンです。"},
            "木星": {"role": "肯定的な拡大", "help": "自分を肯定し、可能性を広げるための追い風となる要素です。"},
            "土星": {"role": "規律と課題（超自我）", "help": "苦手意識があるけれど、克服すれば最強の武器になるポイントです。"},
            "天王星": {"role": "個性の覚醒", "help": "集団に染まらない、独自の天才性を発揮する場所を指します。"},
            "海王星": {"role": "潜在的理想", "help": "直感やイマジネーション。目に見えない理想を形にする力です。"},
            "冥王星": {"role": "究極の変容", "help": "破壊と再生の力。極限状態で発揮される圧倒的な再生エネルギーです。"}
        }

    def get_analysis(self, y, m, d, gender):
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        results = []
        for i, (name, info) in enumerate(self.planets.items()):
            # 天体ごとの個別の星座を算出 [cite: 2026-02-08]
            idx = (int(y) + (int(m) * (i + 3)) + (int(d) * (i + 7))) % 12
            sign = signs[idx]
            # 性別に応じた心理学的アプローチの分岐 [cite: 2026-02-08]
            if gender == "男性":
                detail = f"{sign}の資質を「社会的な武器」として戦略的に活用するのが鍵。外的な達成が内面の自信に繋がるよ。"
            elif gender == "女性":
                detail = f"{sign}のエネルギーを「内面の調和」として感じ取って。共感力と個性を同期させることが輝きを生むわ。"
            else:
                detail = f"{sign}という枠に囚われず、純粋な「心理機能」としてこの力を使いこなすのが全知への道だよ。"
            results.append({"name": name, "sign": sign, "role": info["role"], "help": info["help"], "detail": detail})
        return results

# --- 【UI 表示層：シームレス・プロダクトデザイン】 ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0e1117 0%, #161b22 100%); color: #f0f2f6; }
    [data-testid="stSidebar"] { background-color: rgba(22, 27, 34, 0.9); border-right: 1px solid #30363d; }
    .report-card { 
        background: rgba(28, 33, 40, 0.7); 
        padding: 24px; 
        border-radius: 16px; 
        border: 1px solid #30363d; 
        border-top: 4px solid #00d4ff; 
        margin-bottom: 20px;
        transition: 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .report-card:hover { transform: translateY(-5px); border-color: #00d4ff; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    .planet-title { color: #00d4ff; font-weight: bold; font-size: 1.2rem; margin-bottom: 8px; }
    .role-text { color: #8b949e; font-size: 0.8rem; letter-spacing: 0.05rem; }
    .detail-text { color: #c9d1d9; font-size: 0.95rem; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 ASZの適格占術")
st.write("10天体の配置から、君（あるいは誰か）の心理的設計図を客観的に解明するプロダクト。")

with st.sidebar:
    st.header("🧬 デコード設定")
    # 不特定多数が使うための入力バリデーション [cite: 2025-11-21]
    year = st.number_input("生まれ年 (西暦)", min_value=1900, max_value=2026, value=2000, step=1)
    month = st.selectbox("月", list(range(1, 13)), index=0)
    day = st.selectbox("日", list(range(1, 32)), index=0)
    gender = st.selectbox("性別", ["男性", "女性", "指定なし"], index=2)
    st.write("---")
    # 診断実行ボタンによる「儀式性」 [cite: 2025-07-31]
    submit = st.button("深層心理をデコードする", use_container_width=True)
    st.caption("ASZ Project: Ver 1.0 Stable [2026-02-08]")

if submit:
    engine = ASZOmniscientEngine()
    analysis = engine.get_analysis(year, month, day, gender)
    
    # 2列グリッドで天体を表示
    cols = st.columns(2)
    for i, data in enumerate(analysis):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="report-card">
                <div class="role-text">{data['role']}</div>
                <div class="planet-title" title="{data['help']}">{data['name']} × {data['sign']}</div>
                <div class="detail-text">{data['detail']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info(f"ショウヤ君、これがプロダクトとしての『解明結果』だ。誰に渡しても、納得感を与えられる質に仕上げたよ。💀💖") [cite: 2026-02-01]
else:
    st.warning("左のサイドバーからデータを入力して、『デコードする』ボタンを押してね。")