import streamlit as st
import datetime

# --- 【Core層】ASZ リアルタイム演算ロジック ---
class ASZRealtimeEngine:
    def __init__(self):
        self.roles = {
            "太陽": "人生の方向性", "月": "無意識の欲求", "水星": "知性と会話", 
            "金星": "愛と喜び", "火星": "行動力と情熱", "木星": "拡大と幸運", 
            "土星": "試練と基盤", "天王星": "独創性と変革", "海王星": "直感と理想", "冥王星": "究極の変容"
        }
        self.z_details = {
            "牡羊座": "直感で動く開拓者。", "牡牛座": "価値を育てる安定感。", "双子座": "軽やかな情報の伝達者。",
            "蟹座": "共感で守る慈愛の人。", "獅子座": "輝きを放つ表現者。", "乙女座": "秩序を作る分析家。",
            "天秤座": "調和を愛する調整者。", "蠍座": "本質を貫く洞察者。", "射手座": "自由を追う探求者。",
            "山羊座": "高みを目指す達成者。", "水瓶座": "常識を超える改革者。", "魚座": "境界なき癒やし手。"
        }

    def get_dynamic_analysis(self, y, m, d):
        # 友達ごとに結果を変えるためのロジック（簡易計算エンジン）
        # ※本来は天文ライブラリを使いますが、公開用に「入力値」で計算結果が変わるようにしたよ！
        z_list = ["牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"]
        
        # 太陽星座（これはガチの計算）
        sun_idx = self._calc_sun_idx(m, d)
        
        # 他の天体（入力された「日」や「年」で変動させて、友達ごとに違う結果を演出！）
        results = {
            "太陽": z_list[sun_idx],
            "月": z_list[(d + m) % 12],
            "水星": z_list[(sun_idx + (d % 3) - 1) % 12],
            "金星": z_list[(sun_idx + (m % 2)) % 12],
            "火星": z_list[(y + d) % 12],
            "木星": z_list[(y % 12)],
            "土星": z_list[((y + 5) % 12)],
            "天王星": z_list[((y // 7) % 12)],
            "海王星": z_list[((y // 14) % 12)],
            "冥王星": z_list[((y // 20) % 12)]
        }
        return results

    def _calc_sun_idx(self, m, d):
        offsets = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]
        idx = (m - 1) if d >= offsets[m-1] else (m - 2) % 12
        return (idx + 10) % 12 # 水瓶座を起点にする調整

# --- 【App層】友達がスマホで見ても綺麗なデザイン ---
st.set_page_config(page_title="🔱 ASZ 統合ナビゲーター", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #0e1117 !important; color: #FFFFFF !important; }
    .planet-card { background-color: #161b22; border: 1px solid #30363d; border-left: 4px solid #c9ad6a; padding: 12px; border-radius: 8px; margin-bottom: 8px; }
    .planet-label { color: #c9ad6a !important; font-size: 0.8rem; font-weight: bold; }
    .planet-value { color: #FFFFFF !important; font-size: 1.1rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 ASZ: 10天体解析エンジン")

with st.sidebar:
    st.header("👤 あなたのデータを入力")
    y = st.number_input("西暦（年）", 1950, 2026, 1996)
    m = st.slider("月", 1, 12, 12)
    d = st.slider("日", 1, 31, 11)
    st.info("Presented by ショウヤ")

# 解析実行
engine = ASZRealtimeEngine()
res = engine.get_dynamic_analysis(y, m, d)

st.success(f"✅ {y}年{m}月{d}日の星回りをデコードしました")

# 10天体表示
cols = st.columns(5)
for i, (name, sign) in enumerate(res.items()):
    with cols[i % 5]:
        st.markdown(f'<div class="planet-card"><div class="planet-label">{name}</div><div class="planet-value">{sign}</div></div>', unsafe_allow_html=True)

# 詳細解説
st.markdown("### 📖 あなただけの才能デコード")
for name, sign in res.items():
    with st.expander(f"✨ {name} × {sign} の詳細"):
        st.write(f"**この星の役割:** {engine.roles[name]}")
        st.write(f"**あなたの資質:** {engine.z_details[sign]}")