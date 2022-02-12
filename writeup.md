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
- The dataset includes some negative examples (images with no labels at all) 

![Examples of images in the dataset](resources/examples.png)

#### Cross validation
This section should detail the cross validation strategy and justify your approach.

### Training
#### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
