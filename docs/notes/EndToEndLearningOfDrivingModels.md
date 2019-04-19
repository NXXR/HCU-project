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

**Potential Further Readings:**
- (10) Bojarski, M., Yeres, P., Choromanska, A., Choromanski, K., Firner, B., Jackel, L.D., Muller,U.: ***Explaining how a deep neural network trained with end-to-end learning steers a car***. CoRR (2017)
- (12) Caltagirone, L., Bellone, M., Svensson, L., Wahde, M.: ***Simultaneous perception and pathgeneration using fully convolutional neural networks***. arXiv preprint arXiv:1703.08987(2017)
- (62) Paxton, C., Raman, V., Hager, G.D., Kobilarov, M.: ***Combining neural networks and treesearch for task and motion planning in challenging environments***. In: IROS (2017)
- (63) Pendleton, S.D., Andersen, H., Du, X., Shen, X., Meghjani, M., Eng, Y.H., Rus, D., Ang,M.H.: ***Perception, Planning, Control, and Coordination for Autonomous Vehicles***. Machines5(1) (2017)
77 22 21 56 58 35 74 54 76 47 50 31 64 77 35 28 42 82 6 83 16 78 39 61