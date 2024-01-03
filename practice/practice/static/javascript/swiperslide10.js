var swiper = new Swiper('.mySwiper', {
  slidesPerView: 3,
  spaceBetween: 12,
  loop: true,
  direction: 'horizontal',
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    dynamicBullets: true,
  },
  autoplay: {
    delay: 1000,
  },
});
