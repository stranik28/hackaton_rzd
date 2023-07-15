from fastapi import APIRouter, Depends
from .schema import CreateStation, CreateRoute, CreateRouteStation, CreateTrain, CreateTicket, CreateTicketPrice
from .schema import StationResponse, RouteResponse, RouteStationResponse, TrainResponse, TicketResponse, TicketPriceResponse
from .schema import StationFactory, RouteFactory, RouteStationFactory, TrainFactory, TicketFactory, TicketPriceFactory
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .manager import AdminManager
from transport_routing.model import Station, Route, RouteStation, Train, Ticket, TicketPrice

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/stations")
async def create_station(station: CreateStation, session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.create_station(station, session)

@router.post("/routes")
async def create_route(route: CreateRoute, session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.create_route(route, session)

@router.post("/route_stations")
async def create_route_station(route_station: CreateRouteStation, session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.create_route_station(route_station, session)

@router.post("/trains")
async def create_train(train: CreateTrain, session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.create_train(train, session)

@router.post("/tickets")
async def create_ticket(ticket: CreateTicket, session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.create_ticket(ticket, session)

@router.post("/ticket_prices")
async def create_ticket_price(ticket_price: CreateTicketPrice, session: AsyncSession = Depends(get_async_session)):
    print("Route")
    return await AdminManager.create_ticket_price(ticket_price, session)

@router.get("/stations")
async def get_stations(session: AsyncSession = Depends(get_async_session)):
    result: list[Station] = await AdminManager.get_stations(session)
    return StationFactory.get_station_response_from_list(result)

@router.get("/routes")
async def get_routes(session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.get_routes(session)

@router.get("/route_stations")
async def get_route_stations(session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.get_route_stations(session)

@router.get("/trains")
async def get_trains(session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.get_trains(session)

@router.get("/tickets")
async def get_tickets(session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.get_tickets(session)

@router.get("/ticket_prices")
async def get_ticket_prices(session: AsyncSession = Depends(get_async_session)):
    return await AdminManager.get_ticket_prices(session)
