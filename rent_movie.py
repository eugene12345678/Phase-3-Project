from datetime import datetime, timedelta
from models import Session, Rental, Reservation, Movie, Customer

def rent_movie(customer_id, movie_id):
    session = Session()  # Start a new database session

    # Check if the movie is available for rent
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if not movie or not movie.is_available:
        print("Movie is not available for rent.")
        session.close()  # Close the session before returning
        return

    # Check if the customer exists in the database
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if not customer:
        print("Customer not found.")
        session.close()  # Close the session before returning
        return

    # Check the current number of rentals for the customer
    current_rentals_count = session.query(Rental).filter_by(customer_id=customer_id).count()
    if current_rentals_count >= customer.rental_limit:
        print("Customer has reached their rental limit.")
        session.close()  # Close the session before returning
        return

    # Create a new rental record
    rental = Rental(
        movie_id=movie_id,  # The ID of the rented movie
        customer_id=customer_id,  # The ID of the customer renting the movie
        rental_date=datetime.utcnow(),  # Set the rental date to now
        due_date=datetime.utcnow() + timedelta(days=7)  # Set the due date to 7 days from now
    )
    session.add(rental)  # Add the rental record to the session

    # Mark the movie as not available
    movie.is_available = False

    # Create a reservation entry for the rental
    reservation = Reservation(
        movie_id=movie_id,  # The ID of the reserved movie
        customer_id=customer_id,  # The ID of the customer making the reservation
        reservation_date=datetime.utcnow()  # Set the reservation date to now
    )
    session.add(reservation)  # Add the reservation record to the session

    # Commit all changes to the database
    session.commit()

    print(f"Movie '{movie.title}' rented to customer '{customer.name}' and reserved successfully.")

    session.close()  # Close the session after all operations are complete

# Example usage
if __name__ == "__main__":
    rent_movie(customer_id=1, movie_id=1)  # Replace with actual customer and movie IDs for testing
