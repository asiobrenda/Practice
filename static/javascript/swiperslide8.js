console.log("Swiper initialization started");
var swiper = new Swiper('.mySwiper', {
  slidesPerView: 3,
  spaceBetween: 10,
  loop: true,
  direction: 'vertical',
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  autoplay: {
    delay: 1000,
  },
});
console.log("Swiper initialization completed");