**Task 4: Custom Object Detection with YOLOv8**

**Objective**
Train a YOLOv8 model on a self-created, manually annotated dataset and perform object detection on a test video to validate model performance.

**Tools & Libraries Used**

* Python
* PyTorch
* Ultralytics YOLOv8
* GPU (CUDA) for accelerated training (optional)

**Workflow Summary**

**Device Check**

* Verified the availability of a CUDA-compatible GPU to enable faster training.

**Model Training**

* Custom dataset defined in `data.yaml`.
* Training parameters: 20 epochs, image size = 640, batch size = 4.
* Training outputs, including metrics, model checkpoints, and plots, are saved in `runs/detect/train/`.

**Inference on Video**

* Loaded the best-trained model (`best.pt`).
* Performed inference on `test_video.mp4` to detect objects frame-by-frame.
* Saved the output video with bounding boxes and labels drawn on detected objects.

**Key Outputs**

* Final trained model weights (`best.pt`).
* Training metrics and plots (mAP, precision, recall).
* Output video file with object detection predictions.

**Note**

* The dataset was manually annotated using tools like **Roboflow** or **LabelImg**.
* Ensure the `data.yaml` file is correctly configured and dataset folders strictly follow the YOLO format before initiating training.

