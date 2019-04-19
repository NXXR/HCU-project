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

    ![F: (S[t−k+1,t], V[t−k+1,t], L[t−k+1,t], I[t−k+1,t], P[t]) → S[t+1] × V[t+1]](https://github.com/NXXR/HCU-project/blob/master/docs/notes/img/EndToEndLearningOfDrivingModels_LearningTask.png "Learning Task")
    - S: Vehicle's Steering angle
    - V: Vehicle's Velocity
    - L: Vehicle's Location
    - I: Surround-View Video
    - P: Planned Route
    - discrete time at sampling rate f => decisions every 1/f seconds
        - t indicates the timestamp
        - t-k is the k. previous sample point => the k recent samples are [t-k+1, t]

**Potential Further Readings:**
- (2018) ***End-to-end driving via conditional imitation learning***. Codevilla, Mueller, Lopez, Koltun, Dosovitskiy
- (2018) ***Event-based vision meets deep learning on steering prediction for self-driving cars***. Maqueda, Loquercio, Gallego, Garcia, Scaramuzza

- (2017) ***Explaining how a deep neural network trained with end-to-end learning steers a car***. Bojarski, Yeres, Choromanska, Choromanski, Firner, Jackel, Muller
- (2017) ***Simultaneous perception and pathgeneration using fully convolutional neural networks***. Caltagirone, Bellone, Svensson, Wahde
- (2017) ***Computer vision for autonomous vehicles: Problems, datasets and state-of-the-art***. Janai, Gueney, Behl, Geiger
- (2017) ***Pathtrack: Fast trajectory annotation with path supervision***. Manen, Gygli, Dai, Van Gool
- (2017) ***Combining neural networks and treesearch for task and motion planning in challenging environments***. Paxton, Raman, Hager, Kobilarov
- (2017) ***Perception, Planning, Control, and Coordination for Autonomous Vehicles***. Pendleton, Andersen, Du, Shen, Meghjani, Eng, Rus, Ang

- (2016) ***Surround vehicles trajectory analysis with recurrent neural networks***. Khosroshahi, Ohn-Bar, Trivedi
- (2016) ***Trajectories and maneuvers of surrounding vehicles with panoramic camera arrays***. Dueholm, Kristoffersen, Satzoda, Moeslund, Trivedi

- (2015) ***Toward personalized, context-aware routing***. Yang, Guo, Ma, Jensen

- (2014) ***3d traffic scene understanding from movable platforms***. Geiger, Lauer, Wojek, Stiller, Urtasun

- (2012) ***Autonomous ground vehicles—concepts and a path to the future***. Luettel, Himmelsbach, Wuensche

- (2011) ***Towards fully autonomous driving: Systems and algorithms***. Levinson, Askeland, Becker, Dolson, Held, Kammel, Kolter, Langer, Pink, Pratt, Sokolsky, Stanek, Stavens, Teichman, Werling, Thrun

- (1948) ***Cognitive maps in rats and men***. Tolman
