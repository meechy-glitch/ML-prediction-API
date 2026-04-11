from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import joblib
import os


iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_pred, y_test, target_names=iris.target_names))


os.makedirs("ml", exist_ok=True)
joblib.dump(model, "ml/model.joblib")
print("Model saved to joblib")


#loaded_model = joblib.load("ml/model.joblib")
#sample = [[5.1, 3.5, 1.4, 0.2]]
#prediction = loaded_model.predict(sample)
#print(f"sample prediction: {iris.target_names[prediction[0]]}")