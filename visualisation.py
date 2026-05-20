
import streamlit as st
import cv2
import util



# -------------------------
# Visualization
# -------------------------
def visualisation(img: tuple[util.ImageData,util.ImageData], ctr:util.Controls, match: util.Matching):
    
    st.header("Visualisation")
    
    kp1 = img[0].features[0]
    kp2 = img[1].features[0]
    col1, col2 = st.columns(2)

    

    with col1:
        st.subheader("Original Image 1")
        st.image(img[0].img, channels="BGR")

        # Feature matches visualization
        match_img = cv2.drawMatches(img[0].img, kp1, img[1].img, kp2, match.matches[:20], None, flags=2)
        st.subheader("Feature Matches (Top 20)")
        st.image(match_img, channels="BGR")

    with col2:
        st.subheader("Image 1 aligned with Image 2")
        if match.aligned is not None:
            st.image(match.aligned, channels="BGR")
        else:
            st.warning("Alignment failed")


        # Heatmap difference
        if match.aligned is not None:
            diff = cv2.absdiff(match.aligned, img[1].img)
            heatmap = cv2.applyColorMap(diff, cv2.COLORMAP_JET)
            st.subheader("Difference Heatmap")
            st.image(heatmap, channels="BGR")