from pydantic import BaseModel, Field
from datetime import datetime

class PredictRequest(BaseModel):
    city_from: int = Field(..., example=1)
    city_to: int = Field(..., example=2)
    date_from: datetime = Field(..., example="2021-01-01T00:00:00")
    service_class: str = Field(..., example="economy")

class PredictResponse(BaseModel):
    price: float = Field(..., example=100.0)

class PredictResponseFactory():
    @classmethod
    def predict_from_price(cls, price: float) -> PredictResponse:
        return PredictResponse(price=price)