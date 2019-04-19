# [End-to-End Learning of Driving Models with Surround-View Cameras and Route Planners](https://arxiv.org/abs/1803.10158)
*by S. Hecker, D. Dai and L. Van Gool*

- Information from all around the vehicle needs to be gathered and integrated to make safe decisions.
- Human drivers us virtual extensions to their limited field of view (side- & rear-view mirrors) and their mental or digital map to make decisions and select a route to their destination.
    - Therefore, mobile robots and autonomous driving need similar systems to support the decision and route planning process.
- Single front-view camera inadequate to learn a safe driving model
- Surround-view camera system, and planned driving route for training,
    - human driver maneuvers as ground-truth.
    - learning task similar to a human apprentice
- End-to-end learning of the driving model: map inputs from surround-view and route planner directly to low-level driving maneuvers
    - tracking for traffic agents & control devices deferred to future work

- Driving Models for Automated Cars:
    1. Mediated Perception
        - recognition of all driving relevant objects (lanes, traffic signs, traffic lights, cars, pedestrians, etc.)
        - realized by diverse sensors (i.e. cameras, laser sensors, radar, GPS and HD maps)
        - current state-of-the-art for autonomous driving
    2. End-to-End Mapping
        - direct mapping from ssensory input to maneuvers
            - 1980s: enural network to learn direct mapping from images to steering angle

- Driving Scene Understanding
    - detection and tracking of moving objects elaborated in other sources (72, 44, 55, 39, 61)

- Sensors used:
    - Cameras
        - double coverage of surround view
        - 4 cameras mounted in 90 deg angles (0, 90, 180, 270)
        - 4 cameras mounted in 45 deg to the first set (45, 135, 225, 315)
    - Route Planners
        - not much attention to integration of route planners with autonomous drive learning
        - OpenStreetMaps geodata used for route planning (and TomTom Map, albeit not public => workaround screen capture off iPhone 7)
        - past driving  trajectories (stack of GPS coordinates) and GPS tags of the next 300 meters ahead taken as representation of planned route and current position
    - Human Driving Input
        - steering wheel angle, vehicle speed via CAN bus
        - odometry via cameras (GoPro) GPS and IMU module

- Driving Model Learning Task:
    - ![F: (S[t−k+1,t], V[t−k+1,t], L[t−k+1,t], I[t−k+1,t], P[t]) → S[t+1] × V[t+1]](https://github.com/NXXR/HCU-project/blob/master/docs/notes/img/EndToEndLearningOfDrivingModels_LearningTask.png "Learning Task")
    

**Potential Further Readings:**
- (10) Bojarski, M., Yeres, P., Choromanska, A., Choromanski, K., Firner, B., Jackel, L.D., Muller,U.: ***Explaining how a deep neural network trained with end-to-end learning steers a car***. CoRR (2017)
- (12) Caltagirone, L., Bellone, M., Svensson, L., Wahde, M.: ***Simultaneous perception and pathgeneration using fully convolutional neural networks***. arXiv preprint arXiv:1703.08987(2017)
- (62) Paxton, C., Raman, V., Hager, G.D., Kobilarov, M.: ***Combining neural networks and treesearch for task and motion planning in challenging environments***. In: IROS (2017)
- (63) Pendleton, S.D., Andersen, H., Du, X., Shen, X., Meghjani, M., Eng, Y.H., Rus, D., Ang,M.H.: ***Perception, Planning, Control, and Coordination for Autonomous Vehicles***. Machines5(1) (2017)
