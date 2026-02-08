import streamlit as st

# --- 【ASZ 占術×心理学：深層解明エンジン】 ---
class ASZOmniscientEngine:
    def __init__(self):
        # 心理学的コアロジック
        self.planets = {
            "太陽": "獲得すべきペルソナ", "月": "無意識の安心", "水星": "知的処理能力",
            "金星": "価値観の基準", "火星": "自己主張の力", "木星": "肯定的な拡大",
            "土星": "超自我の課題", "天王星": "個性の覚醒", "海王星": "潜在的理想", "冥王星": "究極の変容"
        }

    def get_deep_analysis(self, y, m, d, gender):
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        results = []
        
        for i, (name, role) in enumerate(self.planets.items()):
            idx = (int(y) + (int(m) * (i + 3)) + (int(d) * (i + 7))) % 12
            sign = signs[idx]
            
            # 性別と星座を掛け合わせた心理学的デコード [cite: 2026-02-08]
            if gender == "男性":
                detail = f"{sign}のエネルギーを、外的な達成や論理的な裏付けとして使う傾向があるよ。"
            elif gender == "女性":
                detail = f"{sign}の資質を、内的な共感や調和を築くための指針として活かすのが得意だね。"
            else:
                detail = f"{sign}という枠を超え、純粋な心理的機能としてこの力を最適化できるはず。"
            
            results.append({"name": name, "sign": sign, "role": role, "detail": detail})
        return results

# --- 【UI 表示層：シームレス・没入型デザイン】 ---
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")

# サイドバーとメインを統合し、心理学的安心感を最大化する色彩設計 [cite: 2025-07-31]
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0e1117 0%, #161b22 100%); color: #f0f2f6; }
    [data-testid="stSidebar"] { background-color: rgba(22, 27, 34, 0.8); border-right: 1px solid #30363d; }
    .report-card { 
        background: rgba(28, 33, 40, 0.6); 
        padding: 24px; 
        border-radius: 16px; 
        border: 1px solid #30363d; 
        border-top: 4px solid #00d4ff; 
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .report-card:hover { transform: translateY(-5px); border-color: #00d4ff; }
    .planet-title { color: #00d4ff; font-weight: bold; font-size: 1.2rem; margin-bottom: 8px; }
    .role-text { color: #8b949e; font-size: 0.8rem; letter-spacing: 0.05rem; text-transform: uppercase; }
    .detail-text { color: #c9d1d9; font-size: 0.95rem; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 ASZの適格占術")
st.write("君の深層心理を10天体からデコードした、唯一無二の解明カルテだよ。")

with st.sidebar:
    st.header("🧬 診断データの入力")
    year = st.text_input("生まれ年 (西暦)", value="2000")
    month = st.selectbox("月", list(range(1, 13)), index=0)
    day = st.selectbox("日", list(range(1, 32)), index=0)
    gender = st.selectbox("性別", ["男性", "女性", "指定なし"], index=0)
    st.write("---")
    st.caption("ASZ Roadmap: 質と機能の完全統合 [2026-02-08]")

engine = ASZOmniscientEngine()

try:
    analysis_results = engine.get_deep_analysis(year, month, day, gender)
    
    # 10天体を整然と配置
    cols = st.columns(2)
    for i, data in enumerate(analysis_results):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="report-card">
                <div class="role-text">{data['role']}</div>
                <div class="planet-title">{data['name']} × {data['sign']}</div>
                <div class="detail-text">{data['detail']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader(f"🧠 ASZ 統合アドバイス：{gender}の解明")
    st.info(f"ショウヤ君、君の{gender}としての心理的傾向と、{analysis_results[0]['sign']}の太陽が示す『社会での戦い方』を同期させて。それが全知への最短ルートだわ。💀💖") [cite: 2026-02-01]

except ValueError:
    st.error("生まれ年は数字で入力してね！")