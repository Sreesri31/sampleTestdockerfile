from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([40000, 50000, 60000, 70000, 80000])
model = LinearRegression()
model.fit(X, y)
experience = np.array([[6]])
predicted_salary = model.predict(experience)
print("excuted linear model for creating docker image")
print(f"Predicted salary for 6 years of experience: ₹{predicted_salary[0]:.2f}")

