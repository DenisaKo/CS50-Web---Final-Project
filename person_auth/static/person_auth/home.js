document.addEventListener("DOMContentLoaded", function() {
    const month_filter = document.querySelector('#id_month');
    let selected_month = parseInt(month_filter.value);
    const year_filter = document.querySelector('#id_year');
    let selected_year = parseInt(year_filter.value);
    getFilterAplly(selected_month, selected_year)

    month_filter.addEventListener('change', function() {
        selected_month = parseInt(month_filter.value);
        getFilterAplly(selected_month, selected_year)
    });
    
    year_filter.addEventListener('change', function() {
        selected_year = parseInt(year_filter.value);
        getFilterAplly(selected_year, selected_year)
    });

});

const modal = document.querySelector('#exampleModal');
const pic_first = modal.querySelector('#id_pic_first');
const sequence = modal.querySelector('#id_random_sequence');
const avatar = modal.querySelector('#avatar');

pic_first.addEventListener('change', function() {
    avatar.src = `https://avatars.dicebear.com/api/${pic_first.value}/{{profile.random_sequence}}.svg?h=256&w=256`;
    
});
sequence.addEventListener('keyup', function() {
    avatar.src = `https://avatars.dicebear.com/api/${pic_first.value}/${sequence.value}.svg?h=256&w=256`;
    console.log(sequence.value);
});

const date = document.querySelector('#id_date');
date.readOnly = true;

const actual_month = parseInt(document.querySelector('#actual_month').getAttribute('data-month'));
const select = document.querySelector('#id_month');
const options = select.querySelectorAll('option');
// console.log(options)
options.forEach(option => {
    if (parseInt(option.value) === actual_month) {
        option.setAttribute('selected', 'selected')
    }
});

const actual_year = parseInt(document.querySelector('#actual_year').getAttribute('data-year'));
const select_year = document.querySelector('#id_year');
const options_year = select_year.querySelectorAll('option');
options_year.forEach(option => {
    if (parseInt(option.value) === actual_year) {
        option.setAttribute('selected', 'selected')
    }
});


function getFilterAplly(selected_month, selected_year) {
    const card = document.querySelector('#hours_card');
    const rows = card.querySelectorAll('.section');
    rows.forEach(row => {
        row.style.display = 'block';
        let month = parseInt(row.querySelector('.month > span').textContent);
        let year = parseInt(row.querySelector('.year > span').textContent);
        if (month === selected_month && year === selected_year) {
            row.style.display = 'table-row'
        } else {
            row.style.display = 'none'
        }
    });  
};

