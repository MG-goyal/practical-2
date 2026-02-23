import pickle, sys, numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(np.array([[1],[2],[3]]), [2,4,6])
pickle.dump(model, open('model.pkl', 'wb'))

pred = model.predict([[4]])[0]
print(f"Prediction: {pred} | {'PASSED' if abs(pred-8.0)<0.1 else 'FAILED'}")
sys.exit(0 if abs(pred-8.0)<0.1 else 1)