**Task 3: Training YOLOv8 on African Wildlife Dataset**

**Objective**
Fine-tune the YOLOv8 object-detection model on the African Wildlife dataset and evaluate its performance using standard metrics and inference results.

**Tools & Libraries Used**

* Python
* Ultralytics YOLOv8
* NVIDIA GPU (optional, recommended for faster training)

**Workflow Summary**

**Model Initialization**

* Load the YOLOv8n base model from the Ultralytics hub (e.g., `yolov8n.pt`) as the starting weights.

**Training**

* Dataset: `african-wildlife.yaml` (4-class object detection dataset).
* Training parameters: 20 epochs, image size = 640, batch size = 8 (adjustable per GPU memory).
* Monitor training logs, metrics, and saved checkpoints; training artifacts (metrics, loss curves, confusion matrix, etc.) are stored in `runs/detect/train/`.

**Inference**

* Use the best-performing weights (`best.pt`) produced during training to run inference on sample wildlife images.
* Generate and visualize prediction outputs with bounding boxes and class labels.

**Key Outputs**

* Training logs and numeric metrics (precision, recall, mAP).
* Visual evaluation plots (loss & metric curves, confusion matrix).
* Inference images showing detected objects with predicted bounding boxes and class labels.

**Note**

* Ensure `african-wildlife.yaml` correctly references the `train/`, `val/` image and label directories and that labels follow YOLO format.
* Adjust `batch` and `img` sizes to fit available GPU memory; if no GPU is available, expect significantly longer training times on CPU.

