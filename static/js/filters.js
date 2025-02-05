document.addEventListener("DOMContentLoaded", function() {
    const toggleFilterButton = document.getElementById("toggleFilterButton");
    const filterFormContainer = document.getElementById("filterFormContainer");

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