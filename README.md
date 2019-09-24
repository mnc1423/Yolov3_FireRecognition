# Yolov3_FireRecognition
implementation of Yolo_v3 for fire recognition

Original repository https://github.com/AlexeyAB/darknet

Training Weights: yolov3-tiny.conv.15 (Yolo-tiny weights) 

Pretrained Weights: yolov3-tiny-obj_40000.weights 

Model is made to run on a Jetson TX2 board: https://developer.nvidia.com/embedded/jetson-tx2

change MakeFile to run on different environments



## Requirements

Built in Linux environment (check original repository for Windows version)

* **OpenCV** >= 2.4 (For Jetson Tx2 board Used 3.4.0)
* **CUDA** == 9.0 (CUDA 10.0 is supported in original repository)
* **cuDNN** == 7.6.3
* **GPU** with **CC**: https://en.wikipedia.org/wiki/CUDA#GPUs_supported

