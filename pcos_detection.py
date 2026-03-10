
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("pcos_dataset.csv")

X = data.drop("pcos_detection", axis=1)
y = data["pcos_detection"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)


print("\nEnter your details:")

age = int(input("Age: "))
bmi = float(input("BMI: "))
periods = int(input("Menstrual irregularities? (1=Yes,0=No): "))
testosterone = float(input("Testosterone level: "))
afc = int(input("Antral follicle count: "))

user_data = [[age, bmi, periods, testosterone, afc]]

prediction = model.predict(user_data)

if prediction[0] == 1:
    print("\n⚠️ High Chances of PCOS Detected.")
    print("\nRecommended Actions:")
    print("- Reduce stress through yoga/meditation")
    print("- Improve sleep (7-8 hours daily)")
    print("- Avoid junk and processed food")
    print("- Exercise at least 30 mins daily")
    print("- Consult a gynecologist for proper diagnosis")
else:
    print("\n✅ Low Chances of PCOS.")
    print("Maintain a healthy lifestyle!")