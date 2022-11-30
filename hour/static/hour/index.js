function validateForm() {
    const date = document.forms['input_form']['date'].value;
    if (date === null || date === ""){
        alert('Please choose a date.');
        return false;
    };
};


document.querySelectorAll(".edit").forEach(button => {
    button.addEventListener('click', function(e){
        e.preventDefault();
        const day_id = button.value;
        const check_button = document.getElementById(`save_edit${day_id}`)
        const cancel_button = document.getElementById(`cancel_edit${day_id}`)
        check_button.style.display = 'block';
        cancel_button.style.display = 'block';
        const all_inputs = document.querySelectorAll(`.time${day_id}`);
        all_inputs.forEach(row => {
            row.querySelector('span').style.display = 'none';
            row.querySelector('input').style.display = 'block';
        })
        button.style.display = 'none';

        cancel_button.addEventListener('click', function(){
            all_inputs.forEach(row => {
                row.querySelector('span').style.display = 'block';
                row.querySelector('input').style.display = 'none';
            })
            check_button.style.display = 'none';
            cancel_button.style.display = 'none';
            button.style.display = 'block';
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
    }

};

function check_time(input_time, output_time) {
    if (input_time > output_time) {
        return false;
    };
    return true;
};

