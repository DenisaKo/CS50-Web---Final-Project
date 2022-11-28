function validateForm() {
    const date = document.forms['input_form']['date'].value
    if (date === null || date === ""){
        alert('Please choose a date.');
        return false;
    };
};

document.querySelectorAll(".edit").forEach(button => {
    button.addEventListener('click', function(e){
        e.preventDefault();
        day_id = button.value;
        document.getElementById(`save_edit${day_id}`).style.display='block';
        document.querySelectorAll(`.time${day_id}`).forEach(row => {
            row.querySelector('span').style.display = 'none';
            row.querySelector('input').style.display = 'block';
        })
        button.style.display = 'none';
        // const whole_form = document.querySelector('.update_time')
        // whole_form.querySelectorAll('.time_start').defaultValue = "{{day.start | time:'H:i'}}"
    })
});

// document.querySelectorAll('.change_time').forEach(form => {
//     form.addEventListener('submit', function(e) {
//         e.preventDefault();
//         console.log(form);
//     })
// })

