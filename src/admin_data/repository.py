from base import BaseRepository
from .schema import CreateStation, CreateRoute, CreateRouteStation, CreateTrain, CreateTicket, CreateTicketPrice
from transport_routing.model import Station, Route, RouteStation, Train, Ticket, TicketPrice
from sqlalchemy import select

class AdminRepository(BaseRepository):

    async def create_station(self, station: CreateStation):
        station: Station = Station(**station.dict())
        self._session.add(station)
        await self._session.commit()
        return station
    
    async def create_route(self, route: CreateRoute):
        route: Route = Route(**route.dict())
        self._session.add(route)
        await self._session.commit()
        return route
    
    async def create_route_station(self, route_station: CreateRouteStation):
        route_station: RouteStation = RouteStation(**route_station.dict())
        self._session.add(route_station)
        await self._session.commit()
        return route_station
    
    async def create_train(self, train: CreateTrain):
        train: Train = Train(**train.dict())
        self._session.add(train)
        await self._session.commit()
        return train
    
    async def create_ticket(self, ticket: CreateTicket):
        ticket: Ticket = Ticket(**ticket.dict())
        self._session.add(ticket)
        await self._session.commit()
        return ticket
    
    async def create_ticket_price(self, ticket_price: CreateTicketPrice):
        print("Hello")
        ticket_price: TicketPrice = TicketPrice(**ticket_price.dict())
        self._session.add(ticket_price)
        await self._session.commit()
        return ticket_price

    async def get_stations(self) -> list[Station]:
        query = (
            select(Station)
        )
        return await self.get_all(query)
    
    async def get_routes(self):
        query = (
            select(Route)
        )
        return await self.get_all(query)
    
    async def get_route_stations(self):
        query = (
            select(RouteStation)
        )
        return await self.get_all(query)
    
    async def get_trains(self):
        query = (
            select(Train)
        )
        return await self.get_all(query)
    
    async def get_tickets(self):
        query = (
            select(Ticket)
        )
        return await self.get_all(query)
    
    async def get_ticket_prices(self):
        query = (
            select(TicketPrice)
        )
        return await self.get_all(query)
