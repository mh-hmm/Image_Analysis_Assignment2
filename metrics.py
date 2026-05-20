
import streamlit as st
import cv2
import numpy as np
import util


# -------------------------
# Metrics
# -------------------------
def metrics(img: tuple[util.ImageData,util.ImageData], match: util.Matching):
    st.header("Registration Metrics")

    num_matches = len(match.matches)
    inlier_ratio = (match.inliers / num_matches if num_matches > 0 else 0)

    # Alignment quality metrics
    mse = None
    mae = None
    overlap_score = None

    if match.aligned is not None:

        aligned = cv2.resize(match.aligned,(img[1].img.shape[1], img[1].img.shape[0]))

        diff = cv2.absdiff(aligned.astype(np.float32),img[1].img.astype(np.float32))

        # Mean Squared Error
        mse = np.mean(diff ** 2)

        # Mean Absolute Error
        mae = np.mean(diff)

        # Similarity estimate (0–1)
        overlap_score = max(0, 1 - (mae / 255))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Good Matches",num_matches)

        st.metric("Inliers",match.inliers)

    with col2:
        st.metric("Inlier Ratio",f"{inlier_ratio:.2f}")

        if mse is not None:
            st.metric("MSE",f"{mse:.1f}")

    with col3:
        if mae is not None:
            st.metric("MAE",f"{mae:.1f}")

        if overlap_score is not None:
            st.metric("Similarity",f"{overlap_score:.2%}")

    st.markdown("### Interpretation")

    if overlap_score is not None:

        if overlap_score > 0.85:
            st.success("Excellent registration: images align very closely.")

        elif overlap_score > 0.65:
            st.warning("Moderate registration: alignment works but may contain local errors.")

        else:
            st.error("Weak registration: significant mismatch remains.")