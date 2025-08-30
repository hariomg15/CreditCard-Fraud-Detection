🚨 Credit Card Fraud Detection using Machine Learning
📖 Overview

Credit card fraud is a critical financial crime that causes billions of dollars in losses every year.
This project uses Machine Learning algorithms to detect fraudulent credit card transactions based on transaction data.

I have built:
✅ Exploratory Data Analysis (EDA) with visualizations
✅ Feature Engineering & Data Preprocessing
✅ Model Training & Evaluation (Logistic Regression, Random Forest, etc.)
✅ Gradio Web App for easy prediction

📂 Project Structure
CREDIT_CARD_FRAUD/
│
├── creditcard.csv               # Dataset
├── CreditCard_fraud.ipynb        # Jupyter Notebook (EDA + Training)
├── fraud_model.pkl               # Saved trained ML model
├── app.py                        # Gradio web app for predictions
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

📊 Exploratory Data Analysis (EDA)

Some key insights:

Fraud transactions are highly imbalanced compared to normal ones.

Fraudulent transactions usually have lower amounts.

Correlation heatmaps help in feature importance analysis.

🔎 Sample Visualizations

Fraud vs Non-Fraud count plot

Transaction Amount distribution

Correlation Heatmap

Confusion Matrix, ROC Curve, Precision-Recall Curve

⚙️ Installation & Running the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/CreditCard_Fraud_Detection.git
cd CreditCard_Fraud_Detection

2️⃣ Create & Activate Virtual Environment
# Create venv
python -m venv venv

# Activate venv
venv\Scripts\activate        # Windows  
source venv/bin/activate     # Linux/Mac

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Gradio App
python app.py


Then open the local URL from terminal in your browser 🎉

🚀 Deployment Options

You can deploy this app for free on:

🌐 Streamlit Cloud

🤗 HuggingFace Spaces
 (with Gradio)

☁️ Heroku / Render

📈 Model Performance

Accuracy: ~99%

ROC-AUC Score: ~0.97

Precision-Recall Curve shows that the model is effective in catching fraudulent cases.