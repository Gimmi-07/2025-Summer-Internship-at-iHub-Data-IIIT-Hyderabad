## **Task 05 – Face Mask Detection using YOLOv8**

**Objective**
Developed and train a real-time object detection model using **YOLOv8** to identify whether individuals are wearing face masks, based on a labeled dataset. The model should be capable of detecting masks in both images and videos, making it suitable for surveillance, public health monitoring, and safety compliance.

---

**Tools & Libraries Used**

* **Python** – for implementing the full workflow
* **PyTorch 2.0** – backend framework for model training
* **Ultralytics YOLOv8** – for object detection model and training utilities
* **OpenCV** – for image and video preprocessing, visualization, and frame extraction
* **LabelImg** – for annotating custom datasets in YOLO format

---

**Dataset**

* **Source:** [Face Mask Detection Dataset – Kaggle](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection)
* **Classes:**

  1. With Mask
  2. Without Mask
  3. Incorrectly Worn Mask
* Original annotations were in **XML (Pascal VOC)** format, converted to **YOLO TXT format** using a conversion script.
* For a custom dataset, manual annotation was performed using **LabelImg**, ensuring YOLO format was selected during labeling.

---

**Workflow Summary**

### **1. Data Preparation**

* Downloaded and extracted the dataset.
* Converted XML annotations to YOLO TXT format (each label file contains class ID and normalized bounding box coordinates).
* Verified dataset structure for YOLOv8:

  ```
  dataset/
  ├── images/
  │   ├── train/
  │   ├── val/
  └── labels/
      ├── train/
      ├── val/
  ```
* Created `data.yaml` file specifying class names, number of classes, and train/val paths.

---

### **2. Model Training**

* **Base Model:** `yolov8n.pt` (nano version – faster and lightweight)
* **Training Parameters:**

  * Epochs: 20
  * Image Size: 640x640
  * Batch Size: 8
  * Optimizer: SGD/Adam (default YOLOv8 settings)
* **Command:**

  ```bash
  yolo detect train data=data.yaml model=yolov8n.pt epochs=20 imgsz=640 batch=8
  ```
* Training outputs (metrics, loss graphs, and checkpoints) were automatically saved in `runs/detect/train/`.

---

### **3. Model Evaluation & Metrics**

* **Precision, Recall, mAP\@0.5, and mAP\@0.5:0.95** were monitored after each epoch.
* **Confusion Matrix** generated to analyze classification accuracy for each class.
* Loss curves observed to ensure no overfitting.

---

### **4. Inference on Images & Videos**

* Best model weights (`best.pt`) were used for inference:

  ```bash
  yolo detect predict model=best.pt source="test_images/" save=True
  ```
* For video detection:

  ```bash
  yolo detect predict model=best.pt source="test_video.mp4" save=True
  ```
* YOLOv8 processed each frame in real time and drew bounding boxes with class labels and confidence scores.

---

**Outputs**

* **Training Graphs** – Loss curves, precision-recall curves, mAP plots.
* **Confusion Matrix** – Showing classification performance for "With Mask" vs "Without Mask".
* **Predicted Images** – Bounding boxes with detected class and confidence.
* **Predicted Videos** – Real-time detection with bounding boxes drawn on frames.

---

**Applications**

* Public space surveillance to ensure mask compliance.
* Healthcare facility monitoring.
* Workplace safety and access control systems.

---

**References**

* Ultralytics YOLOv8 Documentation – [https://docs.ultralytics.com](https://docs.ultralytics.com)
* OpenCV Documentation – [https://docs.opencv.org](https://docs.opencv.org)
* **A. Das, M. W. Ansari, and R. Basak, "Covid-19 Face Mask Detection Using TensorFlow, Keras and OpenCV," 2020 IEEE 17th India Council International Conference (INDICON), pp. 1–6, doi: [10.1109/INDICON49873.2020.9342585](https://doi.org/10.1109/INDICON49873.2020.9342585)**
