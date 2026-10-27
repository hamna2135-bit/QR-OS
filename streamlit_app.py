import streamlit as st


st.set_page_config(
    page_title="QR OS",
    page_icon="🔳",
    layout="wide",
    initial_sidebar_state="locked"
)

with st.sidebar:
    st.sidebar.header("QRコード")
    st.button("読み取り")
    st.button("書き出し")


st.write("QRコードで情報を管理するOSもどきです。")
st.write("⬅️左のメニューから読み込みを行って操作してください")

