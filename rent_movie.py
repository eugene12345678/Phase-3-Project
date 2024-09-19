from datetime import datetime, timedelta
from models import Session, Rental, Reservation, Movie, Customer

def rent_movie(customer_id, movie_id):
    session = Session()

    # Check if the movie is available
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if not movie or not movie.is_available:
        print("Movie is not available for rent.")
        session.close()
        return

    # Check if the customer has reached their rental limit
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if not customer:
        print("Customer not found.")
        session.close()
        return

    # Check the current number of rentals
    current_rentals_count = session.query(Rental).filter_by(customer_id=customer_id).count()
    if current_rentals_count >= customer.rental_limit:
        print("Customer has reached their rental limit.")
        session.close()
        return

    # Create a new rental
    rental = Rental(
        movie_id=movie_id,
        customer_id=customer_id,
        rental_date=datetime.utcnow(),
        due_date=datetime.utcnow() + timedelta(days=7)  # Setting due date as 7 days from now
    )
    session.add(rental)

    # Mark the movie as not available
    movie.is_available = False

    # Create a reservation entry
    reservation = Reservation(
        movie_id=movie_id,
        customer_id=customer_id,
        reservation_date=datetime.utcnow()
    )
    session.add(reservation)

    # Commit all changes to the database
    session.commit()

    print(f"Movie '{movie.title}' rented to customer '{customer.name}' and reserved successfully.")

    session.close()

# Example usage
if __name__ == "__main__":
    rent_movie(customer_id=1, movie_id=1)
