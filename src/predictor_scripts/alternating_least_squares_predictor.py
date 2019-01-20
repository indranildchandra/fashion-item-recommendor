# Alternating Least Squares -> collaborative filtering based recommendation script

import scipy.sparse as sparse
import pandas as pd
import implicit
import csv
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

# Load the data
raw_data = pd.read_csv("./../../data/training_dataset/train.csv")[['UserId','productid','Quantity']]
test_data = pd.read_csv("./../../data/testing_dataset/test.csv")

# Drop NaN columns
data = raw_data.dropna()
data = data.copy()

sparse_item_user = sparse.csr_matrix((data['Quantity'].astype(float), (data['productid'], data['UserId'])))
sparse_user_item = sparse.csr_matrix((data['Quantity'].astype(float), (data['UserId'], data['productid'])))

# Initialize the als model and fit it using the sparse item-user matrix
model = implicit.als.AlternatingLeastSquares(factors=70, regularization=0.6, iterations=20)

# Calculate the confidence by multiplying it by alpha value.
alpha_val = 10
data_conf = (sparse_item_user * alpha_val).astype('double')

# Fit the model
print("Training ALS model...")
model.fit(data_conf)

# Create recommendations for all users
fields=['UserId','product_list']
filename = './../../data/submission/results_als.csv'
with open(filename,'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    userids = test_data['UserId'].drop_duplicates().values.tolist()
    for user in userids:
        products = []
        scores = []
        results = []
        results.append(user)
        recommended = model.recommend(user, sparse_user_item)

        for item in recommended:
            idx, score = item
            products.append(idx)
            scores.append(score)
        results.append(products)
        print("UserID : " + user)
        print("Recommeneded Products : " + products)
        print("Scores : " + scores)
        writer.writerow(results)