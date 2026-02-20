/**
 * Vastu Farms Admin Portal - JavaScript
 * Sidebar collapse/expand functionality
 */

(function() {
  'use strict';

  // Storage key for sidebar state persistence
  const SIDEBAR_STATE_KEY = 'vastufarms_sidebar_collapsed';

  /**
   * Initialize sidebar collapse functionality
   */
  function initSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const collapseBtn = document.querySelector('.sidebar-collapse');
    const layout = document.querySelector('.layout');

    if (!sidebar || !collapseBtn) {
      return;
    }

    // Restore saved state
    const savedState = localStorage.getItem(SIDEBAR_STATE_KEY);
    if (savedState === 'true') {
      sidebar.classList.add('collapsed');
      if (layout) {
        layout.classList.add('sidebar-collapsed');
      }
    }

    // Toggle sidebar on button click
    collapseBtn.addEventListener('click', function() {
      const isCollapsed = sidebar.classList.toggle('collapsed');
      
      if (layout) {
        layout.classList.toggle('sidebar-collapsed', isCollapsed);
      }

      // Save state to localStorage
      localStorage.setItem(SIDEBAR_STATE_KEY, isCollapsed);
    });

    // Keyboard accessibility - toggle on Enter or Space
    collapseBtn.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        collapseBtn.click();
      }
    });
  }

  /**
   * Initialize logout functionality
   */
  function initLogout() {
    const logoutLink = document.getElementById('logoutLink');
    if (logoutLink) {
      logoutLink.addEventListener('click', function(e) {
        // Clear all messages from DOM
        const messageContainer = document.getElementById('messageContainer');
        if (messageContainer) {
          messageContainer.innerHTML = '';
        }
        // Clear session storage messages
        sessionStorage.removeItem('logout_message');
        // Clear any URL parameters that might contain messages
        const currentUrl = new URL(window.location.href);
        currentUrl.searchParams.delete('message');
        currentUrl.searchParams.delete('type');
        window.history.replaceState({}, document.title, currentUrl.pathname + currentUrl.search);
      });
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initSidebar();
      initLogout();
    });
  } else {
    initSidebar();
    initLogout();
  }
})();
