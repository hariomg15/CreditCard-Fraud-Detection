import gradio as gr
import joblib
import numpy as np

# Load trained Logistic Regression model
model = joblib.load("fraud_model.pkl")

# Prediction function
def predict_fraud(Time, Amount, *features):
    try:
        # Convert input into numpy array
        input_data = np.array([[Time, Amount] + list(features)])
        
        # Prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        # Result return
        return f"Prediction: {'Fraud' if prediction==1 else 'Not Fraud'} | Fraud Probability: {probability:.2f}"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Define inputs (Time, Amount, V1...V28)
inputs = [gr.Number(label="Time"), gr.Number(label="Amount")] + [
    gr.Number(label=f"V{i}") for i in range(1, 29)
]

# Output
output = gr.Textbox(label="Result")

# Gradio App
app = gr.Interface(
    fn=predict_fraud,
    inputs=inputs,
    outputs=output,
    title="Credit Card Fraud Detection",
    description="Enter transaction details (Time, Amount, V1...V28) to check if it's Fraud or Not."
)

if __name__ == "__main__":
    app.launch()
