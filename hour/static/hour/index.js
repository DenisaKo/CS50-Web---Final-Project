// get data from a table filter input, add a listener for a change 
document.addEventListener("DOMContentLoaded", function() {
    const month_filter = document.querySelector('#id_month');
    let selected_month = parseInt(month_filter.value);
    const year_filter = document.querySelector('#id_year');
    let selected_year = parseInt(year_filter.value);

    month_filter.addEventListener('change', function() {
        selected_month = parseInt(month_filter.value);
        getFilterAplly(selected_month, selected_year)
    });

    year_filter.addEventListener('change', function() {
        selected_year = parseInt(year_filter.value);
        getFilterAplly(selected_month, selected_year)
    });

    getFilterAplly(selected_month, selected_year);
});

//  get date form a form and send them for a validation, creating a day in a modal
const form = document.querySelector('#day_input')
form.addEventListener('submit', function (e) {
    // e.preventDefault();
    const inputs = form.querySelectorAll('input');
    const date = inputs[1].value;
    const start = inputs[2].value;
    const lunch_in = inputs[3].value;
    const lunch_out = inputs[4].value;
    const end = inputs[5].value;

    if (date === null || date === ""){
        alert('Please choose a date.');
        return false;
    };
    // do not send data if input is not valid
    if (input_validate(start, lunch_in, lunch_out, end) === false){
        e.preventDefault();
        return false;
    };
});

// display data in a table according to the user's filter selection
function getFilterAplly(selected_month, selected_year) {
    const table_rows = document.querySelectorAll('.table > tbody > tr');
    table_rows.forEach(row => {
        row.style.display = 'table-row';

        // get date for each row
        let date_string = row.querySelector('.span_date').textContent;
        let column = date_string.split(".");
        // get id, if day is public hodiday and if day is already complete
        let day_id = row.getAttribute('data-id');
        let public_holiday = row.querySelector(`#span_public_holiday${day_id}`).getAttribute('data-pub');
        let complete_day = row.querySelector(`#span_completed${day_id}`).getAttribute('data-completed');

        // create an data object
        let date = new Date(column[2].concat('.',column[1]).concat('.', column[0]));
        let day_index = date.getDay();

        // check if it's weekend day/public holiday, make them green, if incomplete day - stay red
        if (complete_day === 'True') {
            if (day_index === 0 || day_index === 6) {
                row.style.backgroundColor = 'rgba(0, 170, 170, 0.4)';
            } else if (public_holiday === 'true') {
                row.style.backgroundColor = 'rgba(0, 170, 170, 0.4)';
            };
        };
        
        // display only selected data
        let month = parseInt(column[1])
        let year = parseInt(column[2])
        if (month === selected_month && year === selected_year) {
            row.style.display = 'table-row'
        } else {
            row.style.display = 'none'
        };
    });  
};

// check and delete button behavoir
document.querySelectorAll(".edit").forEach(button => {
    button.addEventListener('click', function(e){
        e.preventDefault();
        const day_id = button.value;
        const check_button = document.getElementById(`save_edit${day_id}`)
        const cancel_button = document.getElementById(`cancel_edit${day_id}`)
        check_button.style.display = 'block';
        cancel_button.style.display = 'block';
        cancel_button.style.marginTop = "5px";
        const all_inputs = document.querySelectorAll(`.time${day_id}`);
        all_inputs.forEach(row => {
            row.querySelector('span').style.display = 'none';
            row.querySelector(':scope > input').style.display = 'block';
        })
        button.style.display = 'none';

        cancel_button.addEventListener('click', function(){
            all_inputs.forEach(row => {
                row.querySelector('span').style.display = 'block';
                row.querySelector(':scope > input').style.display = 'none';
            })
            check_button.style.display = 'none';
            cancel_button.style.display = 'none';
            button.style.display = 'block';
        });

        check_button.addEventListener('click', function(e) {
            e.preventDefault();
            if (validateFormEdit(day_id) === false) {
                return false;
            } else {
                all_inputs.forEach(row => {
                    row.querySelector('span').style.display = 'block';
                    row.querySelector(':scope > input').style.display = 'none';
                })
                check_button.style.display = 'none';
                cancel_button.style.display = 'none';
                button.style.display = 'block';
            };
        });
    });
});

//  get data from the form and send them for a validation, the updating day in a table
function validateFormEdit(day_id) {
            // e.preventDefault();
    const row = document.querySelector(`#row${day_id}`);
    const start = row.querySelector(`#start${day_id}`).value;
    const lunch_in = row.querySelector(`#lunch_in${day_id}`).value;
    const lunch_out = row.querySelector(`#lunch_out${day_id}`).value;
    const end = row.querySelector(`#end${day_id}`).value;
    const public_holiday = row.querySelector(`#public_holiday${day_id}`).checked;

    if (input_validate(start, lunch_in, lunch_out, end) === false){
        return false;
    } else {
        edit_time_input(day_id, start, lunch_in, lunch_out, end, public_holiday);
    };
};

