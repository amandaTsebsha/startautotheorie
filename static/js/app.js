(function() {
    // Focus Visible Polyfill (if you still need it)
    function applyFocusVisiblePolyfill(document) {
      /**
       * Applies the focus-visible polyfill to the given document.
       * @param {Document} document The document to apply the polyfill to.
       */
      let hadKeyboardEvent = true;
      let hadTouchEvent = false;
      let hadPointerEvent = false;
      let pointerRecentlyActive = false;
    
      const inputTypes = new Set(['input', 'textarea', 'select', 'button']);
    
      const focusableSelectors = `
        a[href],
        area[href],
        input:not([disabled]):not([type="hidden"]):not([aria-hidden]),
        select:not([disabled]):not([aria-hidden]),
        textarea:not([disabled]):not([aria-hidden]),
        button:not([disabled]):not([aria-hidden]),
        iframe,
        object,
        embed,
        [tabindex="0"],
        [contenteditable],
        audio[controls],
        video[controls],
        summary
      `.trim().replace(/\s+/g, ',');
    
      /**
       * Helper function for removing the focus from an element.
       * @param {Element} el The element to remove focus from.
       */
      function removeFocus(el) {
        if (el.classList.contains('focus-visible')) {
          el.classList.remove('focus-visible');
        }
      }
    
      /**
       * Helper function for adding the focus to an element.
       * @param {Element} el The element to add focus to.
       */
      function addFocus(el) {
        if (!el.classList.contains('focus-visible')) {
          el.classList.add('focus-visible');
        }
      }
    
      /**
       * Identifies if the focus should be visible for the given element.
       * @param {Element} el The element to check.
       * @returns {boolean} True if the focus should be visible, false otherwise.
       */
      function focusShouldBeVisible(el) {
        if (hadKeyboardEvent) {
          return true;
        }
    
        if (hadTouchEvent) {
          return false;
        }
    
        // All other cases where we want to determine whether the focus should be visible
        if (el.matches(focusableSelectors)) {
          return true;
        }
    
        return false;
      }
    
      /**
       * Handles the focus event on an element.
       * @param {FocusEvent} e The focus event.
       */
      function handleFocus(e) {
        if (focusShouldBeVisible(e.target)) {
          addFocus(e.target);
        }
      }
    
      /**
       * Handles the blur event on an element.
       * @param {FocusEvent} e The blur event.
       */
      function handleBlur(e) {
        removeFocus(e.target);
      }
    
      /**
       * Handles the keydown event on the document.
       */
      function handleKeyDown(e) {
        if (e.metaKey || e.altKey || e.ctrlKey) {
          return;
        }
        hadKeyboardEvent = true;
      }
    
      /**
       * Handles the touchstart event on the document.
       */
      function handleTouchStart() {
        hadTouchEvent = true;
        hadKeyboardEvent = false;
        hadPointerEvent = false;
        pointerRecentlyActive = false;
      }
    
      /**
       * Handles the pointerdown event on the document.
       */
      function handlePointerDown() {
        hadPointerEvent = true;
        pointerRecentlyActive = true;
    
        setTimeout(() => {
          pointerRecentlyActive = false;
        }, 500);
      }
    
      /**
       * Handles the mousemove event on the document.
       */
      function handleMouseMove() {
        if (pointerRecentlyActive) {
          hadKeyboardEvent = false;
          hadTouchEvent = false;
        }
      }
    
      document.addEventListener('focus', handleFocus, true);
      document.addEventListener('blur', handleBlur, true);
      document.addEventListener('keydown', handleKeyDown, true);
      document.addEventListener('touchstart', handleTouchStart, true);
      document.addEventListener('pointerdown', handlePointerDown, true);
      document.addEventListener('mousemove', handleMouseMove);
    }

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

    // Other init functions (placeholders)
    function initMisc() { /* ... */ }
    function initNavigation() { /* ... */ }
    function initSliders() { /* ... */ }
    function initVideo() { /* ... */ }
    function initScrollEvents() { /* ... */ }
    function initScrollTo() { /* ... */ }
    function initScorecard() { /* ... */ }
    function initPopups() { /* ... */ }
    function initDevTools() { /* ... */ }

    // Initialization logic (runs when the script loads)
    applyFocusVisiblePolyfill(document);
    initMisc();
    initNavigation();
    initSliders();
    initVideo();
    initScrollEvents();
    initScrollTo();
    initScorecard();
    initPopups();
    initDevTools();
})();