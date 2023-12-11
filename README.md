# monodepth_3d
monodepth2 + 3d reconstruction

## Introduction

## Framework
Camera(take aphoto) -- RGB Image --> Depth Estimation -- Depth Map --> 3D Reconstruction -- Point Cloud / 3D Model --> Storage -- Visualizaation --> Screen

### Depth Estimation
    Input : RGB Image
    Output : Depth Map

    Backbone : Monodepth2
    https://github.com/nianticlabs/monodepth2

### 3D Reconstruction
    Input : Depth Map
    Output : Point Cloud / 3D Model

    Backbone : opencv, numpy library
    https://github.com/iwatake2222/opencv_sample/tree/master/01_article/01_3d_reconstruction
    https://github.com/SerkanDemirci/reconstruction-from-depth

## Result


## Conclusion
