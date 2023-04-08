const createNav = () => {
    let nav = document.querySelector(".navbar");
    nav.innerHTML = '<div class="nav">
    <img src="../New folder (2)/img/nfb copy.png" class="brand-logo", alt="">
    <div class="nav-items">
       <div class="search">
           <input type="text" class="search-box" placeholder="search brand, product"/>
           <button class="search-btn">search</button>
        </div>
       <a href="#"><img src="../New folder (2)/img/user.png" alt=""/></a>
       <a href="#"><img src="../New folder (2)/img/cart.png" alt=""/></a>
    </div>
 </div>
 <ul class="links-container">
    <li class="Links-item"><a href="#" class="Link">home</a></li>
    <li class="Links-item"><a href="#" class="Link">ladies</a></li>
    <li class="Links-item"><a href="#" class="Link">gentes</a></li>
    <li class="Links-item"><a href="#" class="Link">kids</a></li>
    <li class="Links-item"><a href="#" class="Link">shoes</a></li>
    <li class="Links-item"><a href="#" class="Link">accessories</a></li>
  </ul>
  ;
}


createNav();