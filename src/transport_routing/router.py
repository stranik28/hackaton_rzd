from fastapi import APIRouter, Depends
from .schema import Get_Price, Get_Price_Response, Get_Price_Range, Get_Price_Range_Respones,\
    Get_Price_Range_Response_Factory, Get_Price_Response_Factory
from .model import TicketPrice
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .manager import GetPriceManager
# from email.email import send_notification
import os 
from emails.email import send_notification

router = APIRouter(prefix="/transport_routing", tags=["transport_routing"])

@router.post("/get_price_for_day", response_model=list[Get_Price_Response])
async def get_price(request: Get_Price, session: AsyncSession = Depends(get_async_session),
                    limit: int = 50, offset: int = 0):
    prices: list[TicketPrice] = await GetPriceManager.get_price_for_route(
        request.city_from, request.city_to, request.date, request.service_class,
        session, limit, offset
    )
    if prices != None and len(prices) != 0:
        # Some logic, for now it's so
        send_notification.delay("nplohotn@gmail.com", request.city_from, request.city_to)
    return  Get_Price_Response_Factory.get_prices_respones(prices)
