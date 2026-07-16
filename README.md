# 🎓 Predicting Student Academic Performance using ML



An end-to-end, production-ready Machine Learning system that predicts student grades and academic risk outcomes. Built with a modular data pipeline, this repository handles everything from robust feature engineering to automated model tracking and deployment.

🌐 **Live Demo:** [predicting-student-academic-performance.onrender.com](https://onrender.com)

---

## 🚀 Key Features

*   **End-to-End Pipeline:** Automated data ingestion, robust scaling, categorical encoding, and model artifact generation.
*   **Dual-Mode Target Modeling:** Architected to handle both **Regression** (exact grade prediction) and **Classification** (pass/fail status).
*   **Production Deployment:** Served via a lightweight web application hosted seamlessly on Render.
*   **API Testing Ready:** Pre-configured Postman collections included to quickly test inference endpoints.

---

## 🛠 Tech Stack

*   **Core ML:** Python, Scikit-Learn, Pandas, NumPy, Jupyter Notebooks
*   **API & Web:** Flask / FastAPI, HTML5, CSS3, JavaScript
*   **Mangement & Testing:** Postman (API Globals & Collections)
*   **Environment:** Visual Studio Code, Git, Render Cloud

---

## 📂 Repository Structure

```text
├── .postman/               # Postman environment variables & test collections
├── .vscode/                # Workspace specific configurations
├── artifacts/              # Generated datasets, serialized models (.pkl) & scalars
├── notebooks/              # Jupyter notebooks for EDA and model prototyping
├── src/                    # Production-grade modular source code
│   ├── components/         # Data ingestion, transformation, and model trainer
│   └── pipelines/          # Prediction and training workflows
├── templates/              # HTML UI templates for the web app UI
├── app.py                  # Main web application entry point for inference
├── requirements.txt        # Application dependencies and pinned versions
└── setup.py                # Script to package the project modules
```

---

## ⚙️ Installation & Setup

### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com
cd Predicting-Student-Academic-Performance-using-ML
```

### 2. Create a Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📊 Pipeline Workflow

### 1. Exploratory Data Analysis (EDA)
Comprehensive feature evaluation is conducted inside the `notebooks/` directory to inspect demographic biases, study habits, and attendance correlations.

### 2. Data Transformation
*   Categorical features are mapped using automated pipeline encodings.
*   Numerical values are treated for outliers and normalized using a robust `StandardScaler`.
*   Pipelines are saved securely as serialized artifacts to ensure zero data leakage during real-time inference.

### 3. Model Training & Evaluation
The system runs multiple algorithmic iterations (including Linear Models, Tree Ensembles, and Boosting techniques) evaluating against key performance indicators:
*   **Regression:** $R^2$ Score, MAE, RMSE
*   **Classification:** Accuracy, F1-Score, ROC-AUC

---

## 🖥️ Running the Web App Locally

Launch the Flask/FastAPI server locally using the following command:
```bash
python app.py
```
Once initialized, open your browser and navigate to `http://127.0.0` to interact with the prediction user interface.

### 🧪 API Testing with Postman
Import the configurations stored in the `.postman/` folder directly into your Postman app to execute rapid API payload validations against the prediction endpoints.

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact

**Mohd Zaheeruddin** - [@md_zaheer_jk](https://x.com) - zaheerxaiml@gmail.com  
**Project Link:** [https://github.com](https://github.com)
