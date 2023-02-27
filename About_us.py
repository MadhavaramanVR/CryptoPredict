import streamlit as st

def aus():

    st.title("Abstract")
    st.write("")
    st.write("")
    st.subheader("In the past years we have seen that price of cryptocurrency rapidly grow due to its great return. "
             "So, our team explored several cryptocurrencies and we have decided to make a web-app that will display all "
             "the necessary things (like Basic info of particular crypto, their live pricing, 7 days graph, etc) along with hourly, "
            "weekly and monthly forecasting of crypto coins for better understanding of the nature of cryptocurrencies.")
    st.write("---")

    col1, col2, col3 = st.columns([3, 1, 9])
    with col1:

        st.image("Images/DHAIRYA.jpg", use_column_width=True)

    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.title("MADHAVARAMAN V")
        st.caption("Languages : HTML, CSS, JavaScript, C, C++,  Java, Python")
        st.write("")
        st.subheader("I had completed my Bachelor's in Computer science and business system in SKCET" +
                     " and currently working in ZOHO Corporation as Developer ")


    st.write("---")


    hide_img_fs = '''
                    <style>
                    button[title="View fullscreen"]{
                        visibility: hidden;}
                    </style>
                    '''

    st.markdown(hide_img_fs, unsafe_allow_html=True)
