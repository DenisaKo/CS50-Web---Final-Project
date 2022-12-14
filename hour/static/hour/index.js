// document.addEventListener("DOMContentLoaded", function() {
//     getFilterAplly()
// });

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
    if (input_validate(start, lunch_in, lunch_out, end) === false){
        return false;
    };
 
});


// function getFilterAplly() {
//     const columns_filter = document.querySelectorAll('.table-filter');
//     columns_filter.forEach(column => {
//         let index = column.parentElement.getAttribute('data-index');
//         console.log(index)
//     })
// };

const month_filter = document.querySelector('#id_month');
month_filter.addEventListener('change', function() {
    const val = month_filter.value;
    console.log(val);
});


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
        // const old_public_holiday = old_row.querySelector(`#span_input_public_holiday${day_id}`);



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
        // old_public_holiday.replaceChildren(new_public_holiday);
        old_public_holiday.replaceChildren(new__input_public_holiday);

        old_row.style.backgroundColor = "lightgreen";
        
    });
};


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


function check_time(input_time, output_time) {
    if (input_time > output_time) {
        return false;
    };
    return true;
};



