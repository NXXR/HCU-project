# [LayoutNet: Reconstructing the 3D Room Layout from a Single RGB Image](https://arxiv.org/abs/1803.08999)
*by C. Zou, A. Colburn,Q. Shan, and D. Hoiem*

##### Introduction
- Layout representable as a set of projectted corner positions/boundaries (3D Mesh)
- among the best for perspective images (panoramic) and comparable in speed
- 3 step approach
    1. analyzing vanishing points & alignment w/ floor (wall-wall-boundaries become vertical lines)
    2. corner (layout junctions) and boundary probability map predicted directly on image (CNN w/ encoder-decoder structure)
    3. 3D layout parameters are optimized to fit predicted corners and boundaries

##### Approach
- Panoramic image alignment
    - estimating floor plane under spherical projection
    - reprojection into 2D equirectangular
    - detection of long line segments in overlapped perspective view
    - vote for three mutually orthogonal vanishing directions
- Network structure
    - Deep panorama encoder
        - 6-channel feature map (concatenation of single RGB 512x1024 panorama image)
        - Manhattan line feature map
    - 2D layout decoder
        - 2D feature map
            - boundary prediction through 7 layers of nearest neighbor up-sampling
        - 2D corner map
    - 3D layout regressor
        - 2D corners & boundaries → 3D layout parameters mapping mathematically simple but difficult to learn
        - regressor to produce better corners & boundaries
        - 6 parameters (ground plane aligned to x-z-axis):
            - s_w: width
            - s_l: length
            - s_h: height
            - T = (t_x, t_z): translation
            - r_0: rotation on x-z-plane
    - loss function
        ![Loss Function]()