# Where's Waldo? - CSE 455 Final Project
###### Melissa Birchfield, Jonathan Chen, Michelle Lin

#

# Introduction
Where's Waldo is a series of American puzzle books that challenge readers to search for a single instance of the iconic cartoon character Waldo in a crowded image. As our final project for Computer Vision (CSE 455), our group decided to take on the challenge of creating a neural network to locate Waldo when presented with a image from the original picture books. Our training data for this project primarily comes from a pre-labeled dataset on GitHub compiled by user vc1492a, which includes 19 scenes from the Where's Waldo books and hundreds of cropped image tiles labeled "waldo" or "notwaldo".

While this premise may appear simple or even trivial, there are several factors that make our task complicated than one may initially think. For example, each scene contains multiple red-herring individuals that closely resemble Waldo, sporting a red and white stripped shirt, glasses, or a similar face shape. Additionally, Waldo is almost always partially occluded by another person or object in the scene, meaning our network must not only recognize his face, but other characteristics of Waldo as well. With each Where's Waldo scene containing hundreds of characters, items, and distractions, our neural network needed to be fine-tuned to Waldo's exact likeness, taking into account his clothing, accessories, and color palette, among other factors.

# Dataset

The dataset we used for this was a modified version of one found on [Kaggle](https://www.kaggle.com/residentmario/wheres-waldo). Some images did not include Waldo, some Waldo crops did not center Waldo, and because there were many more non-Waldo than Waldo images. Thus, we made modifications to center Waldo in the crops, replace images without Waldo, and duplicate Waldo images during training to improve generalizability.

# References
The majority of our code was implemented by us, but we referenced several other sources in the process:
* https://towardsdatascience.com/how-to-find-wally-neural-network-eddbb20b0b90 
* https://colab.research.google.com/drive/1kHo8VT-onDxbtS3FM77VImG35h_K_Lav 
* https://colab.research.google.com/drive/1EBz4feoaUvz-o_yeMI27LEQBkvrXNc_4