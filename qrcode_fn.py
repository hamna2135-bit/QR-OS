import streamlit as st
import cv2
import numpy as np

qcd = cv2.QRCodeDetector()
params = cv2.QRCodeEncoder_Params()
qce = cv2.QRCodeEncoder.create(params)


def camera():
    #cap = cv2.VideoCapture(0)
    #while True:
        # カメラから1フレーム読み取り
        #ret, frame = cap.read()
        #if not ret:
        #    continue
        #cap.release()
        #break
    pic = st.camera_input("code")
    if pic:
        detect(pic)




def detect(qrcode):
    file_bytes = np.frombuffer(qrcode.read(), np.uint8)
    item = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(item)
    if decoded_info == ():
        st.write("QRコードがありません")
    for deta in decoded_info:
        if deta == "":
            st.write("内容を読み取れませんでした")
        else:
            st.write(deta)

def main():
    pass

if __name__ == '__main__':
    main()