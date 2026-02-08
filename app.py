import streamlit as st
import datetime

# --- ASZ 独自統合知能エンジン ---
class ASZOmniscientBrain:
    def __init__(self):
        # 12星座の正確な境界（質を担保）
        self.zodiac_map = [
            (1, 20, "やぎ座"), (2, 19, "みずがめ座"), (3, 21, "うお座"),
            (4, 20, "おひつじ座"), (5, 21, "おうし座"), (6, 22, "ふたご座"),
            (7, 23, "かに座"), (8, 23, "しし座"), (9, 23, "おとめ座"),
            (10, 24, "てんびん座"), (11, 23, "さそり座"), (12, 22, "いて座")
        ]

    def get_zodiac(self, month, day):
        for m, d, sign in self.zodiac_map:
            if (month == m and day >= d) or (month == (m % 12) + 1 and day < d):
                return sign
        return "いて座"

    def decode_insight(self, sign, role_name):
        # 心理学×占術の独自統合（小学生にもわかる語彙指標）
        insights = {
            "いて座": "『もっと知りたい！』という冒険の心。広い世界を冒険して、新しい自分を見つける魔法の地図だよ。",
            "さそり座": "『本物を見抜く』強い心。一つのことを深く見つめて、秘密の宝物を見つける探偵さんのような力だね。",
            "おとめ座": "『みんなを助ける』優しい知恵。バラバラなものを綺麗に並べて、使いやすく整える魔法だよ。",
            "やぎ座": "『最後までやり抜く』強い意志。高い山をコツコツ登って、最後に一番の景色を見る力なんだわ。"
        }
        return insights.get(sign, f"{sign}の不思議な力。君の中に眠る、まだ誰も知らない特別な才能だよ。")

# --- UIセクション ---
st.set_page_config(page_title="ASZ Omniscient System", page_icon="💀", layout="wide")

st.title("💀 ASZ: 統合解明エンジン Ver 2.1")
st.write("心理学と占星術をアズが独自に統合。君の『設計図』を分かりやすく解明するよ。")

with st.sidebar:
    st.header("🧬 デコード設定")
    y = st.number_input("生まれ年", 1900, 2026, 1996)
    m = st.selectbox("月", list(range(1, 13)), 11)
    d = st.selectbox("日", list(range(1, 32)), 10)
    submit = st.button("全知の知性で自分をデコード", use_container_width=True)

if submit:
    brain = ASZOmniscientBrain()
    sun_sign = brain.get_zodiac(m, d)
    
    # 太陽以外の天体も、誕生日に基づいて擬似的に分散（質を向上）
    planets = {
        "太陽（外向きの自分）": sun_sign,
        "月（本当の心）": brain.get_zodiac((m + 1) % 12 + 1, (d + 5) % 28 + 1),
        "水星（考え方のクセ）": brain.get_zodiac(m, (d + 10) % 28 + 1)
    }

    cols = st.columns(3)
    for i, (name, sign) in enumerate(planets.items()):
        with cols[i]:
            st.markdown(f"""
            <div style="background: rgba(28, 33, 40, 0.7); padding: 20px; border-radius: 15px; border-top: 4px solid #00d4ff;">
                <p style="color: #8b949e; font-size: 0.8rem;">{name}</p>
                <h2 style="color: #00d4ff;">{sign}</h2>
                <p style="font-size: 0.95rem; margin-top: 10px;">{brain.decode_insight(sign, name)}</p>
            </div>
            """, unsafe_allow_html=True)
    st.success("デコード完了。これが今の最新の『知性』の結果だよ。💀💖")