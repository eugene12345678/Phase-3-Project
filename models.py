from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

# Create a base class for declarative class definitions
Base = declarative_base()

# Association table for the many-to-many relationship between movies and genres
movie_genre = Table(
    'movie_genre', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),  # Foreign key referencing movies
    Column('genre_id', Integer, ForeignKey('genres.id'))   # Foreign key referencing genres
)

# Class representing customers in the database
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)  # Unique identifier for each customer
    name = Column(String)  # Customer's name
    rental_limit = Column(Integer, default=3)  # Rental limit for each customer
    rentals = relationship('Rental', back_populates='customer')  # Relationship with rentals
    reservations = relationship('Reservation', back_populates='customer')  # Relationship with reservations

# Class representing movies in the database
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)  # Unique identifier for each movie
    title = Column(String)  # Movie title
    is_available = Column(Boolean, default=True)  # Availability status of the movie
    genres = relationship('Genre', secondary=movie_genre, back_populates='movies')  # Many-to-many relationship with genres
    rentals = relationship('Rental', back_populates='movie')  # Relationship with rentals
    reservations = relationship('Reservation', back_populates='movie')  # Relationship with reservations

# Class representing genres in the database
class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)  # Unique identifier for each genre
    name = Column(String)  # Genre name
    movies = relationship('Movie', secondary=movie_genre, back_populates='genres')  # Many-to-many relationship with movies

# Class representing rental records in the database
class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True)  # Unique identifier for each rental
    movie_id = Column(Integer, ForeignKey('movies.id'))  # Foreign key referencing the rented movie
    customer_id = Column(Integer, ForeignKey('customers.id'))  # Foreign key referencing the customer
    rental_date = Column(DateTime, default=datetime.utcnow)  # Date and time of rental
    due_date = Column(DateTime)  # Due date for returning the movie

    movie = relationship('Movie', back_populates='rentals')  # Relationship with the movie
    customer = relationship('Customer', back_populates='rentals')  # Relationship with the customer

# Class representing reservation records in the database
class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)  # Unique identifier for each reservation
    movie_id = Column(Integer, ForeignKey('movies.id'))  # Foreign key referencing the reserved movie
    customer_id = Column(Integer, ForeignKey('customers.id'))  # Foreign key referencing the customer
    reservation_date = Column(DateTime, default=datetime.utcnow)  # Date and time of reservation

    movie = relationship('Movie', back_populates='reservations')  # Relationship with the movie
    customer = relationship('Customer', back_populates='reservations')  # Relationship with the customer

# Setup the database
engine = create_engine('sqlite:///movie_rental_system.db')  # Create a SQLite database engine
Base.metadata.create_all(engine)  # Create all tables in the database
Session = sessionmaker(bind=engine)  # Create a session factory for interacting with the database
