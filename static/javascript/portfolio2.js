// Get references to the filter buttons and portfolio items
const filterButtons = document.querySelectorAll('#portfolio-filters li');
const portfolioItems = document.querySelectorAll('.image-portfolio');

// Add click event listeners to filter buttons
filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const category = button.getAttribute('data-filter');

    // Remove the "active" class from all filter buttons
    filterButtons.forEach((btn) => {
      btn.classList.remove('filter-active');
    });

    // Add the "active" class to the clicked filter button
    button.classList.add('filter-active');

    // Loop through portfolio items and show/hide based on the selected category
    portfolioItems.forEach((item) => {
      const itemCategory = item.getAttribute('data-category');

      if (category === '*' || category === itemCategory) {
        item.style.display = 'block'; // Show the item
      } else {
        item.style.display = 'none'; // Hide the item
      }
    });
  });
});
