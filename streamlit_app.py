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
    st.button("新規")

st.title("QR OS")
st.write("QRコードで情報を管理するOSもどきです。")
st.write("⬅️左のメニューからQRコードを読み取り操作してください。")
st.write("はじめて使う方は新規を押してください")

