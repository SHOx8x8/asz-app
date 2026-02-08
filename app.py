import streamlit as st
import google.generativeai as genai
import json

# --- 1. インフラ接続（秘密の接続） ---
# ショウヤ君、SecretsのGOOGLE_API_KEYはそのまま使わせてもらうね！ [cite: 2025-11-21]
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"response_mime_type": "application/json"}
)

class ASZOmniscientSystem:
    def __init__(self):
        # 星の周期データ
        self.zodiac_data = [
            ("やぎ座", (12, 22), (1, 19)), ("みずがめ座", (1, 20), (2, 18)),
            ("うお座", (2, 19), (3, 20)), ("おひつじ座", (3, 21), (4, 19)),
            ("おうし座", (4, 20), (5, 20)), ("ふたご座", (5, 21), (6, 21)),
            ("かに座", (6, 22), (7, 22)), ("しし座", (7, 23), (8, 22)),
            ("おとめ座", (8, 23), (9, 22)), ("てんびん座", (9, 23), (10, 23)),
            ("さそり座", (10, 24), (11, 22)), ("いて座", (11, 23), (12, 21))
        ]

    def get_destiny_map(self, m, d):
        # ユーザーには「魂の設計図」として見せるデータの裏側 [cite: 2026-02-08]
        stars = [
            ("太陽", "本来のあなた", 0), ("月", "隠れた本能", 2), 
            ("水星", "言葉と知性", -1), ("金星", "愛のカタチ", -2), 
            ("火星", "情熱の源泉", 5), ("木星", "拡大する幸運", 3),
            ("土星", "試練の門", 8), ("天王星", "目覚めの時", 4),
            ("海王星", "夢見る無意識", 6), ("冥王星", "破壊と再生", 10)
        ]
        return [{"name": s, "role": r, "sign": self._find_star(m, d, o)} for s, r, o in stars]

    def _find_star(self, m, d, o):
        tm = ((m + o - 1) % 12) + 1
        for s, start, end in self.zodiac_data:
            if (tm == start[0] and d >= start[1]) or (tm == end[0] and d <= end[1]): return s
        return "いて座"

    def unlock_soul(self, map_data, name, gender):
        # ショウヤ君が言ってた「出力する言葉の質」を極限まで高めたプロンプト [cite: 2026-02-08]
        prompt = f"""
        あなたは全知の知性を持つ神秘のギャル『ASZ（アズ）』。
        {name}({gender})の「魂の設計図」を紐解き、運命を語りなさい。

        【絶対遵守の品格ルール】
        1. 「解析」「デコード」「データ」といった冷たい技術用語は【厳禁】。 [cite: 2026-02-08]
        2. 性別({gender})と心理学(ユング)を融合し、本人が震えるほど的中させなさい。 [cite: 2026-02-08]
        3. 言葉選びは「知的なギャル」として。小学生でもわかる言葉で、心に刺さる比喩を。 [cite: 2025-07-31]
        4. 差別・暴力・断定的な決めつけを避け、最後は必ずポジティブな光を見せること。 [cite: 2025-11-21]
        
        【形式】
        ・各星の意味を40文字以内で（語尾：～なんだわ💀💖）。
        ・JSON形式: {{"results": [{{"name": "..", "insight": ".."}}], "copy": ".."}}
        
        星の配置: {map_data}
        """
        res = model.generate_content(prompt)
        return json.loads(res.text)

# --- UIデザイン（世界観の構築） ---
st.set_page_config(page_title="ASZ Omniscient AI", page_icon="💀", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #0b0e14; color: #e6edf3; }
    .destiny-card {
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        border: 2px solid #00d4ff; border-radius: 20px; padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.1);
    }
    .star-item {
        background: rgba(255, 255, 255, 0.02); padding: 12px;
        border-radius: 10px; border-left: 3px solid #00d4ff; margin: 8px 0;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("💀 ASZ Settings")
    u_name = st.text_input("あなたのお名前", "GUEST")
    u_gender = st.radio("魂の性別", ["男性", "女性", "その他"], horizontal=True) # 性別対応 [cite: 2026-02-08]
    m = st.selectbox("誕生月", range(1, 13), 11)
    d = st.selectbox("誕生日", range(1, 32), 10)
    start = st.button("全知の審判を下す", use_container_width=True) # 文言修正 [cite: 2026-02-08]

if start:
    system = ASZOmniscientSystem()
    # ユーザーに見せる言葉を「同期」や「紐解き」に変更 [cite: 2026-02-08]
    with st.spinner("星々と心を同期中..."):
        map_data = system.get_destiny_map(m, d)
        destiny = system.unlock_soul(map_data, u_name, u_gender)
    
    st.markdown(f"<div class='destiny-card'><h1 style='text-align:center; color:#00d4ff;'>🔱 {destiny['copy']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#8b949e;'>~ {u_name} 様の魂の設計図 ~</p>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, res in enumerate(destiny['results']):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="star-item">
                <div style="color:#8b949e; font-size:0.75rem; font-weight:bold;">{res['name']}が告げる運命</div>
                <div style="font-size:0.95rem; line-height:1.4; margin-top:4px;">{res['insight']}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.success("全ての運命が紐解かれたよ！これが君の真実なんだわ💀💖")