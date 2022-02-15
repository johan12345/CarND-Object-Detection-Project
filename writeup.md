### Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

### Set up
This project uses the dependencies as provided in the starter code, i.e. you can use the Dockerfile at
`build/Dockerfile` to run the project.

### Dataset
#### Dataset analysis
The exploratory data analysis was performed in the notebook `Exploratory Data Analysis.ipynb`, and yielded the following
findings:

- Images have a fixed square size of 640x640. The image contents look slightly squished, so they may have originally 
  been taken in a 4:3 or 16:9 aspect ratio.
- Objects are labeled with three classes: vehicle (1), pedestrian (2) and cyclist (4)
- One `.tfrecord` file seems to contain a single continuous recording, i.e. images from a single file show very similar
  road conditions
- Between different recordings, the conditions vary a lot:
  - There are both day- and nighttime recordings (though daytime seems to be more common)
  - Weather includes challenging conditions such as rain (with drops on the camera lens) and fog
  - Data includes different kinds of roads: city streets, highways, narrow driveways, etc.
  - Images seem to be taken by a forward-facing camera
- Labels are also included when the objects are very small (far away) or partially occluded
- Vehicles are by far the most common class, cyclists are pretty rare
- The dataset includes some negative examples (i.e., images with no labels at all) 

![Examples of images in the dataset](resources/examples.png)

#### Cross validation
The dataset is split into training, validation and test sets with a 60/20/20 split.
As mentioned above, each file contains a continuous recording. Therefore, splitting is done inbetween files to make sure
that the model generalizes to unseen recordings with different road conditions.

### Training
#### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.004
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.010
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.004
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.091
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.012
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.029
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.004
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.071
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.368

#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.

##### 1. add data augmentations

 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.011
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.004
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.007
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.057
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.006
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.014
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.034
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.009
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.064
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.467