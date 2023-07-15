from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from database import Base

class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    lat = Column(Float)
    lng = Column(Float)

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class RouteStation(Base):
    __tablename__ = "route_stations"

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    station_id = Column(Integer, ForeignKey("stations.id"))
    order = Column(Integer)

class Train(Base):
    __tablename__ = "trains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    capacity = Column(Integer)

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    train_id = Column(Integer, ForeignKey("trains.id"))
    departure_station_id = Column(Integer, ForeignKey("stations.id"))
    arrival_station_id = Column(Integer, ForeignKey("stations.id"))
    departure_time = Column(DateTime, default=None)
    arrival_time = Column(DateTime, default=None)
    price = Column(Float)
    sold = Column(Integer)
    service_class = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

class TicketPrice(Base):
    __tablename__ = "tickets_prices"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    price = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)