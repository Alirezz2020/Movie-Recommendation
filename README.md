
# Movie Recommendation Django Project

This is a Django-based movie recommendation system with a Netflix-style interface. The project includes the following apps:

- **accounts:** User authentication and profile management.
- **home:** Homepage with dynamic carousels for new and top movies.
- **movies:** Handles movie listings, detail pages, watchlist management, and user ratings.
- **recommendations:** Provides both general and personalized movie recommendations.

## Features

- **Movie Listings:** Display a list of movies fetched from an external API or dataset.
- **Movie Details:** View detailed information for each movie, including poster, description, release date, and ratings.
- **Watchlist:** Users can add movies to a personal watchlist.
- **Ratings:** Each user can rate a movie once, and ratings are averaged to provide a general score.
- **Recommendations:** 
  - **General Recommendations:** Shows top-rated movies.
  - **Personalized Recommendations:** Displays movies based on the user's watchlist (e.g., based on genre preferences).
- **Dynamic Home Page:** The home page includes moving sections for "New Movies" and "Top Movies" that rotate every 5 seconds.




## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Alirezz2020/Movie-Recommendation.git
   cd Movie-Recommendation
2. **Set Up a Virtual Environment:**
    ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
3. **Install Dependencies:**
   ```sh
    pip install -r requirements.txt

4. **Apply Migrations:**
    ```sh
    python manage.py migrate
5. **Create a Superuser:**
    ```sh
   python manage.py createsuperuser
6. **Run the Development Server:**
    ```sh
   python manage.py runserver
7. **Access the Application:**

    Visit http://127.0.0.1:8000/ in your browser to start exploring the platform.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to include tests and follow the project’s coding standards.

## License
This project is licensed under the MIT License.

