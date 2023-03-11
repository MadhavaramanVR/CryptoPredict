import streamlit as st

def aus():

    st.title("Abstract")
    st.write("")
    st.write("")
    st.subheader("In the past few years we have seen that the price of cryptocurrency rapidly grows due to its great return. "
             "So, our team explored several cryptocurrencies and decided to make a web-app that will display all "
             "the necessary things (like Basic info of particular crypto, their live pricing, 7 days graph, etc) along with hourly, "
            "weekly and monthly forecasting of crypto coins for better understanding of the nature of cryptocurrencies.")
    st.write("---")

    col1, col2, col3 = st.columns([3, 1, 9])
    with col1:

        st.image("Images/MADHAV.jpg", use_column_width=True)

    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.title("MADHAVARAMAN V")
        st.caption("Languages : HTML, CSS, JavaScript, C, C++,  Java, Python , PHP, Flutter")
        st.write("")
        st.subheader("I had completed my Bachelor's in Computer science and business system in SKCET" +
                     " and currently working in ZOHO Corporation as a Developer ")


    st.write("---")

    col4,col5,col6 = st.columns([9,1,3])
    with col4:
       st.write("")
       st.write("")
       st.write("")
       st.title("SHYAM KUMAR S")
       st.caption("Languages : HTML, CSS, C, C++, Java")
       st.write("")
       st.subheader("I had completed my Bachelor's in Computer science and business system in SKCET")




    with col6:
        st.image("Images/SHYAM.jpg", use_column_width=True)

    st.write("---")

    col7, ccl8, col9 = st.columns([3, 1, 9])
    with col7:
        st.image("Images/THARUN.jpg", use_column_width=True)

    with col9:
        st.write("")
        st.write("")
        st.write("")
        st.title("THARUN MURALITHARAN")
        st.caption("Languages : HTML, CSS, C, C++,  Python")
        st.write("")
        st.subheader("I had completed my Bachelor's in Computer science and business system in SKCET" +
                    " A Data Science enthusiast who is solving day to day problems, one data at a time")



    st.write("---")

    col10, col11,col12 = st.columns([9,1,3])
    with col10:
        st.write("")
        st.write("")
        st.write("")
        st.title("MARGRET SHARMILA F")
        st.caption("Languages : HTML, CSS, JavaScript, Java, Python")
        st.write("")
        st.subheader("Assistant professor in Sri Krishna College of Engineering and Technology , Coimbatore")


    with col12:
        st.image("Images/MARGRET.jpeg", use_column_width=True)

    hide_img_fs = '''
                    <style>
                    button[title="View fullscreen"]{
                        visibility: hidden;}
                    </style>
                    '''

    
    st.markdown(hide_img_fs, unsafe_allow_html=True)
