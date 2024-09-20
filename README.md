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
cd Phase-3-Project
```
2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux/MacOS
venv\Scripts\activate     # For Windows
```
3. **Install Dependencies**

```bash
pip install -r requirements.txt
```
4. **Set Up the Database**

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

The application provides a command-line interface (CLI) for interacting with the system. You can choose options such as:

- Add a new customer
- Add a new movie
- Rent a movie
- Return a movie
- Reserve a movie
- View rental and reservation history
Follow the prompts in the terminal to perform these actions.

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

Author
[Eugene Mathenge](https://github.com/eugene12345678)


