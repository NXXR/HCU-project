# May Monthly Report

### Contents
- Literature Review
- Project Survey
- Project Scope

### Literature Review
##### [Deep Learning to Detect Objects in Videos from RGB-D Input](http://jderobot.org/Ni9elf-colab)
In the paper the convolutional neural network YOLO (You Only Look Once) is extended and adapted to receive images 
containing color and depth information. The network is end-to-end trained to detect and classify objects, however the
 resulting network is tuned to detect persons in video streams instead of objects. The resulting network and YOLO 
 show significantly faster detection times compared to similar networks (R-CNN and SSD). To adapt to the underlying 
 YOLO network's input layer the depth information is transferred into a colormap and interleaved into the RGB data. 
 Additionally the network identifies objects in the whole image at once, instead of identifying regions of interest and
  only focusing on those, by sectioning the image into a grid and examining each cell in parallel.

##### [LayoutNet: Reconstructing the 3D Room Layout from a Single RGB Image](https://arxiv.org/abs/1803.08999)


##### [Have I Reached the Intersection: A Deep Learning-based Approach for Intersection Detection from Monocular Cameras](https://ieeexplore.ieee.org/document/8206317)


##### [End-to-End Learning of Driving Models with Surround-View Cameras and Route Planners](https://arxiv.org/abs/1803.10158)


##### [End-to-End Navigation with Branch Turning Support Using Convolutional Neural Network](https://www.semanticscholar.org/paper/End-to-End-Navigation-with-Branch-Turning-Support-Seiya-Carballo/b9db6c16504dd3e37fb4d47f140174ef80e7a04e)


##### [Taskonomy: Disentangling Task Transfer Learning](https://arxiv.org/abs/1804.08328)
