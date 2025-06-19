import streamlit as st
import pandas as pd
import joblib

# Load saved model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Setup page
st.set_page_config(page_title="Machine Failure Predictor", layout="centered")

# Add animation, CSS, title
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e3f2fd, #fffde7);
        animation: fadeIn 2s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    h1 {
        color: #2E86C1;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .big-font {
        font-size: 20px !important;
        text-align: center;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Welcome message
st.markdown("<h1>🚀 Welcome to Smart Machine Failure Predictor</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="big-font">
Your intelligent assistant to predict machine breakdowns before they happen.<br>
Upload your sensor data and let AI do the magic! 💫
</div>
""", unsafe_allow_html=True)

# Upload file
uploaded_file = st.file_uploader("📂 Upload your sensor data CSV", type=["csv"])

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
        data.columns = data.columns.str.strip()

        st.subheader("📋 Uploaded Data Preview")
        st.dataframe(data.head())

        # Show spinner while processing
        with st.spinner('🔄 Processing your file, please wait...'):
            features = data.drop('Fail', axis=1, errors='ignore')
            scaled = scaler.transform(features)
            preds = model.predict(scaled)
            probs = model.predict_proba(scaled)[:, 1]

            data['Predicted Failure'] = preds
            data['Failure Risk (%)'] = (probs * 100).round(2)

        st.success("✅ Done processing!")

        # Display results
        st.subheader("📊 Prediction Results")
        st.dataframe(data[['Predicted Failure', 'Failure Risk (%)']])

        st.subheader("📈 Failure Risk Chart")
        st.line_chart(data['Failure Risk (%)'])

        high_risk = data[data['Failure Risk (%)'] > 80]
        if not high_risk.empty:
            st.warning(f"⚠️ {len(high_risk)} machines are at HIGH risk of failure!")

    except Exception as e:
        st.error(f"❌ Error while processing: {e}")
else:
    st.info("⬆️ Upload a CSV file to get started.")
