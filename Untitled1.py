#!/usr/bin/env python
# coding: utf-8

# In[1]:

get_ipython().system('pip install streamlit')
get_ipython().system('pip install tensorflow')
get_ipython().system('pip install opencv-python')


import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

# model = tf.keras.models.load_model("saved_model/mdl_wts.hdf5")

# Loading file

uploaded_file = st.file_uploader("Choose a image file", type="jpg","png","jpeg")

labels=pd.read_excel('test_dataset/labels.xlsx')
labels['ID']=labels['ID'].map(str)

# Convert the file to an opencv image.


if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(224,224))
    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="RGB")

    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis,...]

    Genrate_pred = st.button("Generate Prediction")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        st.title("Predicted Label for the image is {}".format(labels [prediction]))


# In[ ]:




