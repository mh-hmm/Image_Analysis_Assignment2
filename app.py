import streamlit as st
import util
import information
import input
import detection
import transformation
import visualisation
import metrics


ctr = util.Controls()
img = (util.ImageData(), util.ImageData())
match = util.Matching()


st.set_page_config(layout="wide")
st.title("Image Registration (Feature Matching + Transform)")

# Input and Information
input.controls(ctr)
information.explanations()
input.load_img(img)

# Registration
detection.feature_detection(img, ctr)
detection.feature_matching(img, ctr, match)
transformation.transform_estimation(img, ctr, match)

# Output
visualisation.visualisation(img, ctr, match)
metrics.metrics(img, match)