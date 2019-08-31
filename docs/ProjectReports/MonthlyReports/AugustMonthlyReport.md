# July Monthly Report - CG Dataset and IntersectNet

### Contents
- [CG Dataset](#CG-Dataset)
- [IntersectNet](#IntersectNet)

### CG Dataset
As there are no datasets of solely corridors and intersections that are labeled accordingly, a blender script is 
created to generate CG renders of corridor samples.
The Script has a list of different centerpieces for the different amount of possible connections to 
adjacent corridors. The scene is deemed a corridor, if it has two or less connections, resulting in a straight 
corridor, a corner, or a dead end. If the centerpiece has three or four connections, it is considered an intersection
. Each intersection option has two different layouts, one with soft, and one with hard corners. Additionally the 
centerpiece is rotated randomly in 90°-steps. The script also uses a list of different Textures for floor, ceiling 
and walls to further randomize the scene.

![](../../notes/img/Blender_Schematic_Combined.png)
*Different options for the centerpiece layout*

After the layout is generated, the camera is placed semi randomly:
- for intersections the camera is placed within the intersection at a random rotation angle.
- for corridors the camera is placed either inside the centerpiece or inside an adjacent corridor facing towards the 
intersection with a random variation of ±30°.

![](../../notes/img/Blender_CamSpawnArea.png)
*Boundaries of the random camera position*

Finally the script renders normal an panoramic pictures. During renders of the test set both pictures are rendered 
together, so the test dataset contains the same layout in both perspectives.

![](../../notes/img/Blender_NormalPanoComparison.png)
*Sample of test images: normal prespective on the left, equirectangular perspective on the right; corridor in the top
 row, intersection in the bottom row*

### IntersectNet