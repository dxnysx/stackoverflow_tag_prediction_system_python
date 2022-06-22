import streamlit as st
from streamlit import components
from PIL import Image
import requests
from Explained import explained
import joblib
import pickle
import os
import eli5
from explain_words import explain_words


loaded_clf = open("pickle_files/vectorizer.pkl", "rb")
job = joblib.load(loaded_clf)


# load model function


def load_prediction_models(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

# predict function


def predict():
    #st.title(':computer: StackOverflow Tag Predictor')
    image = Image.open(requests.get(
        'https://sachinkalsi.github.io/blog/data/images/blog_posts/stackoverflow.png', stream=True).raw)
    st.image(image, caption='Stackoverflow')

    # file uploader
    uploaded_file = st.file_uploader("Choose a file", type=['txt'])
    input_text = st.text_area('Enter question:')

   

    def file_features():

        # read file value
        bytes_data = uploaded_file.getvalue()
        # transform file value to matrix
        transform_file_matrix = job.transform([bytes_data]).toarray()
        predictor_dt = load_prediction_models(
            "pickle_files/model.pkl")
        result_dt = predictor_dt.predict(transform_file_matrix)
        st.text('Sentiment is {}'.format(result_dt))
        print(result_dt)
        display_explain = explain_words(str(bytes_data))
        raw_html = display_explain._repr_html_()
        components.v1.html(raw_html, height=2000)


    # for the text_input functions
    def text_features():
        # convert input to numeric matrix value
        transform_text_matrix = job.transform([input_text]).toarray()

        predictor_dt = load_prediction_models(
            "pickle_files/model.pkl")
        result_dt = predictor_dt.predict(transform_text_matrix)
        # st.success('Sentiment is {}'.format(result_dt))
        st.text('Sentiment is {}'.format(result_dt))
        display_explain = explain_words(input_text)

        #display_explain = output(input_text)
        raw_html = display_explain._repr_html_()
        components.v1.html(raw_html, height=2000)
        print(result_dt)


    if st.button('Predict'):
         # when no file and no input text are given then print error message
        if uploaded_file is None and len(input_text) <= 0:
            st.error('Upload a file or enter text')
        # when there is a file uploaded then run file_features
        elif uploaded_file is not None:
            file_features()
        else:
            text_features()
  


def main():
    # front end elements of the web page
    '''
    html_temp = """
        <div style="background-color:blue;padding:10px">
        <h1 style="color:white;text-align:center;">Streamlit ML app</h1>
        </div>
            """
    #st.markdown(html_temp, unsafe_allow_html=True)
    '''
    st.image('/Users/admin/Desktop/Data Science Toolbox/Group 2 Data Toolbox Assignment Submission/Streamlit codes/Data Sci Toolbox Images/Tag.PNG')
    activity = ['Prediction', 'Explanation']
    choice = st.sidebar.selectbox("Select Activity:", activity)

    if choice == 'Prediction':
        predict()
    elif choice == 'Explanation':
        explained()


if __name__ == '__main__':
    main()
