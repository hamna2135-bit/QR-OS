import streamlit as st
import cv2
import numpy as np

qcd = cv2.QRCodeDetector()
params = cv2.QRCodeEncoder_Params()
qce = cv2.QRCodeEncoder.create(params)

def detect(qrcode):
    file_bytes = np.frombuffer(qrcode.read(), np.uint8)
    item = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(item)
    if decoded_info == ():
        st.error("QRコードがありません")
    for deta in decoded_info:
        if deta == "":
            st.error("内容を読み取れませんでした")
        else:
            st.write(deta)

def main():
    pass

if __name__ == '__main__':
    main()