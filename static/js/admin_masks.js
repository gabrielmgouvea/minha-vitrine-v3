document.addEventListener("DOMContentLoaded", function() {
    function maskInput(inputElement, maskType) {
        if (!inputElement) return;
        
        inputElement.addEventListener("input", function(e) {
            let value = e.target.value.replace(/\D/g, ""); // Keep only numbers
            
            if (maskType === "cpf") {
                if (value.length > 11) value = value.slice(0, 11);
                
                value = value.replace(/(\d{3})(\d)/, "$1.$2");
                value = value.replace(/(\d{3})(\d)/, "$1.$2");
                value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
            } else if (maskType === "cnpj") {
                if (value.length > 14) value = value.slice(0, 14);
                
                value = value.replace(/(\d{2})(\d)/, "$1.$2");
                value = value.replace(/(\d{3})(\d)/, "$1.$2");
                value = value.replace(/(\d{3})(\d)/, "$1/$2");
                value = value.replace(/(\d{4})(\d{1,2})$/, "$1-$2");
            }
            
            e.target.value = value;
        });

        // Block non-numeric keystrokes
        inputElement.addEventListener("keypress", function(e) {
            if (!/[0-9]/.test(e.key)) {
                e.preventDefault();
            }
        });
        
        // Initial format if it already has value
        let event = new Event('input', { bubbles: true });
        inputElement.dispatchEvent(event);
    }

    const cpfInput = document.getElementById("id_cpf");
    if (cpfInput) {
        maskInput(cpfInput, "cpf");
        cpfInput.setAttribute("placeholder", "___.___.___-__");
        cpfInput.setAttribute("maxlength", "14");
    }

    const cnpjInput = document.getElementById("id_cnpj");
    if (cnpjInput) {
        maskInput(cnpjInput, "cnpj");
        cnpjInput.setAttribute("placeholder", "__.___.___/____-__");
        cnpjInput.setAttribute("maxlength", "18");
    }
});
