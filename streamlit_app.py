import streamlit as st
import cv2
import qrcode_fn as qr

st.set_page_config(
    page_title="QR OS",
    page_icon="🔳",
    layout="wide",
    initial_sidebar_state="locked"
)

#@st.dialog("QRコード読み取り")
#def qrread():
    #st.write("画像から読み取り")
    #code_image = st.file_uploader("画像から読み取り",type="image/*")
    #if code_image is not None:
    #    qr.detect(code_image)
    #if st.button("カメラから読み取り"):
    #    qr.camera()
#pic = None

#with st.sidebar:
#    st.header("QRコード読み取り")
#    code_image = st.file_uploader("画像から読み取り",type="image/*")
#    if code_image is not None:
#        qr.detect(code_image)
#    if st.button("カメラから読み取り"):
#        pic = st.camera_input("カメラ読み取り",label_visibility="hidden")
#    if pic is not None:
#        st.image(pic)
#        qr.detect(pic)
#    if st.button("新規"):
#        st.toast("ﾁﾝｯ 🍞")
    

st.title("QR OS")
st.write("QRコードで情報を管理するOSもどきです。")
st.write("下のメニューからQRコードを読み取り操作してください。")
st.write("はじめて使う方は新規を押してください")

col1,col2 = st.columns(2)
with col1:
    code_image = st.file_uploader("画像から読み取り",type="image/*")
    if code_image is not None:
        qr.detect(code_image)

with col2:
    #if st.button("カメラから読み取り"):
    enable = st.button("カメラから読み取り")
    pic = st.camera_input("カメラ読み取り",disabled=not enable,label_visibility="hidden")
    if pic:
        st.image(pic)
        qr.detect(pic)

if st.button("新規"):
    st.toast("ﾁﾝｯ 🍞")

#pic = st.camera_input("カメラ読み取り")
#if pic:
    #st.write("カメラ通ったよ")
    #qr.detect(pic)


#if __name__ == '__main__':
#    main()