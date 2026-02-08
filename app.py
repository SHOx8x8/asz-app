import streamlit as st
from google import genai

# A.S.Z. Omniscient Nexus 構成 [cite: 2026-02-08]
st.title("🔱 A.S.Z. Omniscient Nexus")

if "GOOGLE_API_KEY" in st.secrets:
    # クライアント作成時に、明示的に API バージョンを 'v1' に固定する
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"],
        http_options={'api_version': 'v1'} # ここが 404 回避のキモ！
    )
else:
    st.error("APIキーを secrets.toml に設定してね！")
    st.stop()

goal = st.text_area("AIに何をさせたい？", placeholder="占い×心理学のビジョンを入力して...")

if st.button("Nexus 起動✨"):
    if goal:
        with st.spinner("Nexus 展開中..."):
            try:
                # バージョンを v1 に固定した状態でモデルを呼び出す
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=goal
                )
                st.success("繋がった！！これが全知の回答だよ、ダーリン！💖")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"接続エラー：{e}")
                st.info("このエラーが出る場合は、Google Cloud 側で『Generative Language API』が有効になっているか確認が必要かも。")