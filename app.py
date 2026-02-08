import streamlit as st
from google import genai

# タイトル
st.title("🔱 A.S.Z. Omniscient Nexus")

# 1. APIクライアントの作成 (極限までシンプルに)
if "GOOGLE_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("APIキーが見つからないよ！")
    st.stop()

# 2. 入力エリア
goal = st.text_area("AIに何をさせたい？", placeholder="今度こそ動いて！って入力してみて")

if st.button("Nexus 起動✨"):
    if goal:
        with st.spinner("接続中..."):
            try:
                # 3. 実行 (システム命令を一旦外して、純粋にモデルを呼び出す)
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=goal
                )
                st.success("成功！！やっと繋がったよ、ダーリン！💖")
                st.write(response.text)
                
            except Exception as e:
                # ここでエラーが出たら、モデル名を別バージョンで強制リトライ
                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash-exp", # もし1.5がダメなら最新の2.0を試す
                        contents=goal
                    )
                    st.success("2.0で接続成功！🚀")
                    st.write(response.text)
                except Exception as e2:
                    st.error(f"最終エラー：{e2}")