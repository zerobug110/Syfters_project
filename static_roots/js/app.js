                                //nav slider
//select variable


//generate the current date

// const currentDate = document.getElementById('current-date');

// currentDate.innerHTML = new Date().getFullYear();






/// image of slider
//////////////////////////
/////////////////////////
////////////////////////
///////////////////////
 
let productImg = document.getElementById('featured');
let thumbnail = document.getElementsByClassName('thumbnail')


thumbnail[0].onclick = function() {
    productImg.src = thumbnail[0].src;
}
thumbnail[1].onclick = function() {
    productImg.src = thumbnail[1].src;
}
thumbnail[2].onclick = function() {
    productImg.src = thumbnail[2].src;
}
thumbnail[3].onclick = function() {
    productImg.src = thumbnail[3].src;
}

//generate the current date
date.innerHTML = new Date().getFullYear();