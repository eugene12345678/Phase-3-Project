from models import Session, Customer, Movie, Genre, Rental, Reservation
from datetime import datetime, timedelta

session = Session()

def add_customer(name):
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    print(f"Customer {name} added successfully.")

def add_movie(title, genre_names):
    genres = [session.query(Genre).filter_by(name=name).first() or Genre(name=name) for name in genre_names]
    movie = Movie(title=title, genres=genres)
    session.add(movie)
    session.commit()
    print(f"Movie {title} added successfully with genres {genre_names}.")

def add_genre(name):
    genre = Genre(name=name)
    session.add(genre)
    session.commit()
    print(f"Genre {name} added successfully.")

def rent_movie(customer_id, movie_id):
    customer = session.query(Customer).get(customer_id)
    movie = session.query(Movie).get(movie_id)

    if not movie.is_available:
        print(f"Movie {movie.title} is not available. Adding to reservation list.")
        reserve_movie(customer_id, movie_id)
        return
    
    if len(customer.rentals) >= customer.rental_limit:
        print(f"Customer {customer.name} has reached the rental limit.")
        return
    
    due_date = datetime.now() + timedelta(days=7)  # 7-day rental period
    rental = Rental(movie=movie, customer=customer, due_date=due_date)
    movie.is_available = False
    session.add(rental)
    session.commit()
    print(f"Movie {movie.title} rented to {customer.name} until {due_date.date()}.")

def return_movie(customer_id, movie_id):
    rental = session.query(Rental).filter_by(customer_id=customer_id, movie_id=movie_id).first()
    if not rental:
        print("Rental record not found.")
        return
    
    movie = rental.movie
    movie.is_available = True
    session.delete(rental)
    session.commit()

    # Check for reservations
    reservations = session.query(Reservation).filter_by(movie_id=movie_id).all()
    if reservations:
        next_customer = reservations[0].customer
        session.delete(reservations[0])
        session.commit()
        rent_movie(next_customer.id, movie_id)
    print(f"Movie {movie.title} returned successfully.")

def reserve_movie(customer_id, movie_id):
    reservation = Reservation(customer_id=customer_id, movie_id=movie_id)
    session.add(reservation)
    session.commit()
    print(f"Movie reserved for customer {customer_id}.")

def search_movies(title=None, genre_name=None, available=None):
    query = session.query(Movie)
    if title:
        query = query.filter(Movie.title.contains(title))
    if genre_name:
        query = query.join(Movie.genres).filter(Genre.name == genre_name)
    if available is not None:
        query = query.filter(Movie.is_available == available)
    
    movies = query.all()
    for movie in movies:
        print(f"{movie.title} (Available: {movie.is_available})")

