import streamlit as st


st.set_page_config(
    page_title="QR OS",
    page_icon="🔳",
    layout="wide",
    initial_sidebar="locked",
    menu_items={
        "test":"a"
    }
)


st.write("QRコードで情報を管理するOSもどきです。")
st.write("⬅️左のメニューから読み込みを行って操作してください")

