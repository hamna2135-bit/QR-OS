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
    #st.write("画像から読み取り")
    code_image = st.file_uploader("画像から読み取り",type="image/*")
    if code_image is not None:
        qr.detect(code_image)
    if st.button("カメラから読み取り"):
        qr.camera()

with st.sidebar:
    st.sidebar.header("QRコード")
    if st.button("読み取り"):
        qrread()
    if st.button("新規"):
        st.toast("ﾁﾝｯ 🍞")

st.title("QR OS")
st.write("QRコードで情報を管理するOSもどきです。")
st.write("⬅️左のメニューからQRコードを読み取り操作してください。")
st.write("はじめて使う方は新規を押してください")


#if __name__ == '__main__':
#    main()