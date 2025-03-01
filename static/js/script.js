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
