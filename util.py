# util.py


import streamlit as st
import cv2
import numpy as np


# Load sample images if none uploaded
def load_sample():
    img1 = cv2.imread("sample_images/Sample_1.png")
    img2 = cv2.imread("sample_images/Sample_2.png")
    return img1, img2


# Resize for performance
def resize(img, max_dim=800):
    h, w = img.shape[:2]
    scale = max_dim / max(h, w)
    if scale < 1:
        img = cv2.resize(img, (int(w*scale), int(h*scale)))
    return img




class Controls:

    # def __init__(self):
    #     st.sidebar.header("Controls")
    #     detector_type = st.sidebar.selectbox("Feature Detector", ["ORB", "SIFT"])
    #     n_features = st.sidebar.slider("Number of Features", 5, 400, 200)
    #     ratio_thresh = st.sidebar.slider("Match Ratio (Lowe's test)", 0.1, 1.00, 0.75)
    #     transform_type = st.sidebar.selectbox("Transform Type", ["Homography", "Affine"])

    detector_type = None
    n_features = None
    ratio_thresh = None
    transform_type = None

class ImageData:
    img = None
    # (kp, des)
    features = []

    def reset():
        features = [] 

class Matching:
    matches = []
    aligned = None
    inliers = 0

    def reset(self):
        matches = []
        aligned = None
        inliers = 0



class Registrator:

    ctr = Controls()

    img1 = ImageData()
    img1 = ImageData()

    match = Matching()


    

    def __init__(self, img1_file = None, img2_file = None):
            if img1_file and img2_file:
                img1 = cv2.imdecode(np.frombuffer(img1_file.read(), np.uint8), 1)
                img2 = cv2.imdecode(np.frombuffer(img2_file.read(), np.uint8), 1)
            else:
                st.info("Using sample images")
                img1, img2 = load_sample()

            img1 = resize(img1)
            img2 = resize(img2)