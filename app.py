import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding", False)
model = pickle.load(open('new_model.pkl','b'))

def main():
 st.sidebar.header("Insurance Cost prediction")
 st.sidebar.text("This a Web app that tells you the predicted insurance costs."
 st.sidebar.heer("Just fill in the information below")
 st.sidebar.text( "The AdaBoost regression Model was used.")
 
 age =st.slider("Input Your age", 0, 100)
 sex =st.slider("Input your Gender with @ for female and 1 for male", 0,1)
 bmi =st.slider("Input your BMI", 0.0,78.8)
 children = st.slider("How many Children", 8,18)
 smoker= st.slider("Are you a smoker & for no and 1 for yes",0,1)
 
 inputs [[age, sex, bmi, children, smoker]]
 
 if st.button('Predict'):
  result model.predict(inputs)
  updated_res result.flatten().astype(float)
  st.success('The Your Insurance Costs will be{}'.format(updated_res))
if _name_=='_main_':
    main()  