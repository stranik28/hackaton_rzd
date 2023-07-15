from .repository import AdminRepository
from .schema import CreateStation, CreateRoute, CreateRouteStation, CreateTrain, CreateTicket, CreateTicketPrice
from sqlalchemy.ext.asyncio import AsyncSession
from transport_routing.model import Station, Route, RouteStation, Train, Ticket, TicketPrice

class AdminManager():

    @classmethod
    async def create_station(cls, station: CreateStation, session: AsyncSession):
        return await AdminRepository(session).create_station(station)
    
    @classmethod
    async def create_route(cls, route: CreateRoute, session: AsyncSession):
        return await AdminRepository(session).create_route(route)
    
    @classmethod
    async def create_route_station(cls, route_station: CreateRouteStation, session: AsyncSession):
        return await AdminRepository(session).create_route_station(route_station)
    
    @classmethod
    async def create_train(cls, train: CreateTrain, session: AsyncSession):
        return await AdminRepository(session).create_train(train)
    
    @classmethod
    async def create_ticket(cls, ticket: CreateTicket, session: AsyncSession):
        return await AdminRepository(session).create_ticket(ticket)
    
    @classmethod
    async def create_ticket_price(cls, ticket_price: CreateTicketPrice, session: AsyncSession):
        print("No_create")
        return await AdminRepository(session).create_ticket_price(ticket_price)
    
    @classmethod
    async def get_stations(cls, session: AsyncSession)-> list[Station]:
        return await AdminRepository(session).get_stations()
    
    @classmethod
    async def get_routes(cls, session: AsyncSession):
        return await AdminRepository(session).get_routes()
    
    @classmethod
    async def get_route_stations(cls, session: AsyncSession):
        return await AdminRepository(session).get_route_stations()
    
    @classmethod
    async def get_trains(cls, session: AsyncSession):
        return await AdminRepository(session).get_trains()
    
    @classmethod
    async def get_tickets(cls, session: AsyncSession):
        return await AdminRepository(session).get_tickets()
    
    @classmethod
    async def get_ticket_prices(cls, session: AsyncSession):
        return await AdminRepository(session).get_ticket_prices()
    
