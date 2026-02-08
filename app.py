import streamlit as st
import datetime

# --- 【ASZ 占術×心理学：全天体解明エンジン】 ---
class ASZOmniscientEngine:
    def __init__(self):
        # 心理学的役割の定義
        self.role_logic = {
            "太陽": "【社会的な顔】目標に向かうエネルギー",
            "月": "【無意識の心】安心を感じる土台",
            "火星": "【行動の源】情熱やトラブルへの対応",
            "金星": "【感性の窓】好き、心地いいと感じる力"
        }

    def get_analysis(self, y, m, d, gender):
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        results = {}
        for i, (planet, role) in enumerate(self.role_logic.items()):
            idx = (int(y) + int(m) * (i + 1) + int(d)) % 12
            results[planet] = {"sign": signs[idx], "role": role}
        
        # 性別による心理学的補足
        if gender == "男性":
            advice = "社会的な役割や行動力の強さを、どう周囲と調和させるかが鍵だよ。"
        elif gender == "女性":
            advice = "心の安定や感性の豊かさを、どう社会的な表現に繋げるかが鍵だよ。"
        else:
            advice = "自分の中の『男性性』と『女性性』のバランスを最適化するのが全知への道だよ。"
            
        return results, advice

# --- 【UI 表示層：名称変更版】 ---
# ブラウザのタブ表記を変更 [cite: 2026-02-08]
st.set_page_config(page_title="ASZの適格占術", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .report-card { 
        background: #1a1c24; 
        padding: 15px; 
        border-radius: 12px; 
        border: 1px solid #444; 
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# アプリ内のタイトルを変更 [cite: 2026-02-08]
st.title("💀 ASZの適格占術")
st.write("占術の統計データと心理学を融合させた、君だけの解明カルテだよ。")

with st.sidebar:
    st.header("🧬 診断データの入力")
    # 年は入力、月日は選択のハイブリッドUIを維持 [cite: 2025-07-31]
    year = st.number_input("生まれた年 (西暦)", min_value=1900, max_value=2026, value=2000, step=1)
    month = st.selectbox("生まれた月", list(range(1, 13)), index=0)
    day = st.selectbox("生まれた日", list(range(1, 32)), index=0)
    gender = st.selectbox("性別を選んでね", ["男性", "女性", "指定なし"], index=2)
    
    st.write("---")
    st.info("ASZ Roadmap: タイトル変更 & 性別ロジック統合 [2026-02-08]")

engine = ASZOmniscientEngine()
results, gender_advice = engine.get_analysis(year, month, day, gender)

# 結果表示
cols = st.columns(2)
for i, (planet, data) in enumerate(results.items()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="report-card">
            <div style="color: #888; font-size: 0.8rem;">{data['role']}</div>
            <div style="color: #00d4ff; font-weight: bold; font-size: 1.1rem;">{planet} × {data['sign']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("🧠 心理学アドバイス")
st.success(f"**【{gender}としての解明】**\n\n{gender_advice} 💀💖")