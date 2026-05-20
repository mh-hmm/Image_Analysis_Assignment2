
import streamlit as st
import cv2
import numpy as np
import util

# -------------------------
# Sidebar Controls
# -------------------------
def controls(ctr: util.Controls):
    st.sidebar.header("Controls")

    ctr.detector_type = st.sidebar.selectbox("Feature Detector", ["ORB", "SIFT"])
    ctr.n_features = st.sidebar.slider("Number of Features", 5, 400, 200)
    ctr.ratio_thresh = st.sidebar.slider("Match Ratio (Lowe's test)", 0.1, 1.00, 0.75)
    ctr.transform_type = st.sidebar.selectbox("Transform Type", ["Homography", "Affine"])

# -------------------------
# File Upload
# -------------------------
def load_img(img: tuple[util.ImageData,util.ImageData]):
    st.sidebar.subheader("Upload Images")

    img1_file = st.sidebar.file_uploader("Image 1", type=["jpg", "png"])
    img2_file = st.sidebar.file_uploader("Image 2", type=["jpg", "png"])



    if img1_file and img2_file:
        img1_temp = cv2.imdecode(np.frombuffer(img1_file.read(), np.uint8), 1)
        img2_temp = cv2.imdecode(np.frombuffer(img2_file.read(), np.uint8), 1)
    else:
        img1_temp, img2_temp = util.load_sample()

    img[0].img = util.resize(img1_temp)
    img[1].img = util.resize(img2_temp)