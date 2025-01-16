// Modal Toggle
document.addEventListener("DOMContentLoaded", () => {
  const modals = document.querySelectorAll("[data-popup]");
  const closeButtons = document.querySelectorAll("[data-popup-close]");

  modals.forEach((modal) => {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.style.display = "none";
      }
    });
  });

  closeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      button.closest(".popup").style.display = "none";
    });
  });
});
