import streamlit as st
import torch
import cv2
from PIL import Image
import numpy as np
def page2():
    
    
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    # Title and description
    st.title("Object Detection with YOLOv5")
    st.write("Upload an image to detect objects using YOLOv5.")
    
    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read uploaded image
        image = Image.open(uploaded_file)
        img_array = np.array(image)
    
        # Perform inference
        results = model(img_array)
    
        # Parse detection results
        for *boxes, conf, cls in results.xyxy[0]:  # Clip boxes to image bounds
            if conf > 0.4:  # Confidence threshold
                # Draw bounding box
                xmin, ymin, xmax, ymax = boxes
                xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)
                cv2.rectangle(img_array, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                cv2.putText(img_array, f'{model.names[int(cls)]}: {conf:.2f}', (xmin, ymin - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
        # Display original and annotated images
        st.image(image, caption='Original Image', use_column_width=True)
        st.image(img_array, caption='Annotated Image', use_column_width=True)