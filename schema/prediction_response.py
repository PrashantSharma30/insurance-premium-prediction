from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category:str
    confidence:float
    class_probabilities:Dict[str,float]
