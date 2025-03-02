let currentPage = 1;

window.onscroll = function () {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        currentPage++;
        loadMoreMovies(currentPage);
    }
};

function loadMoreMovies(page) {
    fetch(`/movies/?page=${page}`)
        .then(response => response.json())
        .then(data => {
            const movieList = document.querySelector('.movie-list');
            data.movies.forEach(movie => {
                let movieItem = document.createElement('div');
                movieItem.classList.add('movie-item');
                movieItem.innerHTML = `
                    <a href="/movies/${movie.id}">
                        <img src="${movie.poster_url}" alt="${movie.title}">
                        <h3>${movie.title}</h3>
                    </a>
                `;
                movieList.appendChild(movieItem);
            });
        });
}
// static/js/home.js
document.addEventListener("DOMContentLoaded", () => {
    console.log("Home page is loaded and ready!");
    // You can add further interactive behavior here.
});
document.addEventListener('DOMContentLoaded', function() {
    function cycleCarousel(carouselId) {
        let carousel = document.getElementById(carouselId);
        if (!carousel) return;
        let items = carousel.getElementsByClassName('carousel-item');
        let currentIndex = 0;
        // Hide all items except the first
        for(let i = 0; i < items.length; i++){
            items[i].style.display = 'none';
        }
        if(items.length > 0) {
            items[0].style.display = 'block';
        }
        setInterval(function() {
            items[currentIndex].style.display = 'none';
            currentIndex = (currentIndex + 1) % items.length;
            items[currentIndex].style.display = 'block';
        }, 5000); // change every 5 seconds
    }

    cycleCarousel('newMoviesCarousel');
    cycleCarousel('topMoviesCarousel');
});
