# [Have I Reached the Intersection: A Deep Learning-based Approach for Intersection Detection from Monocular Cameras](https://ieeexplore.ieee.org/document/8206317)
*by D. Bhatt, D. Sodhi, A. Pal, V. Balasubramanian and M. Krishna*

##### Introduction
- reliable detection of road intersections is an important problem
 in autonomous navigation
- detecting onset of intersection to enable the agent to behave
 more cautiously near intersections
- detecting intersection using only monocular video streams
 (instead of Lidar or other sensor systems)
- mix of Convolutional Neural Networks (spatial understanding)
 and Recurrent Neural Networks (temporal understanding)
- binary classification problem (intersection vs. non-intersection)
    - can be extended to classify intersection types
     (T- vs. X-junction)
- end-to-end trained network

##### Methodology
- Convolutional Neural Network as visual feature extractor
- Recurrent Neural Network with feedback loop, Long Short-Term Memory
 networks to carry long-term dependencies
- the fusion of deep hierarchical visual feature extractor and LSTM
 network enables end-to-end optimization of visual and sequential
 model parameters
- pretrained CNN is a minor variant of AlexNet
- training on Oxford dataset ~6 hrs (2000 epochs), finetuning 1.4 hrs

##### Dataset
- no explicit dataset publicly available
    - 110 intersection & 200 non-intersection sequences extracted
     from Oxford RobotCar dataset
    - 22 intersection & 40 non-intersection sequences extracted from
     Lara traffic-light detection dataset
- flipped all images around vertical axis & added Gaussian noise to
 augment the dataset by a factor of 4
- 1240 sequences (440 intersection / 800 non-intersection) from Oxford
- 248 sequences (88 intersection / 160 non-intersection) from Lara

##### Result
- LRCN better than Single Frame (trained on Lara: 2.5% better,
 trained on Oxford: 5.5% better)
- LRCN trained for intersection classification with ~91.72% accuracy
- finetuning Lara dataset using Oxford subsets significantly boosts
 Accuracy (~13.91% increase)
 