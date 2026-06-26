# ❤️ Heart Disease Prediction Web App

An end-to-end Machine Learning web application that predicts the likelihood of heart disease based on clinical and medical data. This project uses a trained **Logistic Regression** model and is deployed as an interactive web interface using **Streamlit**.

🔗 **[Link](https://heart-disease-analyzer-cbh4xeraurpw7cjlfsmbfb.streamlit.app/)**

---

## 🚀 Features
- **Interactive UI:** Input medical metrics easily using sliders, dropdowns, and numeric fields.
- **Instant Predictions:** Uses a serialized Python model backend to output instant risk assessments.
- **Clean Layout:** Responsive and accessible web design built with Streamlit components.

---

## 🛠️ Tech Stack
- **Frontend/Deployment:** [Streamlit](https://streamlit.io)
- **Machine Learning Library:** [Scikit-learn](https://scikit-learn.org)
- **Model Serialization:** [Joblib](https://readthedocs.io)
- **Language:** Python 3.13

---

## 📁 Repository Structure
```text
├── app.py                  # Streamlit application user interface & logic
├── logistic_heart.pkl      # Pre-trained Logistic Regression model weights
└── requirements.txt        # Production dependencies for cloud hosting
```

---

## ⚙️ How to Run Locally

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Purva-Maurya/heart-disease-predictor.git
cd heart-disease-predictor
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# On Windows activate with:
venv\Scripts\activate
# On Mac/Linux activate with:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Application
```bash
streamlit run app.py
```
Your browser will automatically open the app at `http://localhost:8501`.

---

## 🌐 Deployment Details
This project is continuously deployed using **Streamlit Community Cloud**. Any changes pushed to the `main` branch of this repository will trigger an automatic rebuilding and updating of the live site.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check out the issues page if you want to propose changes.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
