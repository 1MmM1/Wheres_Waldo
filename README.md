# Where's Waldo?

Created by Melissa Birchfield, Jonathan Chen, and Michelle Lin

## Introduction
Where's Waldo is a series of American puzzle books that challenge readers to search for a single instance of the iconic cartoon character Waldo in a crowded image. As our final project for Computer Vision (CSE 455), our group decided to take on the challenge of creating a neural network to locate Waldo when presented with a image from the original picture books. Our training data for this project primarily comes from a pre-labeled dataset on GitHub compiled by user vc1492a, which includes 19 scenes from the Where's Waldo books and hundreds of cropped image tiles labeled "waldo" or "notwaldo".

While this premise may appear simple or even trivial, there are several factors that make our task complicated than one may initially think. For example, each scene contains multiple red-herring individuals that closely resemble Waldo, sporting a red and white stripped shirt, glasses, or a similar face shape. Additionally, Waldo is almost always partially occluded by another person or object in the scene, meaning our network must not only recognize his face, but other characteristics of Waldo as well. With each Where's Waldo scene containing hundreds of characters, items, and distractions, our neural network needed to be fine-tuned to Waldo's exact likeness, taking into account his clothing, accessories, and color palette, among other factors.

More details about our process can be found on our [website](https://sites.google.com/cs.washington.edu/cse455findingwaldo/home).

## Dataset

The dataset we used for this was a modified version of one found on [Kaggle](https://www.kaggle.com/residentmario/wheres-waldo). Some images did not include Waldo, some Waldo crops did not center Waldo, and because there were many more non-Waldo than Waldo images. Thus, we made modifications to center Waldo in the crops, replace images without Waldo, and duplicate Waldo images during training to improve generalizability.

## Usage

In our Python Notebook, `find_waldo.ipynb`, we have implemented a pipeline which trains a model to find Waldo, and uses that model on an unseen image to highlight areas of Waldo in that image. `find_waldo.ipynb` also includes code to create data splits (train, validation, and test) using a 64:16:20 split, load the data, and train a model from scratch and assumes you are working on Google Colab. The code should work for any folder structure as long as you make sure `BASE_PATH` is set to the correct folder in your Google Drive and the demo image location is set correctly under the "Run model on an unseen image" subsection. Running this notebook should produce model checkpoints and an image with the model's predicted Waldo tiles highlighted.

## References
The majority of our code was implemented by us, but we referenced several other sources in the process:
* https://towardsdatascience.com/how-to-find-wally-neural-network-eddbb20b0b90 
* https://towardsdatascience.com/beginners-guide-to-loading-image-data-with-pytorch-289c60b7afec
* https://courses.cs.washington.edu/courses/cse455/21sp/