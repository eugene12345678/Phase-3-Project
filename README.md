# Movie Rental System
## Overview
The Movie Rental System is a Python-based application designed to manage the rental and reservation of movies. It allows customers to rent and return movies, reserve movies, and view rental and reservation history. The system uses SQLAlchemy for ORM and SQLite as the database backend.

## Features
- **Customer Management:** Add and manage customer details.
- **Movie Management:** Add and manage movie details including genres.
- **Rental Management:** Rent movies and track due dates.
- **Reservation Management:** Reserve movies and manage reservations.
- **Search and Filter:** Search and filter movies by genres.

## Installation

### Prerequisites
- Python 3.7 or higher
- SQLite (comes pre-installed with Python)
- SQLAlchemy

### Steps
1. **Clone the Repository**

```bash
git clone git@github.com:eugene12345678/Phase-3-Project.git
```
2. **Navigate to the Project Directory**
```bash
cd Phase-3-Project
```
3. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux/MacOS
venv\Scripts\activate     # For Windows
```
4. **Install Dependencies**

```bash
pip install -r requirements.txt
```
5. **Set Up the Database**

```bash
python models.py
```
## Usage
### Running the Application
1. **Start the Application**

```bash
python cli.py
```

2. **Interacting with the CLI**
Once the application is running, you will be presented with a menu of options. You can select an option by entering the corresponding number. Below are the functionalities you can access:

1. **Add Customer:** Enter the name of a new customer to add them to the system.
2. **Add Movie:** Enter the title and genres of a new movie to add it to the inventory.
3. **Add Genre:** Specify a new genre to categorize movies.
4. **Rent Movie:** Rent a movie by entering the customer ID and movie ID.
5. **Return Movie:** Return a rented movie using the customer ID and movie ID.
6. **Search Movies:** Search for movies based on title or genre, with filters for availability.
7. **Exit:** Close the application.

### Database Schema
The application uses a SQLite database with the following tables:

- **customers:** Stores customer information.
- **movies:** Stores movie information.
- **genres:** Stores genre information.
- **rentals:** Tracks rental transactions between customers and movies.
- **reservations:** Manages movie reservations for customers.

### API Endpoints
This application primarily functions through a command-line interface, but you can extend it to include API endpoints in the future. Here are some potential endpoints you could implement:

- POST /customers: Add a new customer.
- POST /movies: Add a new movie.
- POST /genres: Add a new genre.
- POST /rentals: Rent a movie.
- POST /returns: Return a rented movie.
- GET /movies: Search for movies.

### Future Enhancements
- **User Authentication:** Implement user login and authentication for secure access.
- **Web Interface:** Create a web-based interface using Flask or Django for easier accessibility.
- **Enhanced Search:** Add advanced search features, allowing filters by rating, year, etc.
- **Notifications:** Notify customers via email about rental due dates or reservations.
- **Reporting:** Generate reports on rental statistics, popular movies, etc.

### Example Commands
- **Add a Customer**

```markdown
1. Choose option: 1
2. Enter customer name: John Doe
```
- **Rent a Movie**

```markdown
1. Choose option: 4
2. Enter customer ID: 1
3. Enter movie ID: 2
````
- **Return a Movie**

```markdown
1. Choose option: 5
2. Enter customer ID: 1
3. Enter movie ID: 2
```
## Contributing
We welcome contributions to improve the Movie Rental System! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch)`.
5. Create a new Pull Request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or issues, please contact eugene.mukabi@student.moringaschool.com.

## Author
[Eugene Mathenge](https://github.com/eugene12345678)


