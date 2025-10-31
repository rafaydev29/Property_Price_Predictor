from sklearn.linear_model import LinearRegression
import numpy as np
import time

X = [[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000],]
y = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]

model = LinearRegression()
model.fit(X, y)

area = int(input("Enter your area per of your property: "))
area_array = np.array([[area]]) 

predicted_score = model.predict(area_array)
time.sleep(2)
print("analyzing data...")
time.sleep(2)
print("matching pattern...")
time.sleep(2)
print("predicting price...")
time.sleep(2)
print(f"Predicted price for {area} price: {predicted_score[0]:.2f}")
