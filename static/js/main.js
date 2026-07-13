// ===== Navbar User Dropdown =====
document.addEventListener('DOMContentLoaded', function() {
    const userMenuBtn = document.getElementById('userMenuBtn');
    const userDropdown = document.getElementById('userDropdown');
    
    if (userMenuBtn && userDropdown) {
        userMenuBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            userDropdown.classList.toggle('show');
        });
        
        document.addEventListener('click', function() {
            userDropdown.classList.remove('show');
        });
    }
    
    // Mobile Menu
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    const closeMobileMenu = document.getElementById('closeMobileMenu');
    
    if (mobileMenuToggle && mobileMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            mobileMenu.classList.add('active');
        });
        
        closeMobileMenu.addEventListener('click', function() {
            mobileMenu.classList.remove('active');
        });
        
        // Fechar ao clicar em um link
        const mobileLinks = document.querySelectorAll('.mobile-nav-link');
        mobileLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
            });
        });
    }
    
    // Close Messages
    const closeMessageBtns = document.querySelectorAll('.close-message');
    closeMessageBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const message = this.closest('.message');
            message.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => message.remove(), 300);
        });
    });

    // Theme toggle (Dark/Light) - persisted em localStorage
    const body = document.body;
    const themeToggle = document.getElementById('themeToggle');
    const themeToggleMobile = document.getElementById('themeToggleMobile');
    const themeIcon = document.getElementById('themeToggleIcon');

    const applyTheme = (theme) => {
        if (theme === 'light') {
            body.classList.add('light-mode');
            if (themeIcon) themeIcon.className = 'fas fa-sun';
            if (themeToggleMobile) themeToggleMobile.innerHTML = '<i class="fas fa-sun"></i> Modo claro';
            localStorage.setItem('theme', 'light');
        } else {
            body.classList.remove('light-mode');
            if (themeIcon) themeIcon.className = 'fas fa-moon';
            if (themeToggleMobile) themeToggleMobile.innerHTML = '<i class="fas fa-moon"></i> Modo noturno';
            localStorage.setItem('theme', 'dark');
        }
    };

    const storedTheme = localStorage.getItem('theme');
    if (storedTheme === 'dark') {
        applyTheme('dark');
    } else if (storedTheme === 'light') {
        applyTheme('light');
    } else {
        // Padrão do projeto: escuro
        applyTheme('dark');
    }

    const toggleTheme = () => {
        const isLight = body.classList.contains('light-mode');
        applyTheme(isLight ? 'dark' : 'light');
    };

    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    if (themeToggleMobile) {
        themeToggleMobile.addEventListener('click', toggleTheme);
    }
    
    // Auto-hide messages after 5 seconds
    setTimeout(() => {
        const messages = document.querySelectorAll('.message');
        messages.forEach(message => {
            message.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => message.remove(), 300);
        });
    }, 5000);

    // Navbar search (Netflix-like expand)
    const navSearchBtn = document.getElementById('navSearchBtn');
    const navSearchInput = document.getElementById('navSearchInput');
    const navSearchForm = navSearchInput ? navSearchInput.closest('form') : null;
    const closeSearchIfEmpty = () => {
        if (!navSearchForm || !navSearchInput) return;
        if (!navSearchInput.value) navSearchForm.classList.remove('is-open');
    };

    if (navSearchBtn && navSearchInput && navSearchForm) {
        navSearchBtn.addEventListener('click', () => {
            const opened = navSearchForm.classList.contains('is-open');
            const hasQuery = navSearchInput.value.trim().length > 0;
            if (opened && hasQuery) {
                navSearchForm.submit();
                return;
            }
            navSearchForm.classList.add('is-open');
            setTimeout(() => navSearchInput.focus(), 0);
        });

        navSearchInput.addEventListener('focus', () => navSearchForm.classList.add('is-open'));
        navSearchInput.addEventListener('blur', closeSearchIfEmpty);

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                navSearchForm.classList.remove('is-open');
                navSearchInput.blur();
            }
        });
    }

    // Categorias (modal no topo)
    const categoriesBtn = document.getElementById('navCategoriesBtn');
    const categoriesBtnMobile = document.getElementById('navCategoriesBtnMobile');
    const categoriesModal = document.getElementById('categoryMore');
    const categoriesClose = document.getElementById('categoryMoreClose');
    const categoriesBackdrop = document.getElementById('categoryMoreBackdrop');

    if (categoriesModal && (categoriesBtn || categoriesBtnMobile)) {
        const setExpanded = (val) => {
            if (categoriesBtn) categoriesBtn.setAttribute('aria-expanded', val ? 'true' : 'false');
            if (categoriesBtnMobile) categoriesBtnMobile.setAttribute('aria-expanded', val ? 'true' : 'false');
        };

        function openCategories() {
            categoriesModal.hidden = false;
            setExpanded(true);
            document.body.style.overflow = 'hidden';
            const first = categoriesModal.querySelector('.category-more-item');
            if (first) first.focus?.();
        }

        function closeCategories() {
            categoriesModal.hidden = true;
            setExpanded(false);
            document.body.style.overflow = '';
        }

        const toggleCategories = () => {
            if (categoriesModal.hidden) openCategories();
            else closeCategories();
        };

        if (categoriesBtn) categoriesBtn.addEventListener('click', toggleCategories);
        if (categoriesBtnMobile) categoriesBtnMobile.addEventListener('click', () => {
            toggleCategories();
            if (mobileMenu) mobileMenu.classList.remove('active');
        });
        if (categoriesClose) categoriesClose.addEventListener('click', closeCategories);
        if (categoriesBackdrop) categoriesBackdrop.addEventListener('click', closeCategories);

        document.addEventListener('keydown', (e) => {
            if (!categoriesModal.hidden && e.key === 'Escape') closeCategories();
        });
    }

    // ===== Password Toggle =====
    const togglePasswordBtns = document.querySelectorAll('.toggle-password');
    togglePasswordBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const input = document.getElementById(targetId);
            const icon = this.querySelector('i');
            
            if (input && input.type === 'password') {
                input.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else if (input) {
                input.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });

    // ===== Password Strength =====
    const passwordInput = document.getElementById('id_password1');
    const strengthFill = document.getElementById('passwordStrengthFill');
    const strengthText = document.getElementById('passwordStrengthText');
    
    if (passwordInput && strengthFill && strengthText) {
        passwordInput.addEventListener('input', function() {
            const val = this.value;
            let strength = 0;
            
            if (val.length >= 6) strength += 1;
            if (val.match(/[A-Z]/)) strength += 1;
            if (val.match(/[0-9]/)) strength += 1;
            if (val.match(/[^A-Za-z0-9]/)) strength += 1;
            
            strengthFill.className = 'password-strength-fill';
            
            if (val.length === 0) {
                strengthFill.style.width = '0';
                strengthText.textContent = 'Digite uma senha forte';
            } else if (strength <= 1) {
                strengthFill.classList.add('strength-weak');
                strengthText.textContent = 'Fraca';
            } else if (strength === 2) {
                strengthFill.classList.add('strength-fair');
                strengthText.textContent = 'Razoável';
            } else if (strength === 3) {
                strengthFill.classList.add('strength-good');
                strengthText.textContent = 'Boa';
            } else {
                strengthFill.classList.add('strength-strong');
                strengthText.textContent = 'Forte';
            }
        });
    }
});

