const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li')
    //  Aquí cremamos un evento que registra un click y realiza lo siguiente:
    burger.addEventListener('click', () => {
        // Esto activa los estilos que transladan el menú hacia la izquierda para hacerlo visible
        nav.classList.toggle('nav-active');
        // Esto es lo que activa la transformación de nuestro botón.
        burger.classList.toggle('toggle')

    });
}

navSlide();