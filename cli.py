from main import add_customer, add_movie, add_genre, rent_movie, return_movie, search_movies

def main():
    while True:
        print("\nMovie Rental System")
        print("1. Add Customer")
        print("2. Add Movie")
        print("3. Add Genre")
        print("4. Rent Movie")
        print("5. Return Movie")
        print("6. Search Movies")
        print("7. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter customer name: ")
            add_customer(name)
        elif choice == '2':
            title = input("Enter movie title: ")
            genres = input("Enter genres (comma-separated): ").split(',')
            add_movie(title, genres)
        elif choice == '3':
            name = input("Enter genre name: ")
            add_genre(name)
        elif choice == '4':
            customer_id = int(input("Enter customer ID: "))
            movie_id = int(input("Enter movie ID: "))
            rent_movie(customer_id, movie_id)
        elif choice == '5':
            customer_id = int(input("Enter customer ID: "))
            movie_id = int(input("Enter movie ID: "))
            return_movie(customer_id, movie_id)
        elif choice == '6':
            title = input("Enter movie title (leave blank for any): ")
            genre = input("Enter genre (leave blank for any): ")
            available = input("Available only? (yes/no): ").lower() == 'yes'
            search_movies(title=title, genre_name=genre, available=available)
        elif choice == '7':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
