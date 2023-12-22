# monodepth_3d
monodepth2 + 3d reconstruction

## Introduction
This is the final work I submitted for the `robot vision_2023-2` class.

## Framework
Camera(take aphoto) -- RGB Image --> Depth Estimation -- Depth Map --> 3D Reconstruction -- Point Cloud / 3D Model --> Storage -- Visualizaation --> Screen

### Depth Estimation
    Input : RGB Image
    Output : Depth Map

Reference : Monodepth2
https://github.com/nianticlabs/monodepth2

#### Example
    python test_simple.py --image_path assets/test_image.jpg --model_name robot_model

### 3D Reconstruction
    Input : Depth Map
    Output : Point Cloud / 3D Model

Reference : opencv, numpy library
https://github.com/iwatake2222/opencv_sample/tree/master/01_article/01_3d_reconstruction
https://github.com/SerkanDemirci/reconstruction-from-depth

#### Example
    python depthTo3d.py test_result/test_image.jpg test_result/test_image_disp.jpeg test_image.ply 1148.93617021 1150.38461538 750 500

## ⚙️ Setup
I ran my experiments with =
PyTorch 0.4.1, CUDA 9.1, Python 3.6.6 and Ubuntu 20.04.
> `conda create -n monodepth2 python=3.6.6 anaconda`

    pip3 install torch torchvision torchaudio
    pip install tensorboardX
    conda install opencv=3.3.1   # just needed for evaluation


## 💾 Dataset
I used the raw KITTI dataset while training monodepth2.
2011/9/26, 2011/9/28, 2011/9/29, 2011/9/30, 2011/10/03

Folder structure of KITTI dataset
`{Date}/{Date}_drive_{num}_sync/image_{00~03}/data/{num}.jpg`
- image_00 : Left_B/W
- image_01 : Right_B/W
- image_02 : Left_RGB
- image_03 : Right_RGB

(If all the photos were used, there would be too many duplicated parts, so only the `image_02` folder was used for training.)

## Result

### test image
<p align="center">
  <img src="test_result/test_image.jpg" alt="test_image" width="600" />
  <img src="test_result/test_image_disp.jpeg" alt="test_image_disp" width="600" />
</p>

## Colab version
I also made colab version
https://colab.research.google.com/drive/1D8lU2vcgkR2xHJHfeS0vTGme5I9YL7KG?usp=sharing


Thankyou!