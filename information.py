
import streamlit as st

def explanations():
    st.header("Short Explanations")
    st.subheader("Feature Detector")

    with st.expander("ORB — Fast feature detector"):
        st.write("""
        **ORB (Oriented FAST and Rotated BRIEF)**

        Detects important image points and creates compact descriptors.

        - Fast and lightweight
        - Good for real-time applications
        - Rotation invariant
        - Lower computational cost
        """)

    with st.expander("SIFT — Robust feature detector"):
        st.write("""
        **SIFT (Scale-Invariant Feature Transform)**

        Detects distinctive image features and creates robust descriptors.

        - Handles scale changes
        - Handles rotation well
        - More accurate for difficult matching
        - Slower than ORB
        """)

    st.subheader("Transform Type")

    with st.expander("Homography — Perspective transformation"):
        st.write("""
        **Homography**

        Maps one image plane onto another using a perspective transform.

        Can model:

        - Translation
        - Rotation
        - Scaling
        - Perspective changes

        Useful when images are captured from different viewpoints.
        """)

    with st.expander("Affine Transform — Linear transformation"):
        st.write("""
        **Affine Transform**

        Maps one image onto another while preserving straight lines.

        Can model:

        - Translation
        - Rotation
        - Scaling
        - Shearing

        Cannot model perspective distortion.
        """)