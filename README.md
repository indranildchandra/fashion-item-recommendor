# Overview
For each user of the client's e-commerce website, predict 10 relevant items from the items protfolio that the user may be interested in and hence help in increasing client's engagement with the users.

##Problem Statement
Capillary would like to welcome you to build a recommender system for its top fashion retail client to increase the client's user engagement. The main goal is to come up with an algorithm which will recommend best suited items from the inventory to a user in order to improve his/her shopping experience. On the basis of user transaction history, collaborative information and item features, recommend the ranked top 10 items for a user which means that the participant has to rank the recommendations for any user in the order of choice.
 
As part of this challenge, you are provided a retail brand dataset with user transaction details, item tagged fashion images, item attributes and other metadata.

##Data Dictionary
1. Train.zip contains the following:

•	train.csv
training data contains transaction history of 27778 users for 7 months (April - October)
  
Variable	Description
UserId		Unique ID for user
productid	Unique ID for product
Quantity	Quantity of product bought
OrderDate	Timestamp of transaction
 
•	product_attributes.csv
 
Variable		Description
productid		Unique ID for product
attribute_name	Name of attribute (fit/sleeve/Fabric….)
attributevalue	Anonymised Attribute Value (unordered)
 
•	Images Folder
Contains the images corresponding to all items with the format <productid>.jpg
 
2. test.csv
The test data contains the user list for which the participant is supposed to come up with the best recommendations (maximum 10). These users represent a subset of users from the train data who made atleast 1 transaction in the 2 months following the last transaction in the train set.
Variable	Description
UserId	Unique ID for user
 
##Evaluation Metric
The evaluation metric for this contest is Mean Average Precision at K  - MAP@K (K = 10)



# Predictor Scripts

1. alternating_least_squares_predictor.py: collaborative filtering based recommendation script


# Helper Scripts

For image embedding generation following scripts will be useful -

1. image_reader_converter.py : Created input dataset from given images , suitable to feed to autoencoder for embedding generation

2. autoencoder_training.py: Training script of autoencoder. saves the model

3. fashion_item_recommendor_autoencoder.86-479.35.h5 : Basic autoencoder model based on the script autoencoder_training.py (can be tuned further)

4. final_inferencing_features.py : inferencing script, loads the autoencoder model and generates 128 length vector for each image
