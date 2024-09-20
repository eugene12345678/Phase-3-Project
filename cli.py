from main import add_customer, add_movie, add_genre, rent_movie, return_movie, search_movies

def main():
    # Main loop for the Movie Rental System
    while True:
        print("\nMovie Rental System")
        print("1. Add Customer")
        print("2. Add Movie")
        print("3. Add Genre")
        print("4. Rent Movie")
        print("5. Return Movie")
        print("6. Search Movies")
        print("7. Exit")
        
        # Prompt user for input
        choice = input("Choose an option: ")
        
        # Add a new customer
        if choice == '1':
            name = input("Enter customer name: ")
            add_customer(name)
        
        # Add a new movie
        elif choice == '2':
            title = input("Enter movie title: ")
            genres = input("Enter genres (comma-separated): ").split(',')
            add_movie(title, genres)
        
        # Add a new genre
        elif choice == '3':
            name = input("Enter genre name: ")
            add_genre(name)
        
        # Rent a movie to a customer
        elif choice == '4':
            customer_id = int(input("Enter customer ID: "))
            movie_id = int(input("Enter movie ID: "))
            rent_movie(customer_id, movie_id)
        
        # Return a rented movie
        elif choice == '5':
            customer_id = int(input("Enter customer ID: "))
            movie_id = int(input("Enter movie ID: "))
            return_movie(customer_id, movie_id)
        
        # Search for movies based on title and genre
        elif choice == '6':
            title = input("Enter movie title (leave blank for any): ")
            genre = input("Enter genre (leave blank for any): ")
            available = input("Available only? (yes/no): ").lower() == 'yes'
            search_movies(title=title, genre_name=genre, available=available)
        
        # Exit the program
        elif choice == '7':
            print("Exiting the Movie Rental System.")
            break
        
        # Handle invalid options
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
