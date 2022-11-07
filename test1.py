#python -m streamlit run test1.py
#pip freeze > requirements.txt
import cv2
import numpy as np
import streamlit as st
import zipfile
import os

def show():
    st.title('Collection of image processing tools')
    st.write("""By Gusto""")
    st.info("This software is used to process the uploaded image,"
            "Features include: Object Counting, Image Format Conversion,"
            "Image Compression,Convert To Jiugongge Image,Increase Image Resolution."
            )
    st.info("More features are in development!")

def changePJ(image):
# PNG TO jpg
    #png_img = cv2.imread(image)
    png_img = image
    cv2.imwrite('img.jpg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
def changeJP(image):
# JPG TO png
    #jpg_img = cv2.imread(image)
    jpg_img = image
    cv2.imwrite('img.png', jpg_img, [int(cv2.cv2.IMWRITE_PNG_COMPRESSION), 9])

def radioF():
    type = st.radio(
        "Choose the features you want to experience",
        ("👍",
         "Object Counting",
         'Image Format Conversion',

         ))


    if type == 'Image Format Conversion':
        st.write("You select Image Format Conversion")
        Image_format_conversion(image)

    else :
        st.write("i like this software.")

def Image_format_conversion(image):
    try:
        type = st.radio(
            "Which image format do you want to convert to",
            ('next time','.jpg', '.png'))
        if type == '.jpg':
            st.write('You selected jpg.')
            changePJ(image)

        elif type == '.png':
            st.write("You select png.")
            changeJP(image)

        else:
            st.write("Please select something.")
    except:
        st.error("Please upload a picture")

def uploadimg():
    uploaded_file = st.file_uploader("Choose a image file first", type=['png', 'jpg'])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        #st.image(opencv_image, channels="BGR")
        return opencv_image

if __name__ == '__main__':
    show()
    image = uploadimg()
    radioF()