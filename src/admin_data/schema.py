from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from transport_routing.model import Station, Route, RouteStation, Train, Ticket, TicketPrice

class CreateStation(BaseModel):
    name: str = Field(..., example="Moscow")
    lat: float = Field(..., example=55.7558)
    lng: float = Field(..., example=37.6173)

class CreateRoute(BaseModel):
    name: str = Field(..., example="Moscow - St. Petersburg")
    
class CreateRouteStation(BaseModel):
    route_id: int = Field(..., example=1)
    station_id: int = Field(..., example=1)
    order: int = Field(..., example=1)
    
class CreateTrain(BaseModel):
    name: str = Field(..., example="Moscow - St. Petersburg")
    route_id: int = Field(..., example=1)
    capacity: int = Field(..., example=100)

class CreateTicket(BaseModel):
    train_id: int = Field(..., example=1)
    departure_station_id: int = Field(..., example=1)
    arrival_station_id: int = Field(..., example=2)
    departure_time: Optional[datetime] = Field(..., example="2021-01-01T00:00:00")
    arrival_time: Optional[datetime] = Field(..., example="2021-01-01T00:00:00")
    price: float = Field(..., example=100.0)
    sold: Optional[int] = Field(..., example=0)
    service_class: str = Field(..., example="economy")
    date: datetime = datetime.utcnow()

class CreateTicketPrice(BaseModel):
    ticket_id: int = Field(..., example=1)
    price: float = Field(..., example=100.0)
    date: datetime = datetime.utcnow()

class StationResponse(CreateStation):
    id: int = Field(..., example=1)

class RouteResponse(CreateRoute):
    id: int = Field(..., example=1)

class RouteStationResponse(CreateRouteStation):
    id: int = Field(..., example=1)

class TrainResponse(CreateTrain):
    id: int = Field(..., example=1)

class TicketResponse(CreateTicket):
    id: int = Field(..., example=1)

class TicketPriceResponse(CreateTicketPrice):
    id: int = Field(..., example=1)

class StationFactory:

    @staticmethod
    def get_station_response_from_model(station: Station) -> StationResponse:
        return StationResponse(
            id=station.id,
            name=station.name,
            lat=station.lat,
            lng=station.lng
        )
    
    @classmethod
    def get_station_response_from_list(cls, stations: list[Station]) -> list[StationResponse]:
        return [cls.get_station_response_from_model(station) for station in stations]
    
class RouteFactory:

    @staticmethod
    def get_route_response_from_model(route: Route) -> RouteResponse:
        return RouteResponse(
            id=route.id,
            name=route.name
        )
    
    @classmethod
    def get_route_response_from_list(cls, routes: list[Route]) -> list[RouteResponse]:
        return [cls.get_route_response_from_model(route) for route in routes]
    
class RouteStationFactory:
    
        @staticmethod
        def get_route_station_response_from_model(route_station: RouteStation) -> RouteStationResponse:
            return RouteStationResponse(
                id=route_station.id,
                route_id=route_station.route_id,
                station_id=route_station.station_id,
                order=route_station.order
            )
        
        @classmethod
        def get_route_station_response_from_list(cls, route_stations: list[RouteStation]) -> list[RouteStationResponse]:
            return [cls.get_route_station_response_from_model(route_station) for route_station in route_stations]
        
class TrainFactory:
        
            @staticmethod
            def get_train_response_from_model(train: Train) -> TrainResponse:
                return TrainResponse(
                    id=train.id,
                    name=train.name,
                    route_id=train.route_id,
                    capacity=train.capacity
                )
            
            @classmethod
            def get_train_response_from_list(cls, trains: list[Train]) -> list[TrainResponse]:
                return [cls.get_train_response_from_model(train) for train in trains]
            
class TicketFactory:
     
    @staticmethod
    def get_ticket_response_from_model(ticket: Ticket) -> TicketResponse:
        return TicketResponse(
            id=ticket.id,
            train_id=ticket.train_id,
            departure_station_id=ticket.departure_station_id,
            arrival_station_id=ticket.arrival_station_id,
            departure_time=ticket.departure_time,
            arrival_time=ticket.arrival_time,
            price=ticket.price,
            sold=ticket.sold,
            service_class=ticket.service_class,
            date=ticket.date
        )
    
    @classmethod
    def get_ticket_response_from_list(cls, tickets: list[Ticket]) -> list[TicketResponse]:
        return [cls.get_ticket_response_from_model(ticket) for ticket in tickets]
    
class TicketPriceFactory:

    @staticmethod
    def get_ticket_price_response_from_model(ticket_price: TicketPrice) -> TicketPriceResponse:
        return TicketPriceResponse(
            id=ticket_price.id,
            ticket_id=ticket_price.ticket_id,
            price=ticket_price.price,
        )
    
    @classmethod
    def get_ticket_price_response_from_list(cls, ticket_prices: list[TicketPrice]) -> list[TicketPriceResponse]:
        return [cls.get_ticket_price_response_from_model(ticket_price) for ticket_price in ticket_prices]
    