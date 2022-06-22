import streamlit as st
from streamlit import components
from PIL import Image
import numpy as np

# Explained function

def explained():
    st.title("Explanation")
    
    #introduction
    intro = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/intro.png')
    st.image(intro)
    
    
    #research question
    ques_title = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/researchq.png')
    st.image(ques_title)
    
    #hypothesis
    hypo_title = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/hypothesis_title.png')
    st.image(hypo_title)
    hypo = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/Hypothesis.jpg')
    st.image(hypo)
    
    #methodology
    m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/methodology.png')
    st.image(m)
    image = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/Toolbox Methodology.png')
    st.image(image, channels="BGR")
    
    #description for methodology
    a_m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/a_m.png')
    st.image(a_m)
    
    b_m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/b_m.png')
    st.image(b_m)
    
    c_m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/c_m.png')
    st.image(c_m)
    
    d_m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/d_m.png')
    st.image(d_m)
    
    e_m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/e_m.png')
    st.image(e_m)
    
    f_m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/f_m.png')
    st.image(f_m)
    
    g_m = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/g_m.png')
    st.image(g_m)
    
    title2 = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/rf.png')
    st.image(title2)
    
    #classification report
    cr_title = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/cr.png')
    st.image(cr_title)
    image1 = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/Toolbox assignment Classification Report.jpg')
    # new_title = '<p style="font-family:serif; color:Black; font-size: 25px;">Classification Report</p>'
    # st.markdown(new_title, unsafe_allow_html=True)
    st.image(image1, channels="BGR")
    
    #Confusion matrix
    cm_title = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/cm.png')
    st.image(cm_title)
    image2 = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/Toolbox assignment Confusion Matrix.jpg')
    # new_title = '<p style="font-family:serif; color:Black; font-size: 25px;">Confusion Matrix</p>'
    # st.markdown(new_title, unsafe_allow_html=True)
    # st.header("Confusion Matrix")
    st.image(image2, channels="BGR")
    
    #ROC-AUC Curve
    curve_title = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/rocauc.png')
    st.image(curve_title)
    image3 = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/ROCAUC Curve.jpg')
    # new_title = '<p style="font-family:serif; color:Black; font-size: 25px;">ROC-AUC Curve</p>'
    # st.markdown(new_title, unsafe_allow_html=True)
    # st.header("ROC-AUC Curve")
    st.image(image3, channels="BGR")
    
    #Model Explainer
    me_title = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/modelexplainer_title.png')
    st.image(me_title)
    image5 = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/Model Explainer.jpeg')
    st.image(image5, channels="BGR")
    
    conclusion = Image.open('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/conclusion.png')
    st.image(conclusion)
    
    st.balloons()
    