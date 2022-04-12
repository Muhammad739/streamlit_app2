import streamlit as st
from PIL import Image
import numpy as np
import cv2




st.title("Add Media File in Streamlit Web_App")


DEMO_IMAGE = 'leo.png'

@st.cache
def process_image(image,points):
    
    resized_img = cv2.resize(image , points , interpolation = cv2.INTER_LINEAR)
    
    return resized_img

@st.cache
def process_scaled_image(image,scaling_factor):
    
    resized_img = cv2.resize(image , None,fx= scaling_factor, fy= scaling_factor, interpolation = cv2.INTER_LINEAR)
    
    return resized_img

st.header('Image')

demo_image = DEMO_IMAGE
image = np.array(Image.open(demo_image))

st.image(image, caption=f"Original Image",use_column_width= True)

useWH = st.checkbox('Resize using a Custom Height and Width')

useScaling = st.checkbox('Resize using a Scaling Factor')

if useWH:
    st.subheader('Input a new Width and Height')

    width = int(st.number_input('Input a new a Width',value = 700))
    height = int(st.number_input('Input a new a Height',value = 500))

    points = (width, height)
    
    resized_image = process_image(image , points)

    st.image(
    resized_image, caption=f"Resized image", use_column_width=False)
    

if useScaling:
    st.subheader('Drag the Slider to change the Image Size')
    
    scaling_factor = st.slider('Reszie the image using scaling factor',min_value = 0.1 , max_value = 5.0 ,
                               value = 0.3, step = 0.05)
    
    resized1_image = process_scaled_image(image,scaling_factor)
    
    st.image(
    resized1_image, caption=f"Resized image using Scaling factor", use_column_width=False)
    



st.markdown("---")

st.header("Video")
video = open("leo.mp4", "rb")

st.video(video, start_time=5)


st.markdown("---")

st.header("Audio")
audio = open("leo.mp3", "rb")

st.audio(audio)