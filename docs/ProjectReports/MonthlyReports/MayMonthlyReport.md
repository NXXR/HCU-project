# May Monthly Report - Project Survey

### Contents
- [Literature Review](#Literature-Review)
    - [Deep Learning to Detect Objects in Videos from RGB-D Input](#Deep-Learning-to-Detect-Objects-in-Videos-from-RGB-D-Input)
    - [LayoutNet: Reconstructing the 3D Room Layout from a Single RGB Image](#LayoutNet:-Reconstructing-the-3D-Room-Layout-from-a-Single-RGB-Image)
    - [Have I Reached the Intersection: A Deep Learning-based Approach for Intersection Detection from Monocular Cameras](#Have-I-Reached-the-Intersection:-A-Deep-Learning-based-Approach-for-Intersection-Detection-from-Monocular-Cameras)
    - [End-to-End Learning of Driving Models with Surround-View Cameras and Route Planners](#End-to-End-Learning-of-Driving-Models-with-Surround-View-Cameras-and-Route-Planners)
    - [Taskonomy: Disentangling Task Transfer Learning](#Taskonomy:-Disentangling-Task-Transfer-Learning)
- [Project Scope](#Project-Scope)
    - [Comparison to Similar Projects from the Literature Review](#Comparison-to-Similar-Projects-from-the-Literature-Review)

### Literature Review

##### [Deep Learning to Detect Objects in Videos from RGB-D Input](http://jderobot.org/Ni9elf-colab)
In the project, the convolutional neural network YOLO (You Only Look Once) is extended and adapted to receive images 
containing color and depth information. The network is end-to-end trained to detect and classify objects, however the 
resulting network is tuned to detect persons in video streams instead of objects. The resulting network and YOLO both 
show significantly faster detection times compared to similar networks (R-CNN and SSD). To adapt to the underlying 
YOLO network's input layer, the depth information is transferred into a colormap and interleaved into the RGB data. 
Additionally the network identifies objects in the whole image at once, instead of identifying regions of interest and 
only focusing on those, by sectioning the image into a grid and examining each cell in parallel.

##### [LayoutNet: Reconstructing the 3D Room Layout from a Single RGB Image](https://arxiv.org/abs/1803.08999)
LayoutNet is a network trained to extract the 3D room layout from surround view images. it operates using a three 
step approach:
First the surround view image is projected into 2D equirectangular space and aligned to the floor 
plane so that wall-to-wall boundaries become vertical lines in the image. Additionally, the first step 
detects long sine segments for possible wall-to-floor/ceiling boundaries and determines three mutually orthogonal 
vanishing points to establish a coordinate system for the room layout.
In the second step the results from the first step are used to create a corner and boundary probability map directly 
on top of the original image, representing determined locations of corners and lines along the determined 
wall-to-wall, wall-to-floor and wall-to-ceiling boundaries.
Finally, the parameters of the 3D layout are optimized to fit the predicted corners and boundaries of the generated 
corner and boundary maps.
The network is structured into 3 subsystems which are trained separately:
A deep panorama encoder is used to extract a 6-channel feature map as well as a Manhattan line feature map from the 
surround view image.
A 2D layout decoder trained to predict 2D feature maps of boundary predictions and corner predictions from 7 layers of 
nearest neighbor up-sampling.
A 3D layout regressor to find and optimize 3D layout parameters from 2D corners and boundaries. Optimization is done 
by sampling ~1000 layout candidates by shifting boundary position within ±10% and determining the best candidate 
based on a score function. The sampling takes less than 30 s per image.
While the sampling is too intensive for real time applications, the network performs better or equal to current 
state-of-the-art networks.

##### [Have I Reached the Intersection: A Deep Learning-based Approach for Intersection Detection from Monocular Cameras](https://ieeexplore.ieee.org/document/8206317)
IntersectNet is a end-to-end trained, Long-Term Recurrent Convolutional Network (LRCN), a mix of a Convolutional 
Neural Network (CNN) for spacial understanding and a Recurrent Neural Network (RNN) for temporal understanding. It 
aims to classify  video sequences into intersection and non-intersection sequences, as well as classify the 
intersection into T- and X-junctions. The convolutional neural network acts as a visual feature extractor, while the 
recurrent neural network serves to carry long-term dependencies. The resulting network was trained on ~1488 
sequences extracted and augmented from Oxford RobotCar and Lara traffic-light detection datasets. The temporal 
component leads to a significant improvement (2.5-5.5% improvement) compared to single frame networks without a 
Recurrent Neural Network component.

##### [End-to-End Learning of Driving Models with Surround-View Cameras and Route Planners](https://arxiv.org/abs/1803.10158)
This paper proposes features to improve autonomous driving by incorporating surround view video stream and route 
planning information to and end-to-end driving model. The surround view video is generated from two sets or four 
cameras arranged in 90 degree angles, and the route planning data is either a stack of GPS pins from OpenStreetMap or 
a visual image stream from a TomTom navigational device. The driving model consists of multiple convolutional neural 
networks for feature encoding, as well as four long short-term memory networks for temporal encoding, and 
fully-connected networks to fuse input information and predict steering angle and speed for 0.3 seconds into the 
future. The steering angle and speed are rather easy for the network to predict, as the input data does not change 
significantly in the prediction range. The paper also mentions relying on the past as ground truth may be dangerous, 
as past driving states may not be correct. To avoid this, the network is trained without ground truth input, so the 
network solely relies on input data of the route planner and the road situation. However the paper proves that 
incorporation of surround view cameras and a route planning component are highly beneficial, especially on low speed 
environments without traffic control agents.

##### [End-to-End Navigation with Branch Turning Support Using Convolutional Neural Network](https://www.semanticscholar.org/paper/End-to-End-Navigation-with-Branch-Turning-Support-Seiya-Carballo/b9db6c16504dd3e37fb4d47f140174ef80e7a04e)
The project focused on end-to-end training a network to detect intersections and followed assigned trajectories 
through the intersection. Initial training along a predetermined path resulted in a model for each trajectory, 
however later implementations were trained to follow and unknown trajectory by introducing a vector to the next 
target after the convolutional layers of the feature encoder. Additionally the system is able to handle complex 
trajectories with multiple branching options and a pure pursuit sub algorithm to return to the predicted trajectory 
upon deviation. This way the network learned to navigate locally based on the target direction vector. 

##### [Taskonomy: Disentangling Task Transfer Learning](https://arxiv.org/abs/1804.08328)
Taskonomy is a meta-learning project that seeks to find the complex mapping between different tasks. This way 
relationships between learning tasks can be used to avoid minute and expensive isolated training. Additionally, the 
successively more abstract representations can be used for multiple related outputs.
Based on source and target tasks a hypergraph in created to visualize task learning transferability, which can be 
used to estimate an optimal transfer policy.

### Project Scope
Initially the project aims to gain an understanding of basic machine learning systems in conjunction with computer 
vision. Furthermore the goal is to create a neural network that is capable to identify junctions in indoor corridors 
from images obtained by a surround view camera. Once a suitable network to recognize corridors and junctions is in 
place, an end-to-end driving model is planned to be trained to navigate a mobile robot unobstucted along the corridors. 
Depending on the progress, a route planning system is planned to be implemented to allow navigation to set waypoints.
An optional goal is to implement an object detection system to identify additional, sometimes moving, obstacles and 
targets that are fed to the route planner to be inserted into the currently planned path of the mobile robot.

##### Comparison to Similar Projects from the Literature Review
| Feature                      | HCU Project | End-to-End Navigation | End-to-End Learning of Driving Models | 
| :--------------------------- | :---------: | :-------------------: | :-----------------------------------: |
| ***Single Sensor System***   | O           | X                     | X                                     |
| ***Path Detection***         | O           | O (Lidar)             | O
| *Route Planning*             | O           | junction trajectories | external system (GPS)                 |
| *Obstacle Detection*         | O           | X                     | O                                     |

While both projects from the literature employ end-to-end driving models, they both differ significantly to this 
projects as neither relies on a single sensor for input, the Navigation Project uses a frontal camera paired with 
Lidar to map and detect the corridor layout, while the Driving model in the other project relies on a multi-camera 
surround view setup paired with a route planning system, as the driving model is constructed for road vehicles.
All projects use path detection is some form, however the route planning through the detected environment is in the 
Navigation projects case realized in given instructions for singular junction trajectories, similar to the planned 
system for this project, and the Driving model in the other project uses an external system for the planned route.