// get cookie variable
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

// fetch data after user update day in a calendar
function edit_time_input(day_id, start, lunch_in, lunch_out, end, public_holiday) {

    const csrftoken = getCookie('csrftoken');
    fetch(`update_day/${day_id}/`, {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin', // Do not send CSRF token to another domain.
        body: JSON.stringify({
            start: start,
            lunch_in: lunch_in,
            lunch_out: lunch_out,
            end: end,
            public_holiday: public_holiday
        })
    })
    .then(response => response.json())
    .then(data => {
       
        const old_row = document.querySelector(`#row${day_id}`);
        const old_completed = document.querySelector(`#span_completed${day_id}`);
        const old_start = old_row.querySelector(`#span_start${day_id}`);
        const old_lunch_in = old_row.querySelector(`#span_lunch_in${day_id}`);
        const old_lunch_out = old_row.querySelector(`#span_lunch_out${day_id}`);
        const old_end = old_row.querySelector(`#span_end${day_id}`);
        const old_required = old_row.querySelector(`#span_required${day_id}`);
        const old_extra = old_row.querySelector(`#span_extra${day_id}`);
        const old_public_holiday = old_row.querySelector(`#span_public_holiday${day_id}`);
    
        const new_start = document.createElement('span');
        new_start.append(data.day.start);
        const new_lunch_in = document.createElement('span');
        new_lunch_in.append(data.day.lunch_in);
        const new_lunch_out = document.createElement('span');
        new_lunch_out.append(data.day.lunch_out);
        const new_end = document.createElement('span');
        new_end.append(data.day.end);
        const new_required = document.createElement('span');
        new_required.append(data.day.required);
        const new_extra = document.createElement('span');
        new_extra.append(data.day.extra);
        const new_completed = document.createElement('span');
        new_completed.append("");

        const new__input_public_holiday = document.createElement('input');
        new__input_public_holiday.type = 'checkbox';
        new__input_public_holiday.checked = data.day.public_holiday;
        new__input_public_holiday.disabled = 'disabled';

        old_start.replaceChildren(new_start);
        old_lunch_in.replaceChildren(new_lunch_in);
        old_lunch_out.replaceChildren(new_lunch_out);
        old_end.replaceChildren(new_end);
        old_required.replaceChildren(new_required);
        old_extra.replaceChildren(new_extra);
        old_completed.replaceChildren(new_completed);
        old_public_holiday.replaceChildren(new__input_public_holiday);

        old_row.style.backgroundColor = 'lightgreen';
        
    });
};

// validation if inputed date resulted in a valid day in a calendar
function input_validate(start, lunch_in, lunch_out, end) {  
    if (start && lunch_in){
        if (check_time(start, lunch_in)) {
            if (lunch_out && end) {
                if (check_time(lunch_in, lunch_out) && check_time(lunch_out, end)) {
                    console.log("work all day");
                } else {
                    alert("wrong time input");
                    return false;
                }
            } else if (!lunch_out && !end){
                (console.log("work in the morning olny"));
            } else {
                alert("incomplete day");
                return false;
            }
        } else {
            alert("wrong time input");
            return false;
        }
    } else if (!start && !lunch_in) {
        if (lunch_out && end) {
            if (check_time(lunch_out, end)) {
                console.log("work in the afternoon");
            } else {
                alert("wrong time input");
                return false;
            }
        } else if (!lunch_out && !end){
            console.log("work not at all");
        } else {
            alert("incomplete day");
            return false;
        }
    } else if (start && !lunch_in ) {
        if (!lunch_out && end){
            if (check_time(start, end)) {
                console.log("work all day without launch pause");
            } else {
                alert("wrong time input");
                return false;
            }
        } else {
            alert("incomplete day");
            return false;
        }
    } else {
        alert("incomplete day");
        return false;
    };
};

// validation if inputed date resulted in a valid time of the day
function check_time(input_time, output_time) {
    if (input_time > output_time) {
        return false;
    };
    return true;
};

// set an actual month in the table filter
const actual_month = parseInt(document.querySelector('#actual_month').getAttribute('data-month'));
const select_month = document.querySelector('#id_month');
const options_month = select_month.querySelectorAll('option');
options_month.forEach(option => {
    if (parseInt(option.value) === actual_month) {
        option.setAttribute('selected', 'selected')
    }
});

// set an actual year in a table filter
const actual_year = parseInt(document.querySelector('#actual_year').getAttribute('data-year'));
const select_year = document.querySelector('#id_year');
const options_year = select_year.querySelectorAll('option');
options_year.forEach(option => {
    if (parseInt(option.value) === actual_year) {
        option.setAttribute('selected', 'selected')
    }
});

// make table filter requirements visible after clicking of the button
const filter_button = document.querySelector('#filter_button');
const filter = document.querySelector('#open_filter');
filter.style.display = 'none';
filter_button.addEventListener('click', function() {
    if (filter.style.display === 'none') {
        filter.style.display = 'block';
    } else {
        filter.style.display = 'none';
    }
});


