document.addEventListener('DOMContentLoaded', () => {
    const menuIcon = document.getElementById('menuicn');
    const navContainer = document.querySelector('.navcontainer');
    const mainContainer = document.querySelector('.main-container');
    const mainSearch = document.getElementById('mainSearch');
    const secondarySearch = document.getElementById('secondarySearch');

    menuIcon.addEventListener('click', () => {
        navContainer.classList.toggle('active');
        mainContainer.classList.toggle('shift');
    });

    const debounce = (func, delay) => {
        let debounceTimer;
        return function() {
            const context = this;
            const args = arguments;
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => func.apply(context, args), delay);
        };
    };

    const searchItems = (event) => {
        const searchTerm = event.target.value.toLowerCase();
        const items = document.querySelectorAll('.item1');
        items.forEach((item) => {
            const itemName = item.querySelector('.t-op-nextlvl').innerText.toLowerCase();
            if (itemName.includes(searchTerm)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    };

    mainSearch.addEventListener('input', debounce(searchItems, 300));
    secondarySearch.addEventListener('input', debounce(searchItems, 300));
});
