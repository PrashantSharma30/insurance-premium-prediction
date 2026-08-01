from fastapi import FastAPI
from schema.user_input import UserInput
from model.predict import predict_output
from schema.prediction_response import PredictionResponse

app = FastAPI(
    title="Insurance Premium Prediction API",
    description="Predict insurance premium category",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Insurance Premium Prediction API is running"
    }

@app.get('/health')
def health_check():
    return{
        'status':'OK'
    }

@app.post("/predict",response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input ={
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }

    prediction = predict_output(user_input)
    
    return prediction