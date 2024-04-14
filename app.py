import streamlit as st
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
#st.image("fr.jpg")
st.title("Flower Recognition")
st.write("Flowers allowed are:-['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']")
image=st.file_uploader("Upload image")
CLASS_NAMES = ['dog','cat']
MODEL = tf.keras.models.load_model("dogvscat.h5")
if st.button("Submit"):
    size=(64,64)
    image = np.array((Image.open(image)).resize(size))
    img_batch = np.expand_dims(image, 0)
    
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence =(np.max(predictions[0])*100)
    st.write("class:",predicted_class,)
    st.write("confidence:",confidence)