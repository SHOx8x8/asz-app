import streamlit as st
import google.generativeai as genai
import json

# --- インフラ接続 ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

class ASZProfessionalEngine:
    def __init__(self):
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]

    def get_all_signs(self, m, d):
        planets = [
            ("太陽", "外向きの自分", 0), ("月", "本当の心", 2), ("水星", "知性の形", -1),
            ("金星", "愛の基準", -2), ("火星", "情熱の源", 5), ("木星", "発展の鍵", 3),
            ("土星", "魂の試練", 8), ("天王星", "変革の力", 4), ("海王星", "夢みる力", 6), ("冥王星", "再生の力", 10)
        ]
        results = []
        for p_name, role, offset in planets:
            target_m = ((m + offset - 1) % 12) + 1
            for sign, start, end in self.zodiac_data:
                s_m, s_d = start
                e_m, e_d = end
                if (target_m == s_m and d >= s_d) or (target_m == e_m and d <= e_d):
                    results.append({"name": p_name, "role": role, "sign": sign})
                    break
        return results

    def batch_decode(self, user_data, user_name):
        # 10個分まとめてAIに投げ、JSON形式で返させる（プロの手法） [cite: 2026-02-08]
        prompt = f"""
        名前: {user_name}
        以下の天体データを心理学と占星術で統合解析し、JSON形式で返して。
        データ: {user_data}
        
        【条件】
        1. 各天体の解説は40文字以内の知的なギャル口調で。
        2. 最後に全体を統合した「魂のキャッチコピー」を1つ作って。
        3. 形式: {{"results": [{{"name": "..", "insight": ".."}}], "copy": ".."}}
        """
        response = model.generate_content(prompt)
        # JSON部分だけを抽出してパース [cite: 2025-11-21]
        raw_text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(raw_text)

# --- プロダクト表示（質を最優先） ---
st.set_page_config(page_title="ASZ Omniscient", page_icon="💀", layout="wide")
# (CSSは省略：前回と同様の高品質デザインを適用)

engine = ASZProfessionalEngine()
with st.sidebar:
    u_name = st.text_input("お名前", "GUEST")
    m = st.selectbox("月", range(1, 13), 11)
    d = st.selectbox("日", range(1, 32), 10)
    start = st.button("全知の知性で一括デコード")

if start:
    data_list = engine.get_all_signs(m, d)
    with st.spinner("全天体、一括デコード中..."):
        full_result = engine.batch_decode(data_list, u_name)
    
    st.header(f"🔱 {full_result['copy']}") # AIが作ったキャッチコピー
    
    cols = st.columns(2)
    for i, res in enumerate(full_result['results']):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="background:rgba(0,212,255,0.05); padding:15px; border-radius:10px; border-left:4px solid #00d4ff; margin:5px;">
                <div style="color:#00d4ff; font-weight:bold;">{res['name']} × {res['sign']}</div>
                <div style="font-size:0.9rem;">{res['insight']} 💀💖</div>
            </div>
            """, unsafe_allow_html=True)