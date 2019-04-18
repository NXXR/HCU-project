# [Deep Learning to Detect Objects in Videos from RGB-D Input](http://jderobot.org/Ni9elf-colab)
*by N. Fernandez, F. Rivas and A. Martin*

- detecting & recognizing objects in videos using RGB + depth data
- additional depth data to increase accuracy

- YOLO (you only look once):
    - regression problem to bounding boxes and class probabilities
        - single neural network for prediction in one evaluation
    - provides 45-150 fps
        - regression problem doesn't require complex pipeline
    - takes whole image into account instead of just proposed regions (R-CNN)
    - tested to be able to learn generalizable representation of objects
    
    1. image is divided into *SxS* grid responsible for detection if center of object within grid
    2. each grid cell predicts *B* bounding boxes + confidence scores
        - confidence score is IoU (Intersection over Union) between ground truth and predicted box, or 0 if no object inside
    
        => each bounding box has 5 values:
        >- relative center of box (x, y)
        >- width & height
        >- confidence score
    3. each grid cell predicts *C* conditional class probabilities (if the cell is containing an object)
    >> The paper uses *S* = 7, *B* = 2
    >
    > => final layer is predicting a 7x7x30 Tensor
    > - 7x7 represents number of grid cells
    > - 30 represents the number of predictions per grid cell
    >   - 10 (2 bounding boxes x 5 predictions each)
    >   - +20 class probabilities ([pascal voc](http://host.robots.ox.ac.uk/pascal/VOC/))

    - more localization errors compared to R-CNN; Issues in localizing small objects
    - multiple small objects in one image grid, due to *B* = 2 => can only detect *B* objects at most
    - loss function treats error in small bounding boxes the same as in large bounding boxes

- R-CNN
    - optimization of CNN by selective search for region proposals instead of sliding window approach
    - detection in 3 parts
        1. Category independent region proposal through selective search
        2. CNN to extract fixed length feature vector for object recognition
        3. class specific linear SVMs (support-vector machines) use the feature vector for object recognition
    - ***slow and hard to optimize due to complex training pipeline (individual components trained separately)***
    - ***no real time performance capabilities (7 fps)*** *(faster variants: Fast R-CNN, Faster R-CNN)*

- SSD (Single Shot MultiBox Detector)
    - simple End-to-End training instead of 3-stage R-CNN
    - ***real time performant (~59 fps)***

- [RGBD Datasets: Past, Present and Future](https://arxiv.org/pdf/1604.00999.pdf) presents a selection of popular RGBD Datasets, some similar to [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
