document.addEventListener("DOMContentLoaded", function () {
    /**
     * Updates the year in the footer to the current year.
     */
    const yearElement = document.getElementById("year");
    const currentYear = new Date().getFullYear();
    yearElement.textContent = currentYear;

});