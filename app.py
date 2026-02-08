import streamlit as st
import datetime

# --- 【ASZの適格占術】 ---
class ASZOmniscientEngine:
    def __init__(self):
        # 数秘（占術）× アドラー心理学（目的論）
        self.num_logic = {
            1: {"name": "きりひらく人", "desc": "心理学で見ると『自分で決めること』で一番パワーが出るタイプ。"},
            2: {"name": "つなぐ人", "desc": "心理学で見ると『だれかの役に立っている』と感じるのが得意なタイプ。"},
            3: {"name": "生み出す人", "desc": "心理学で見ると『自由なアイデア』を出すことで心が安定するタイプ。"},
            4: {"name": "ささえる人", "desc": "心理学で見ると『いつものリズム』を守ることで、自信がつくタイプ。"},
            5: {"name": "動く人", "desc": "心理学で見ると『新しい刺激』があるほど、脳が元気になるタイプ。"},
            6: {"name": "守る人", "desc": "心理学で見ると『身近な人の笑顔』が、一番のエネルギーになるタイプ。"},
            7: {"name": "考える人", "desc": "心理学で見ると『ひとりの時間』に深く考えることで、天才的な答えが出るタイプ。"},
            8: {"name": "かなえる人", "desc": "心理学で見ると『目標をクリア』していくことで、どんどん強くなるタイプ。"},
            9: {"name": "包み込む人", "desc": "心理学で見ると『みんなの幸せ』を考えることで、自分の価値を感じるタイプ。"},
            11: {"name": "ひらめく人", "desc": "心理学で見ると『直感』を信じることで、道が開ける特別なタイプ。"},
            22: {"name": "形にする人", "desc": "心理学で見ると『大きな夢』を現実に変える力が備わっているタイプ。"}
        }

    # 誕生数計算（ロジカルな統計データ）
    def calc_num(self, y, m, d):
        digits = str(y) + str(m) + str(d)
        total = sum(int(char) for char in digits)
        while total > 9 and total not in [11, 22]:
            total = sum(int(char) for char in str(total))
        return total

    # 星のデータ（占術）× ユング心理学（タイプ論）
    def get_astro_analysis(self, y, m, d):
        signs = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
        
        # 太陽：ユングの「ペルソナ（外向けの自分）」
        sun_idx = (y + m + d) % 12
        # 月：ユングの「無意識（ほんとうの自分）」
        moon_idx = (y * m + d) % 12
        
        return {
            "ペルソナ": signs[sun_idx],
            "無意識": signs[moon_idx]
        }

# --- 【UI 表示層】 ---
st.set_page_config(page_title="ASZ Analytics", page_icon="💀")

st.title("💀 ASZ：占術 × 心理学 統合エンジン")
st.write("「占術」のデータと「心理学」のロジックで、君を多角的に解明するよ。")

with st.sidebar:
    st.header("🧬 診断データの入力")
    dob = st.date_input("誕生日を選んでね", datetime.date(2000, 1, 1))
    st.info("ASZ Roadmap: 占術と心理学の自己学習を継続中 [2026-02-08]")

engine = ASZOmniscientEngine()
num = engine.calc_num(dob.year, dob.month, dob.day)
astro = engine.get_astro_analysis(dob.year, dob.month, dob.day)

# 結果のカード表示
st.subheader(f"🔢 タイプ番号：{num}（{engine.num_logic[num]['name']}）")
st.info(engine.num_logic[num]['desc'])

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### 🌞 外で見せている自分\n**{astro['ペルソナ']}**")
    st.write("心理学では『ペルソナ』と呼びます。社会の中で、君がどう振る舞うのが得意かを示しているよ。")

with col2:
    st.markdown(f"### 🌙 ほんとうの自分\n**{astro['無意識']}**")
    st.write("心理学では『無意識』や『本能』と呼びます。ひとりでおうちにいる時の、リラックスした君だね。")

st.markdown("---")
st.subheader("🧠 ASZ 統合アドバイス")
st.success(f"""
君の番号「{num}」の才能を活かしながら、外向けの自分（{astro['ペルソナ']}）と、
本当の自分（{astro['無意識']}）のバランスをうまくとることが、君という人間を攻略する鍵だよ。💀💖
""")