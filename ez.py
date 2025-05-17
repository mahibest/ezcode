import streamlit as st
st.set_page_config(page_title="ez coding", page_icon="💻")
st.header("ez coding language")
code = st.text_input("1")
code1 = st.text_input("2")
code2 = st.text_input("3")
code3 = st.text_input("4")
code4 = st.text_input("5")
if "show" in code:
    sh = code.replace("show", "")
    st.write(sh)
if "ask" in code:
    ask = code.replace("ask", "")
    no_1 = st.text_input(ask)
if "show" in code1:
    sh2 = code1.replace("show", "")
    if "no_1" in sh2:
        st.write(sh2.replace("no_1", no_1))
    else:
        st.write(sh2)
if "ask" in code1:
    ask2 = code1.replace("ask", "")
    no_2 = st.text_input(ask2)
if "show" in code2:
    sh3 = code2.replace("show", "")
    if "no_1" in sh3:
        st.write(sh3.replace("no_1", no_1))
    if "no_2" in sh3:
        st.write(sh3.replace("no_2", no_2))
    else:
        st.write(sh3)
if "ask" in code2:
    ask3 = code2.replace("ask", "")
    no_3 = st.text_input(ask3)
if "show" in code3:
    sh4 = code3.replace("show", "")
    if "no_1" in sh4:
        st.write(sh4.replace("no_1", no_1))
    if "no_2" in sh4:
        st.write(sh4.replace("no_2", no_2))
    if "no_3" in sh4:
        st.write(sh4.replace("no_3", no_3))
    else:
        st.write(sh4)
if "ask" in code3:
    ask4 = code3.replace("ask", "")
    no_4 = st.text_input(ask4)
if "show" in code4:
    sh5 = code4.replace("show", "")
    if "no_1" in sh5:
        st.write(sh5.replace("no_1", no_1))
    if "no_2" in sh5:
        st.write(sh5.replace("no_2", no_2))
    if "no_3" in sh5:
        st.write(sh5.replace("no_3", no_3))
    if "no_4" in sh5:
        st.write(sh5.replace("no_4", no_4))
    else:
        st.write(sh5)
if "ask" in code4:
    ask5 = code4.replace("ask", "")
    no_5 = st.text_input(ask5)
