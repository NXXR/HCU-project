# [End-to-End Learning of Driving Models with Surround-View Cameras and Route Planners](https://arxiv.org/abs/1803.10158)
*by S. Hecker, D. Dai and L. Van Gool

- Information from all around the vehicle needs to be gathered and integrated to make safe decisions.
- Human drivers us virtual extensions to their limited field of view (side- & rear-view mirrors) and their mental or digital map to make decisions and select a route to their destination.
    - Therefore, mobile robots and autonomous driving need similar systems to support the decision and route planning process.
- Single front-view camera inadequate to learn a safe driving model
- Surround-view camera system, and planned driving route for training,
    - human driver maneuvers as ground-truth.
    - learning task similar to a human apprentice
- End-to-end learning of the driving model: map inputs from surround-view and route planner directly to low-level driving maneuvers
    - tracking for traffic agents & control devices deferred to future work

// 2. Related Work