from base import BaseRepository
from .model import TicketPrice, Ticket
from datetime import datetime
from sqlalchemy import select, and_, cast, Date


class TransportRoutingRepository(BaseRepository):

    async def get_price_for_route(
        self, city_from: int, city_to: int, date: datetime,
        service_class: str,
        limit: int, offset: int
    ):
        date = date.date()
        ticket_price = (
            select(TicketPrice)
            .select_from(TicketPrice)
            .join(Ticket, Ticket.id == TicketPrice.ticket_id, isouter=False)
            .where(
                and_(
                    Ticket.departure_station_id == city_from,
                    Ticket.arrival_station_id == city_to,
                    cast(Ticket.departure_time, Date) == date,
                    Ticket.service_class == service_class
                    )
            ).limit(limit).offset(offset)
        )
        return await self.get_all(ticket_price)
