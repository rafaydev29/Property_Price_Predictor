from sklearn.linear_model import LinearRegression
import numpy as np

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [ 10 ,20,  30,  40,  50,  60,  70,  80,  90, 100]

model = LinearRegression()
model.fit(X, y)

hours = int(input("Enter your studying hours: "))
hours_array = np.array([[hours]]) 

predicted_score = model.predict(hours_array)
print(f"Predicted exam score for {hours} hours: {predicted_score[0]:.2f}")
