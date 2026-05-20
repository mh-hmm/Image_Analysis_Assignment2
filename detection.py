
import streamlit as st
import cv2
import util




# -------------------------
# Feature Detection
# -------------------------

def feature_detection(img: tuple[util.ImageData,util.ImageData], ctr:util.Controls):
    if ctr.detector_type == "ORB":
        detector = cv2.ORB_create(nfeatures=ctr.n_features)
    else:
        detector = cv2.SIFT_create(nfeatures=ctr.n_features)

    # features = []
    img[0].features = []
    img[1].features = []

    img[0].features = detector.detectAndCompute(cv2.cvtColor(img[0].img, cv2.COLOR_BGR2GRAY), None)
    img[1].features = detector.detectAndCompute(cv2.cvtColor(img[1].img, cv2.COLOR_BGR2GRAY), None)


# -------------------------
# Matching
# -------------------------
def feature_matching(img: tuple[util.ImageData,util.ImageData], ctr:util.Controls, match: util.Matching):

    des1 = img[0].features[1]
    des2 = img[1].features[1]

    if des1 is None or des2 is None:
        st.error("Feature detection failed. Try different parameters.")
        st.stop()

    if ctr.detector_type == "ORB":
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    else:
        bf = cv2.BFMatcher(cv2.NORM_L2)

    raw_matches = bf.knnMatch(des1, des2, k=2)

    match.matches = []


    for pair in raw_matches:

        # Sometimes KNN can return <2 neighbors
        if len(pair) < 2:
            continue

        m, n = pair

        # Lowe's ratio test
        if m.distance < ctr.ratio_thresh * n.distance:
            match.matches.append(m)

    # Sort by match quality
    match.matches = sorted(match.matches,key=lambda x: x.distance)