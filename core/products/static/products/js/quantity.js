let minusButton = document.getElementById('minus');
let plusButton = document.getElementById('plus');
let inputField = document.getElementById('quantity');

minusButton.addEventListener('click', event => {
    event.preventDefault();
    let currentValue = Number(inputField.value) || 0;
    if (currentValue > 1) {
        inputField.value = currentValue - 1;
    } else {
        inputField.value = 1;
    }
});

plusButton.addEventListener('click', event => {
    event.preventDefault();
    let currentValue = Number(inputField.value) || 0;
    inputField.value = currentValue + 1;
});