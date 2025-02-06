document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.getElementsByClassName("btn-edit");
    const reviewText = document.getElementById("id_content");
    const ratingSelect = document.getElementById("id_rating");
    const reviewForm = document.getElementById("reviewForm");
    const submitButton = document.getElementById("submitButton");
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteButton");

    /**
     * Initializes edit functionality for the provided edit buttons.
     * 
     * For each button in the `editButtons` collection:
     * - Retrieves the associated review's ID upon click.
     * - Fetches the content and rating of the corresponding review.
     * - Populates the `reviewText` and `ratingSelect` with the review's content and rating.
     * - Updates the form's action attribute to the `edit_review/{reviewId}` endpoint.
     * - Shows the modal.
     */
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let reviewId = e.target.getAttribute("data-review_id");
            let reviewContent = document.getElementById(`review${reviewId}`).innerText;
            let reviewRating = document.getElementById(`reviewRating${reviewId}`).innerText;

            reviewText.value = reviewContent.trim();
            ratingSelect.value = reviewRating.trim();
            submitButton.innerText = "Update";
            reviewForm.setAttribute("action", `edit_review/${reviewId}/`);
        });
    }

    /**
     * Creates modal for delete confirmation.
     */

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let reviewId = e.target.getAttribute("data-review_id");
            deleteConfirm.href = `delete_review/${reviewId}`;
            deleteModal.show();
        });
    }
});