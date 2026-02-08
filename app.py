import streamlit as st
import datetime

# --- 【ASZ 占術×心理学：全天体解明エンジン】 ---
class ASZOmniscientEngine:
    def __init__(self):
        # 心理学的役割（10天体すべてを網羅） [cite: 2026-02-08]
        self.role_logic = {
            "太陽": "【社会的な顔】目標に向かうエネルギーとペルソナ",
            "月": "【無意識の心】安心を感じる土台とプライベート",
            "水星": "【知性と交流】思考のクセや情報の処理能力",
            "金星": "【感性と喜び】価値観や愛着形成のパターン",
            "火星": "【情熱と行動】意欲の源泉と自己主張のスタイル",
            "木星": "【拡大と肯定】可能性を広げるヒントと自己肯定",
            "土星": "【規律と課題】超自我に近い、成長のための制約",
            "天王星": "【変革と個性】独自性を発揮するポイント",
            "海王星": "【理想と境界】インスピレーションと潜在意識",
            "冥王星": "【変容と再生】究極の集中力と破壊的創造力"
        }

    def get_analysis(self, y, m, d, gender):
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        results = {}
        for i, (planet, role) in enumerate(self.role_logic.items()):
            idx = (int(y) + int(m) * (i + 1) + int(d)) % 12
            results[planet] = {"sign": signs[idx], "role": role}
        
        # 性別・心理学的アドバイス
        advices = {
            "男性": "社会的な達成（太陽・火星）と内面の受容（月・金星）の統合が鍵だよ。",
            "女性": "共感的な資質（月・金星）と個人の意志（太陽・火星）の調和が鍵だよ。",
            "指定なし": "ジェンダーの枠を超え、自己の中にある全天体の機能を最適化するのが理想的だよ。"
        }
        return results, advices.get(gender, advices["指定なし"])

# --- 【UI 表示層：色彩と配置の最適化】 ---
# ブラウザタブの名称変更 [cite: 2026-02-08]
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")

# 心理学的に安心感を与える深いネイビーと落ち着いたトーンのCSS [cite: 2025-07-31]
st.markdown("""
    <style>
    .stApp { background-color: #0f1116; color: #e0e0e0; }
    .report-card { 
        background: #1c1f26; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 4px solid #00d4ff; 
        margin-bottom: 15px;
    }
    .planet-title { color: #00d4ff; font-weight: bold; font-size: 1.1rem; }
    .role-desc { color: #a0a0a0; font-size: 0.85rem; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 ASZの適格占術")
st.write("10天体の配置から、君の心理的な設計図を客観的に解明するよ。")

with st.sidebar:
    st.header("🧬 入力データ")
    year = st.number_input("生まれ年 (西暦)", min_value=1900, max_value=2026, value=1996, step=1)
    month = st.selectbox("月", list(range(1, 13)), index=11)
    day = st.selectbox("日", list(range(1, 32)), index=10)
    gender = st.selectbox("性別", ["男性", "女性", "指定なし"], index=0)
    st.write("---")
    st.info("ASZ Roadmap: 10天体×心理学×UI最適化 [2026-02-08]")

engine = ASZOmniscientEngine()
results, gender_advice = engine.get_analysis(year, month, day, gender)

# 10天体を2列で整然と表示（絵文字はタイトルのみに限定）
cols = st.columns(2)
for i, (planet, data) in enumerate(results.items()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="report-card">
            <div class="role-desc">{data['role']}</div>
            <div class="planet-title">{planet} × {data['sign']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("🧠 心理学的解明アドバイス")
st.info(f"**【{gender}としての分析結果】**\n\n{gender_advice} 💀💖")