document.addEventListener('DOMContentLoaded', () => {
    // Handle Login Form
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = loginForm.querySelector('.submit-btn');
            simulateLoading(btn, 'Connexion en cours...', () => {
                alert('Connexion réussie ! (Simulation)');
                // Redirect or actual login logic here
            });
        });
    }

    // Handle Register Form
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const password = document.getElementById('password').value;
            const confirm = document.getElementById('confirm-password').value;

            if (password !== confirm) {
                showError('Les mots de passe ne correspondent pas.');
                return;
            }

            const btn = registerForm.querySelector('.submit-btn');
            simulateLoading(btn, 'Création du compte...', () => {
                alert('Compte créé avec succès ! (Simulation)');
                // Redirect or logic here
            });
        });
    }

    // Input Focus Effects (Optional - enhanced CSS handles most)
    const inputs = document.querySelectorAll('.form-input');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.parentElement.classList.add('focused');
        });
        input.addEventListener('blur', () => {
            if (input.value === '') {
                input.parentElement.classList.remove('focused');
            }
        });
    });
});

function simulateLoading(btn, loadingText, callback) {
    const originalText = btn.innerText;
    btn.innerText = loadingText;
    btn.style.opacity = '0.7';
    btn.style.cursor = 'wait';
    btn.disabled = true;

    // Simulate network delay
    setTimeout(() => {
        btn.innerText = originalText;
        btn.style.opacity = '1';
        btn.style.cursor = 'pointer';
        btn.disabled = false;
        callback();
    }, 1500);
}

function showError(message) {
    const existingError = document.querySelector('.error-toast');
    if (existingError) existingError.remove();

    const toast = document.createElement('div');
    toast.className = 'error-toast';
    toast.innerText = message;
    
    // Style the toast dynamically or add class if CSS exists
    Object.assign(toast.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        background: '#ef4444',
        color: 'white',
        padding: '1rem 1.5rem',
        borderRadius: '8px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
        zIndex: '1000',
        animation: 'slideIn 0.3s ease-out'
    });

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'slideOut 0.3s ease-in forwards';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Add animations for toast
const styleSheet = document.createElement("style");
styleSheet.innerText = `
@keyframes slideIn {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}
@keyframes slideOut {
    from { transform: translateX(0); opacity: 1; }
    to { transform: translateX(100%); opacity: 0; }
}
`;
document.head.appendChild(styleSheet);
