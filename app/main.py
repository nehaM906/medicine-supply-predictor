from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model and feature columns
with open('app/models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('app/models/feature_cols.pkl', 'rb') as f:
    feature_cols = pickle.load(f)

# Create FastAPI app
app = FastAPI(title="Medicine Supply Predictor API")

# Define input data structure
class DrugInput(BaseModel):
    production_drop_3m: float
    import_dependency: float
    demand_surge: int
    days_since_last_shortage: float
    manufacturer_shortage_history: float
    price_increase_pct: float

# Home route
@app.get("/")
def home():
    return {"message": "Medicine Supply Predictor API is running!"}

# Prediction route
@app.post("/predict")
def predict(drug: DrugInput):
    # Convert input to array
    data = np.array([[
        drug.production_drop_3m,
        drug.import_dependency,
        drug.demand_surge,
        drug.days_since_last_shortage,
        drug.manufacturer_shortage_history,
        drug.price_increase_pct
    ]])
    
    # Make prediction
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]
    
    # Return result
    result = "At Risk" if prediction == 1 else "Not At Risk"
    confidence = round(float(max(probability)) * 100, 2)
    
    return {
        "prediction": result,
        "confidence": f"{confidence}%",
        "risk_score": int(prediction)
    }