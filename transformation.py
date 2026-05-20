

import cv2
import numpy as np
import util


# -------------------------
# Transform Estimation
# -------------------------
def transform_estimation(img: tuple[util.ImageData,util.ImageData], ctr:util.Controls, match: util.Matching):
    kp1 = img[0].features[0]
    kp2 = img[1].features[0]

    match.aligned = None
    match.inliers = 0

    if len(match.matches) > 4:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in match.matches]).reshape(-1,1,2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in match.matches]).reshape(-1,1,2)

        if ctr.transform_type == "Homography":
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if M is not None:
                match.aligned = cv2.warpPerspective(img[0].img, M, (img[1].img.shape[1], img[1].img.shape[0]))
        else:
            M, mask = cv2.estimateAffine2D(src_pts, dst_pts)
            if M is not None:
                match.aligned = cv2.warpAffine(img[0].img, M, (img[1].img.shape[1], img[1].img.shape[0]))

        if mask is not None:
            match.inliers = int(mask.sum())