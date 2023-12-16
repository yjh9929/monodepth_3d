# monodepth_3d
monodepth2 + 3d reconstruction

## Introduction

## Framework
Camera(take aphoto) -- RGB Image --> Depth Estimation -- Depth Map --> 3D Reconstruction -- Point Cloud / 3D Model --> Storage -- Visualizaation --> Screen

### Depth Estimation
    Input : RGB Image
    Output : Depth Map

Reference : Monodepth2
https://github.com/nianticlabs/monodepth2

### 3D Reconstruction
    Input : Depth Map
    Output : Point Cloud / 3D Model

Reference : opencv, numpy library
https://github.com/iwatake2222/opencv_sample/tree/master/01_article/01_3d_reconstruction
https://github.com/SerkanDemirci/reconstruction-from-depth

## ⚙️ Setup
I ran my experiments with =
PyTorch 0.4.1, CUDA 9.1, Python 3.6.6 and Ubuntu 20.04.
`conda create -n monodepth2 python=3.6.6 anaconda`

    conda install pytorch=0.4.1 torchvision=0.2.1 -c pytorch
    pip install tensorboardX==1.4
    conda install opencv=3.3.1   # just needed for evaluation


## Result


## Conclusion

\