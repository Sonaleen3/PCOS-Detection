# PCOS-Detection
# PCOS Detection using Machine Learning

A simple Machine Learning project that predicts the likelihood of **Polycystic Ovary Syndrome (PCOS)** using patient health data such as age, BMI, menstrual irregularities, hormone levels, and antral follicle count.

The project uses **Logistic Regression** to classify whether a person may have a high or low chance of PCOS.

---

## 📌 Project Overview

Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder affecting women of reproductive age. Early detection can help in better management and treatment.

This project builds a **Machine Learning model** that:

* Trains on a PCOS dataset
* Predicts PCOS risk
* Provides lifestyle recommendations based on the prediction

---

## ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Machine Learning (Logistic Regression)

---

## 📂 Project Structure

```
pcos-detection-ml/
│
├── pcos_dataset.csv        # Dataset used for training
├── pcos_model.py           # Main Python script
├── README.md               # Project documentation
```

---

## 📊 Features Used in Model

The model uses the following health parameters:

* Age
* BMI (Body Mass Index)
* Menstrual Irregularities
* Testosterone Level
* Antral Follicle Count (AFC)

Target variable:

```
pcos_detection
0 → No PCOS
1 → PCOS Detected
```

---

## 🧠 Machine Learning Model

The project uses **Logistic Regression**, a supervised learning algorithm used for binary classification problems.

Workflow:

1. Load dataset
2. Split dataset into training and testing sets
3. Train Logistic Regression model
4. Evaluate model accuracy
5. Predict PCOS risk based on user input

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/pcos-detection-ml.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd pcos-detection-ml
```

### 3️⃣ Install Required Libraries

```bash
pip install pandas scikit-learn
```

### 4️⃣ Run the Python Script

```bash
python pcos_model.py
```

---

## 💻 Example Input

```
Enter your details:

Age: 24
BMI: 27
Menstrual irregularities? (1=Yes,0=No): 1
Testosterone level: 0.8
Antral follicle count: 12
```

---

## 📈 Example Output

```
Model Accuracy: 0.87

⚠️ High Chances of PCOS Detected.

Recommended Actions:
- Reduce stress through yoga/meditation
- Improve sleep (7–8 hours daily)
- Avoid junk and processed food
- Exercise at least 30 minutes daily
- Consult a gynecologist
```

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.
It does **not replace professional medical diagnosis**. Always consult a qualified healthcare professional for medical advice.

---


