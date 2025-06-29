# ⚙️ Smart Machine Failure Prediction App

This project is a **machine learning-powered web application** designed to **predict failure risks in industrial machines** based on real-time sensor data.

Built as a capstone project by **Subhojit**, it combines ML + UI + deployment to showcase a full end-to-end solution.

---

## 🚀 Features

- 📂 Upload your own sensor CSV data
- 🧠 Predict machine failures using a trained model
- 📊 View failure risks as a percentage
- 📈 See risk trends in an interactive chart
- 📥 Download predictions as CSV
- 🌐 Fully deployed & mobile responsive (Streamlit Cloud)

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Classifier (customizable)
- **Input Features**:  
  `Footfall`, `Temperature`, `VOC`, `RP`, `IP`, `CS`, `USS`, `AQ`, `Temp Mode`, etc.  
- **Target**: `Fail` (0 = working, 1 = failure)

Trained using historical sensor logs and evaluated on unseen test sets.

---

## 🛠️ Tech Stack

| Tool        | Purpose                  |
|-------------|---------------------------|
| Python      | Core programming          |
| Streamlit   | Front-end web interface   |
| scikit-learn| ML model training         |
| Joblib      | Saving/loading model      |
| GitHub      | Code hosting              |
| Streamlit Cloud | Free public deployment |

---

## 📁 Repository Structure