// Animation for slide out
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ===== Smooth Scroll =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===== Search Enhancement =====
const searchInput = document.querySelector('.search-input');
if (searchInput) {
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            this.closest('form').submit();
        }
    });
}

// ===== Lazy Loading Images =====
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// ===== Card Animations on Scroll =====
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const cardObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '0';
            entry.target.style.transform = 'translateY(30px)';
            
            setTimeout(() => {
                entry.target.style.transition = 'all 0.5s ease';
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, 100);
            
            cardObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.establishment-card, .evento-card').forEach(card => {
    cardObserver.observe(card);
});

// ===== Form Validation Enhancement =====
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (!this.value.trim()) {
                this.style.borderColor = 'var(--error-color)';
            } else {
                this.style.borderColor = 'var(--border-color)';
            }
        });
        
        input.addEventListener('input', function() {
            if (this.value.trim()) {
                this.style.borderColor = 'var(--border-color)';
            }
        });
    });
});

// ===== Utilities =====
function showNotification(message, type = 'info') {
    const messagesContainer = document.querySelector('.messages-container') || createMessagesContainer();
    
    const icons = {
        success: 'fa-check-circle',
        error: 'fa-exclamation-circle',
        warning: 'fa-exclamation-triangle',
        info: 'fa-info-circle'
    };
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${type}`;
    messageDiv.innerHTML = `
        <i class="fas ${icons[type]}"></i>
        <span>${message}</span>
        <button class="close-message">
            <i class="fas fa-times"></i>
        </button>
    `;
    
    messagesContainer.appendChild(messageDiv);
    
    messageDiv.querySelector('.close-message').addEventListener('click', function() {
        messageDiv.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => messageDiv.remove(), 300);
    });
    
    setTimeout(() => {
        if (messageDiv.parentElement) {
            messageDiv.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => messageDiv.remove(), 300);
        }
    }, 5000);
}

function createMessagesContainer() {
    const container = document.createElement('div');
    container.className = 'messages-container';
    document.body.appendChild(container);
    return container;
}

// ===== Loading State =====
function showLoading() {
    const loadingDiv = document.createElement('div');
    loadingDiv.id = 'loading-overlay';
    loadingDiv.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner"></div>
            <p>Carregando...</p>
        </div>
    `;
    loadingDiv.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
    `;
    document.body.appendChild(loadingDiv);
}

function hideLoading() {
    const loadingDiv = document.getElementById('loading-overlay');
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

// ===== Image Preview =====
function previewImage(input, previewId) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            document.getElementById(previewId).src = e.target.result;
        };
        
        reader.readAsDataURL(input.files[0]);
    }
}

// ===== Debounce Function =====
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ===== Scroll to Top Button =====
window.addEventListener('scroll', function() {
    if (window.scrollY > 500) {
        if (!document.getElementById('scrollTopBtn')) {
            const btn = document.createElement('button');
            btn.id = 'scrollTopBtn';
            btn.innerHTML = '<i class="fas fa-arrow-up"></i>';
            btn.style.cssText = `
                position: fixed;
                bottom: 2rem;
                right: 2rem;
                width: 50px;
                height: 50px;
                background: var(--primary-color);
                color: white;
                border: none;
                border-radius: 50%;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                transition: all 0.3s ease;
                z-index: 900;
            `;
            btn.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
            btn.addEventListener('mouseenter', () => {
                btn.style.transform = 'translateY(-4px)';
                btn.style.boxShadow = '0 8px 20px rgba(0, 0, 0, 0.2)';
            });
            btn.addEventListener('mouseleave', () => {
                btn.style.transform = 'translateY(0)';
                btn.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
            });
            document.body.appendChild(btn);
        }
    } else {
        const btn = document.getElementById('scrollTopBtn');
        if (btn) btn.remove();
    }
});

// ===== Live Search (AJAX) =====
const liveSearchInputs = document.querySelectorAll('.live-search-input');
liveSearchInputs.forEach(input => {
    let debounceTimer;
    const resultsContainer = input.parentElement.querySelector('.search-dropdown-results');
    
    input.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        const query = this.value.trim();
        
        if (query.length < 2) {
            resultsContainer.style.display = 'none';
            return;
        }
        
        debounceTimer = setTimeout(() => {
            fetch(`/buscar-ajax/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    resultsContainer.innerHTML = '';
                    if (data.results && data.results.length > 0) {
                        data.results.forEach(item => {
                            const link = document.createElement('a');
                            link.href = item.url;
                            link.className = 'search-result-item';
                            
                            const placeholderIcon = item.tipo === 'evento' ? 'fa-calendar-alt' : 'fa-store';
                            const imgHTML = item.imagem 
                                ? `<img src="${item.imagem}" alt="${item.nome}" class="search-result-img">`
                                : `<div class="search-result-placeholder"><i class="fas ${placeholderIcon}"></i></div>`;
                                
                            link.innerHTML = `
                                ${imgHTML}
                                <div class="search-result-info">
                                    <span class="search-result-name">${item.nome}</span>
                                    <span class="search-result-cat">${item.categoria}</span>
                                </div>
                            `;
                            resultsContainer.appendChild(link);
                        });
                        resultsContainer.style.display = 'block';
                    } else {
                        resultsContainer.innerHTML = '<div class="search-result-empty">Nenhum resultado encontrado</div>';
                        resultsContainer.style.display = 'block';
                    }
                })
                .catch(error => console.error('Erro na busca AJAX:', error));
        }, 300); // 300ms delay debounce
    });
    
    // Esconder dropdown quando clicar fora
    document.addEventListener('click', function(e) {
        if (!input.contains(e.target) && !resultsContainer.contains(e.target)) {
            resultsContainer.style.display = 'none';
        }
    });
});

console.log('Minha Vitrine - Sistema inicializado');

