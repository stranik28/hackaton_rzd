from .model import TicketPrice
from .repository import TransportRoutingRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime

class GetPriceManager():

    @classmethod
    async def get_price_for_route(self,
        city_from: int, city_to: int, date: datetime,
        service_class: str, session: AsyncSession,
        limit: int, offset: int
    ):
        return await TransportRoutingRepository(session).get_price_for_route(
            city_from, city_to, date, service_class, limit, offset
        )

    
