# [JdeRobot: Ni9elf-colab](http://jderobot.org/Ni9elf-colab)

- detecting & recognizing objects in videos using RGB + depth data
- additional depth data to increase accuracy
- YOLO (you only look once):
    - regression problem to bounding boxes and class probabilities
        - single neural network for prediction in one evaluation
    - provides 45-150 fps
        - regression problem doesn't require complex pipeline
    - takes whole image into account instead of just proposed regions (R-CNN)
    - tested to be able to learn generalizable representation of objects