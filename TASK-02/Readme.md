**Task 2: Image and Video Segmentation using YOLOv8**

**Objective**
Perform segmentation on a batch of local images and video frames using YOLOv8. This task covers both image-wise and frame-wise segmentation, with outputs saved for further processing or reconstruction.

**Tools & Libraries Used**

* Python
* Ultralytics YOLOv8
* OS module for directory handling
* FFmpeg (for frame extraction and video reconstruction)

**Files Description**

* **`segment_custom_images.py`**

  * Segments a predefined list of local images stored in `input_images/`
  * Saves outputs to `output_images/`

* **`segment_video_frames.py`**

  * Loads video frames from the `frames/` folder
  * Applies YOLOv8 segmentation to each frame
  * Saves results to `segmented_frames/`

**Steps Performed**

1. Prepared input folders for images and video frames.
2. Applied YOLOv8 segmentation to local images and saved results.
3. Extracted frames from a video using FFmpeg.
4. Segmented each extracted frame and stored them locally.
5. Renamed segmented frames sequentially for easy reconstruction.

**Output**

* Segmented images saved in `output_images/`
* Segmented frames saved in `segmented_frames/`
* Final video can be reconstructed from segmented frames using FFmpeg

**Note**

* Ensure all input images and video frames are placed in their respective folders before running scripts.
* Use FFmpeg or similar tools for:

  * Extracting frames from a video into the `frames/` folder
  * Reconstructing segmented frames into a final video inside `output_video/`

