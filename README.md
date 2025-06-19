# 🧊 FREEZE-Inspired 6D Pose Estimation Pipeline

This repository implements a modular, training-free 6D pose estimation pipeline. The system takes a 3D CAD model and an RGB-D scene image as input and estimates the 6D pose (rotation + translation) of the object in the scene using foundation models for geometry and vision.

---
### Google Colab Link
https://colab.research.google.com/drive/1Hk9ukODfuD4KrVSMEoGCGcJG6S1zISzL?usp=sharing#scrollTo=w0zFOYdAt62W
---

## 📚 Pipeline Overview

Each module is decoupled for clarity, modular testing, and development. Below is a summary of each module’s input, task, and output.

---

### 🔹 Module 1: Multi-view Rendering of CAD Model

- **📥 Input**: 
  - 3D CAD Model `Q`
- **🛠 Task**: 
  - Render multi-view RGB and depth images from different camera poses around the object.
  - Generate point clouds per view using known intrinsics and depth.
- **📤 Output**:
  - RGB images of CAD model
  - Depth images
  - CAD point clouds (per view)

---

### 🔹 Module 2: Feature Extraction from CAD Model

- **📥 Input**: 
  - RGB images and point clouds from Module 1
- **🛠 Task**: 
  - Extract:
    - **2D visual features** using models like **DINOv2**
    - **3D geometric features** using **FCGF**, **PointNet++**, or custom geometric encoders
- **📤 Output**:
  - `2a`: 2D visual features (DINOv2 per view)
  - `2b`: 3D geometric features (CAD keypoints/descriptors)

---

### 🔹 Module 3: Object Segmentation in RGB Scene

- **📥 Input**:
  - RGB image of the scene
- **🛠 Task**:
  - Use **FastSAM** or **SAM** for zero-shot segmentation
  - Select the mask corresponding to the target object
- **📤 Output**:
  - Binary mask for the target object

---

### 🔹 Module 4: Scene Point Cloud Extraction

- **📥 Input**:
  - RGB image
  - Binary object mask
  - Depth image
- **🛠 Task**:
  - Apply mask to depth and color
  - Generate 3D point cloud of the **visible** object in the scene
- **📤 Output**:
  - Target object point cloud extracted from the scene

---

### 🔹 Module 5: Scene Feature Extraction

- **📥 Input**:
  - Scene point cloud (target object only)
- **🛠 Task**:
  - Extract:
    - Visual features (optional 2D lifting + DINOv2)
    - Geometric features (FCGF or similar)
- **📤 Output**:
  - Scene feature descriptors (same format as CAD descriptors)

---

### 🔹 Module 6: Feature Fusion

- **📥 Input**:
  - CAD features (from Module 2)
  - Scene features (from Module 5)
- **🛠 Task**:
  - Concatenate or otherwise fuse visual + geometric features
  - Match scene features with CAD model features
- **📤 Output**:
  - Fused descriptors (query-target correspondences)

---

### 🔹 Module 7: Pose Estimation

- **📥 Input**:
  - Fused 3D-3D feature correspondences
- **🛠 Task**:
  - Estimate 6D pose using **RANSAC-based registration**
- **📤 Output**:
  - Initial pose hypothesis: `T = (R, t)`

---

### 🔹 Module 8: Pose Refinement

- **📥 Input**:
  - Initial pose hypothesis
  - Scene & CAD point clouds
- **🛠 Task**:
  - Refine pose using **ICP** (Iterative Closest Point)
  - Optionally perform **symmetry-aware selection**
- **📤 Output**:
  - Refined 6D pose estimate

---

### 🔹 Module 9: Validation & Scoring

- **📥 Input**:
  - Refined pose
  - Ground truth (if available) or synthetic renders
- **🛠 Task**:
  - Compute validation metrics (e.g., ADD-S, IoU)
  - Confidence scoring based on feature similarity and inlier ratios
- **📤 Output**:
  - Final pose confidence
  - Quantitative evaluation metrics

---

## 🛠 Requirements

- Python 3.9+
- PyTorch
- Open3D
- Trimesh, Pyrender
- DINOv2 (via HuggingFace or custom)
- FCGF / PointNet++ for 3D descriptors
- FastSAM or SAM for segmentation

---

## 🚀 How to Run

Each module can be tested independently. A full run involves:
```bash
1. Run Module 1 to render multi-view CAD images.
2. Extract features using Module 2.
3. Segment scene using Module 3.
4. Extract target object from depth in Module 4.
5. Extract scene features in Module 5.
6. Match & fuse in Module 6.
7. Estimate pose via Module 7.
8. Refine with ICP in Module 8.
9. Score and validate in Module 9.
