  function testimonialSlider() {
            const slides = document.querySelectorAll('.testimonial-container');
            let currentIndex = 0;

            function showSlide(index) {
                slides.forEach((slide) => {
                    slide.style.display = 'none';
                });

                slides[index].style.display = 'block';
            }

            function nextSlide() {
                currentIndex = (currentIndex + 1) % slides.length;
                showSlide(currentIndex);
            }

            function previousSlide() {
                currentIndex = (currentIndex - 1 + slides.length) % slides.length;
                showSlide(currentIndex);
            }

            // Auto-advance to the next slide every 5 seconds (5000 milliseconds)
            setInterval(nextSlide, 5000);

            // Show the initial slide
            showSlide(currentIndex);
        }

        // Call the testimonialSlider function when the document is ready
        document.addEventListener('DOMContentLoaded', testimonialSlider);


// JavaScript code for continuous slide functionality and dot pagination
const slides = document.querySelectorAll('.container-test');
const dots = document.querySelectorAll('.dot');
let currentIndex = 0;

function showSlides() {
    slides.forEach((slide, index) => {
        slide.style.display = 'none';
    });

    for (let i = 0; i < 3; i++) {
        const slideIndex = (currentIndex + i) % slides.length;
        slides[slideIndex].style.display = 'block';
    }

    activateDot(currentIndex);
    currentIndex = (currentIndex + 1) % slides.length;
}

function activateDot(index) {
    dots.forEach((dot) => {
        dot.classList.remove('active');
    });
    dots[index].classList.add('active');
}

// Auto-advance to the next set of slides every 5 seconds (5000 milliseconds)
setInterval(showSlides, 5000); // Changed from 1000 to 5000

// Show the initial set of slides
showSlides();
