from pydantic import BaseModel, Field
from datetime import datetime
from .model import TicketPrice

class Get_Price(BaseModel):
    city_from: int = Field(..., example=1)
    city_to: int = Field(..., example=2)
    date: datetime = Field(..., example="2021-01-01T00:00:00")
    service_class: str = Field(..., example="economy")

class Get_Price_Response(BaseModel):
    ticket_id: int = Field(..., example=1)
    date: datetime = Field(..., example="2021-01-01T00:00:00")
    price: float = Field(..., example=100.0)

class Get_Price_Response_Factory():
    @staticmethod
    def get_price_respones(ticket_id: int, departure_time: datetime, price: float) -> Get_Price_Response:
        return Get_Price_Response(ticket_id=ticket_id, date=departure_time, price=price)
    
    @classmethod
    def get_prices_respones(cls, tickets=list[TicketPrice]) -> list[Get_Price_Response]:
        return [
            cls.get_price_respones(ticket_id=price.ticket_id,departure_time=price.date ,price=price.price)
            for price in tickets
            ]
    
class Get_Price_Range(BaseModel):
    day_start_from: datetime = Field(..., example="2021-01-01T00:00:00")
    day_start_to: datetime = Field(..., example="2021-01-01T00:00:00")
    day_end_from: datetime = Field(..., example="2021-01-01T00:00:00")
    day_end_to: datetime = Field(..., example="2021-01-01T00:00:00")
    number_of_days_from: int = Field(..., example=1)
    number_of_days_to: int = Field(..., example=1)
    city_from: int = Field(..., example=1)
    city_to: int = Field(..., example=2)

class Get_Price_Range_Respones(BaseModel):
    day_from: datetime = Field(..., example="2021-01-01T00:00:00")
    day_to: datetime = Field(..., example="2021-01-01T00:00:00")
    price: float = Field(..., example=100.0)

class Get_Price_Range_Response_Factory():
    @staticmethod
    def get_price_respones(cls, day_from: datetime, day_to: datetime, price: float) -> Get_Price_Range_Respones:
        return Get_Price_Range_Respones(day_from=day_from, day_to=day_to, price=price)

    @classmethod
    def get_prices_respones(cls, tickets=list[TicketPrice]) -> list[Get_Price_Range_Respones]:
        return [cls.get_price_respones(price.day_from, price.day_to, price.price) for price in tickets]