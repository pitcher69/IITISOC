## 🧩 Modules Overview

### 1. Multi-view CAD Rendering
- **Function**: Render RGB and depth images of the CAD model from multiple viewpoints.
- **Input**: 3D CAD model `Q`
- **Output**: Multi-view RGB images, depth maps, point clouds

### 2. CAD Feature Extraction
- **Function**: Extract visual and geometric features from the rendered CAD views.
- **Input**: Rendered RGB images and point clouds
- **Output**: Visual descriptors (e.g., DINOv2), 3D geometric descriptors (e.g., PointNet++)

### 3. Segmentation
- **Function**: Segment candidate regions in the input image using zero-shot methods.
- **Input**: RGB-D image `I`, 3D model `Q`, K segmentation models
- **Output**: Set of candidate object masks

### 4. Scene Point Cloud Extraction
- **Function**: Extract the masked 3D point cloud of the target object from the scene.
- **Input**: RGB image, depth map, selected mask
- **Output**: Target object point cloud

### 5. Scene Feature Extraction
- **Function**: Extract visual and geometric features from the scene point cloud.
- **Input**: Scene point cloud
- **Output**: Visual descriptors, 3D geometric descriptors

### 6. Feature Matching
- **Function**: Match scene features with CAD features to find 3D-3D correspondences.
- **Input**: CAD and scene descriptors
- **Output**: Fused feature correspondences

### 7. Pose Estimation
- **Function**: Estimate 6D pose from 3D-3D correspondences using RANSAC.
- **Input**: Feature correspondences
- **Output**: Initial 6D pose `(R, t)`

### 8. Pose Refinement
- **Function**: Refine the estimated pose using ICP.
- **Input**: Initial pose, CAD and scene point clouds
- **Output**: Refined 6D pose

### 9. Pose Scoring
- **Function**: Compute confidence score of the pose using feature similarity and ICP inliers.
- **Input**: Refined pose, features
- **Output**: Pose confidence score

