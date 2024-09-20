from models import Session, Customer, Movie, Genre, Rental, Reservation
from datetime import datetime, timedelta

# Create a session to interact with the database
session = Session()

# Function to add a new customer to the database
def add_customer(name):
    customer = Customer(name=name)
    session.add(customer)  # Add the customer object to the session
    session.commit()  # Commit the transaction to save it in the database
    print(f"Customer {name} added successfully.")

# Function to add a new movie with associated genres
def add_movie(title, genre_names):
    # Retrieve existing genres or create new ones based on genre_names
    genres = [session.query(Genre).filter_by(name=name).first() or Genre(name=name) for name in genre_names]
    
    # Create the movie object with title and genres
    movie = Movie(title=title, genres=genres)
    
    session.add(movie)  # Add the movie object to the session
    session.commit()  # Commit the transaction
    print(f"Movie {title} added successfully with genres {genre_names}.")

# Function to add a new genre to the database
def add_genre(name):
    genre = Genre(name=name)
    session.add(genre)  # Add the genre object to the session
    session.commit()  # Commit the transaction to save it
    print(f"Genre {name} added successfully.")

# Function to rent a movie to a customer
def rent_movie(customer_id, movie_id):
    customer = session.query(Customer).get(customer_id)  # Get customer by ID
    movie = session.query(Movie).get(movie_id)  # Get movie by ID

    # Check if the movie is available for rent
    if not movie.is_available:
        print(f"Movie {movie.title} is not available. Adding to reservation list.")
        reserve_movie(customer_id, movie_id)  # Reserve the movie for the customer
        return

    # Check if the customer has reached their rental limit
    if len(customer.rentals) >= customer.rental_limit:
        print(f"Customer {customer.name} has reached the rental limit.")
        return

    # Set the rental due date to 7 days from now
    due_date = datetime.now() + timedelta(days=7)
    
    # Create a new rental record for the customer
    rental = Rental(movie=movie, customer=customer, due_date=due_date)
    
    movie.is_available = False  # Mark the movie as unavailable
    session.add(rental)  # Add the rental object to the session
    session.commit()  # Commit the transaction
    print(f"Movie {movie.title} rented to {customer.name} until {due_date.date()}.")

# Function to return a rented movie
def return_movie(customer_id, movie_id):
    # Get the rental record for the customer and movie
    rental = session.query(Rental).filter_by(customer_id=customer_id, movie_id=movie_id).first()
    
    if not rental:
        print("Rental record not found.")
        return
    
    movie = rental.movie
    movie.is_available = True  # Mark the movie as available again
    session.delete(rental)  # Delete the rental record
    session.commit()  # Commit the changes

    # Check if there are any reservations for the movie
    reservations = session.query(Reservation).filter_by(movie_id=movie_id).all()
    
    if reservations:
        # If there are reservations, rent the movie to the next customer
        next_customer = reservations[0].customer
        session.delete(reservations[0])  # Remove the reservation
        session.commit()
        rent_movie(next_customer.id, movie_id)  # Rent the movie to the next customer in line
    
    print(f"Movie {movie.title} returned successfully.")

# Function to reserve a movie for a customer if it's unavailable
def reserve_movie(customer_id, movie_id):
    # Create a reservation record for the movie and customer
    reservation = Reservation(customer_id=customer_id, movie_id=movie_id)
    session.add(reservation)  # Add the reservation to the session
    session.commit()  # Commit the transaction
    print(f"Movie reserved for customer {customer_id}.")

# Function to search for movies by title, genre, and availability
def search_movies(title=None, genre_name=None, available=None):
    query = session.query(Movie)  # Start the query on the Movie model
    
    if title:
        # Filter by movie title if provided
        query = query.filter(Movie.title.contains(title))
    
    if genre_name:
        # Join the Movie and Genre models and filter by genre name if provided
        query = query.join(Movie.genres).filter(Genre.name == genre_name)
    
    if available is not None:
        # Filter by availability status if provided
        query = query.filter(Movie.is_available == available)
    
    # Fetch all matching movies
    movies = query.all()
    
    # Print each movie's title and availability status
    for movie in movies:
        print(f"{movie.title} (Available: {movie.is_available})")
