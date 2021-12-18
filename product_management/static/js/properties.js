const navList = document.querySelector('.nav__list');
const navToggle = document.querySelector('.lines');

navToggle.addEventListener('click', ()=> {
    navList.classList.toggle('show');    
});

