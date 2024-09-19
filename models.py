from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

# Association table for the many-to-many relationship between movies and genres
movie_genre = Table(
    'movie_genre', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rental_limit = Column(Integer, default=3)  # Rental limit for each customer
    rentals = relationship('Rental', back_populates='customer')
    reservations = relationship('Reservation', back_populates='customer')

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_available = Column(Boolean, default=True)
    genres = relationship('Genre', secondary=movie_genre, back_populates='movies')
    rentals = relationship('Rental', back_populates='movie')
    reservations = relationship('Reservation', back_populates='movie')

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    movies = relationship('Movie', secondary=movie_genre, back_populates='genres')

class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rental_date = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)

    movie = relationship('Movie', back_populates='rentals')
    customer = relationship('Customer', back_populates='rentals')

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    reservation_date = Column(DateTime, default=datetime.utcnow)

    movie = relationship('Movie', back_populates='reservations')
    customer = relationship('Customer', back_populates='reservations')

# Setup the database
engine = create_engine('sqlite:///movie_rental_system.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)