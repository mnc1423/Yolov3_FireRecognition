# Yolov3_FireRecognition
implementation of Yolo_v3 for fire recognition

Original repository https://github.com/AlexeyAB/darknet

Model is made to run on a Jetson Tx2 board: https://developer.nvidia.com/embedded/jetson-tx2

## Requirements 

Built in Linux environment (check original repository for Windows version)

* **OpenCV** >= 2.4 (For Jetson Tx2 board Used 3.4.0)
* **CUDA** == 9.0 (CUDA 10.0 is supported in original repository)
* **cuDNN** == 7.6.3
* **GPU** with **CC**: https://en.wikipedia.org/wiki/CUDA#GPUs_supported

Compiling on **Linux** by using  <code>make</code> (or alternative way by using <code>cmake . && make</code>)



## Training

You can train on your own data using <code>yolov3-tiny.conv.15</code> 

Pre-trained model: <code>yolov3-tiny-obj_40000.weights</code> (40000 iterations on the training data)



## Data Set

Data sets are included in the <code>img</code> file (labels included) 

There may be some errors for the labels, you can edit them using Yolo_mark: https://github.com/AlexeyAB/Yolo_mark



## Compiling on Linux

Edit <code>Makefile</code> according to your system

* `GPU=1` to build with CUDA to accelerate by using GPU (CUDA should be in `/usr/local/cuda`)
* `CUDNN=1` to build with cuDNN v5-v7 to accelerate training by using GPU (cuDNN should be in `/usr/local/cudnn`)
* `CUDNN_HALF=1` to build for Tensor Cores (on Titan V / Tesla V100 / DGX-2 and later) speedup Detection 3x, Training 2x
* `OPENCV=1` to build with OpenCV 4.x/3.x/2.4.x - allows to detect on video files and video streams from network cameras or web-cams
* `DEBUG=1` to bould debug version of Yolo
* `OPENMP=1` to build with OpenMP support to accelerate Yolo by using multi-core CPU
* `LIBSO=1` to build a library `darknet.so` and binary runable file `uselib` that uses this library. Or you can try to run so `LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./uselib test.mp4` How to use this SO-library from your own code - you can look at C++ example: https://github.com/AlexeyAB/darknet/blob/master/src/yolo_console_dll.cpp
    or use in such a way: `LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./uselib data/coco.names cfg/yolov3.cfg yolov3.weights test.mp4`
* `ZED_CAMERA=1` to build a library with ZED-3D-camera support (should be ZED SDK installed), then run
    `LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./uselib data/coco.names cfg/yolov3.cfg yolov3.weights zed_camera`

*Copied from https://github.com/AlexeyAB/darknet/edit/master/README.md



Pre-trained model was trained on RTX 2080 and was run on Jetson Tx2 

so if you want to run on Tx2 board you should uncomment the <code>ARCH= -gencode arch=compute_53,code=[sm_53,compute_53]</code> and make 

`DataFiles` includes the files needed for training  on the `img` file. 

You may need to edit `obj.data` and `yolo-obj.cfg` according to you system



## Connection to Client (Windows)

In `src/image.c` edit the PORT https://github.com/mnc1423/Yolov3_FireRecognition/blob/master/src/image.c#L30

and IP https://github.com/mnc1423/Yolov3_FireRecognition/blob/master/src/image.c#L31 according to the client  

Run `WindowServer.py`  on windows, run Yolo on Linux and you should get a connection 



## Results

<img width="400" alt="image" src="https://user-images.githubusercontent.com/41675771/65851656-b00cc980-e38e-11e9-8c16-fc1a776a4b9c.PNG">