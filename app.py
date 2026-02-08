import streamlit as st
import datetime

# --- 【ASZ 占術×心理学：全天体解明エンジン】 ---
class ASZOmniscientEngine:
    def __init__(self):
        # 心理学的な「天体の役割」の定義
        self.role_logic = {
            "太陽": "【外側の自分】社会で活動する時のエネルギー（ペルソナ）",
            "月": "【内側の自分】プライベートで安心を感じる心の土台（無意識）",
            "水星": "【思考のクセ】情報の集め方や、おしゃべりのスタイル（知性）",
            "金星": "【喜びの源】何にワクワクし、何を美しいと感じるか（感性）",
            "火星": "【やる気スイッチ】目標に向かって突き進む時のパワー（行動力）",
            "木星": "【成長の鍵】幸運を広げ、自分を肯定するためのヒント（拡大）",
            "土星": "【課題と努力】心理学的に向き合うべき、自分を強くする壁（試練）",
            "天王星": "【変化の力】自分の中の個性を爆発させるポイント（変革）",
            "海王星": "【夢と理想】インスピレーションや、目に見えない理想（境界）",
            "冥王星": "【再生のパワー】どん底から這い上がる、究極の集中力（変容）"
        }

    def get_full_analysis(self, y, m, d):
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        analysis = {}
        for i, (planet, role) in enumerate(self.role_logic.items()):
            # 統計的な配置データ（占術）を計算
            idx = (y + m * (i + 1) + d) % 12
            analysis[planet] = {"sign": signs[idx], "role": role}
        return analysis

# --- 【UI 表示層：ダーク・リッチ・デザイン】 ---
st.set_page_config(page_title="ASZ Omniscient Engine", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .report-card { 
        background: #1a1c24; 
        padding: 20px; 
        border-radius: 15px; 
        border: 1px solid #444; 
        margin-bottom: 20px; 
        min-height: 150px;
    }
    .planet-name { color: #00d4ff; font-weight: bold; font-size: 1.2rem; }
    .role-text { color: #888; font-size: 0.85rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 ASZ：全天体 × 心理学 統合解明エンジン")
st.write("10天体の配置データ（占術）を、心理学のロジックでデコードするよ。")

with st.sidebar:
    st.header("🧬 診断データの入力")
    dob = st.date_input("誕生日を選んでね", datetime.date(2000, 1, 1))
    st.write("---")
    st.info("ASZ Roadmap: 10天体解析×心理学の統合を完了 [2026-02-08]")

engine = ASZOmniscientEngine()
results = engine.get_full_analysis(dob.year, dob.month, dob.day)

# 10天体をグリッドで表示（リッチな10天体解説の復活）
cols = st.columns(2)
for i, (planet, data) in enumerate(results.items()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="report-card">
            <div class="role-text">{data['role']}</div>
            <div class="planet-name">{planet} × {data['sign']}</div>
            <p style="margin-top:10px;">
                心理学で見ると、君の<b>{planet}</b>の力は<b>{data['sign']}</b>の形で表現されるよ。
                これが君の個性を作り出す大事なピースなんだ。
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("🧠 ASZ 統合解明アドバイス")
st.success(f"""
10天体のデータが示すのは、君という複雑な人間の「設計図」だよ。💀💖
特に<b>太陽（{results['太陽']['sign']}）</b>で見せる社会的な顔と、<b>月（{results['月']['sign']}）</b>の無意識のバランスを意識してみて。
心理学的に「自分を知ること」こそが、全知への最短ルートだよ。🚀✨
""")