document.addEventListener("DOMContentLoaded", function() {
    const toggleFilterButton = document.getElementById("toggleFilterButton");
    const filterFormContainer = document.getElementById("filterFormContainer");

    // Check if filters are applied
    const urlParams = new URLSearchParams(window.location.search);
    const filtersApplied = Array.from(urlParams.keys()).length > 0;

    if (filtersApplied) {
        filterFormContainer.style.display = "block";
        toggleFilterButton.textContent = "Hide Filters";
    }

    toggleFilterButton.addEventListener("click", function() {
        if (filterFormContainer.style.display === "none") {
            filterFormContainer.style.display = "block";
            toggleFilterButton.textContent = "Hide Filters";
        } else {
            filterFormContainer.style.display = "none";
            toggleFilterButton.textContent = "Show Filters";
        }
    });
});