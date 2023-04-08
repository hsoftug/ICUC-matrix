const productImages = document.querySelectorAll(".product-images - img");
const productIamgesSlide = document.querySelector(".images-slider");

let activeImageSlide = 0;

productImages.forEach((item, i) => {
    item.addEventListener('click', () => {
        productImages[activeImageSlide].classiList.remove('active');
        item.classList.add('active');
        productIamgesSlide.style.backgroundImage = 'url('${item.src}')';
        activeImageSlide = i;
    })
    })

//toogle size buttons
const sizeBtns = document.querySelectorAll('.size-radio-btn');
let checkedBtn = 0;

sizeBtns.forEach((item, i) => {
    item.addEventListener('click', () =>{
        sizeBtns[checkedBtn].classList.remove('check');
        item.classList.add('check');
        checkedBtn = i;
    })
    }) 

