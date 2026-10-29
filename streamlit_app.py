import streamlit as st
import cv2
import qrcode_fn as qr

st.set_page_config(
    page_title="QR OS",
    page_icon="🔳",
    layout="wide",
    initial_sidebar_state="locked"
)
@st.dialog("QRコード読み取り")
def qrread():
    st.write("画像から読み取り")
    code_image = st.file_uploader("QRコード",type="image/*")
    for item in code_image:
        qr.detect(item)
    st.button("カメラから読み取り")
    

with st.sidebar:
    st.sidebar.header("QRコード")
    st.button("読み取り",on_click=qrread())
    st.button("新規")

st.title("QR OS")
st.write("QRコードで情報を管理するOSもどきです。")
st.write("⬅️左のメニューからQRコードを読み取り操作してください。")
st.write("はじめて使う方は新規を押してください")

