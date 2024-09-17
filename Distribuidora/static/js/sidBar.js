document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#botonMenuSidebar').addEventListener('click', function() {
        const sidBar = document.getElementById('sidBar');
        sidBar.classList.toggle('d-none');
    });
});
