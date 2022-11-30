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
        check_button.style.display = 'block';
        document.querySelectorAll(`.time${day_id}`).forEach(row => {
            row.querySelector('span').style.display = 'none';
            row.querySelector('input').style.display = 'block';
        })
        button.style.display = 'none';
    
        check_button.addEventListener('click', function(e) {
            e.preventDefault();
            const row = document.querySelector(`#row${day_id}`);
            const start = row.querySelector(`#start${day_id}`).value;
            const lunch_in = row.querySelector(`#lunch_in${day_id}`).value;
            const lunch_out = row.querySelector(`#lunch_out${day_id}`).value;
            const end = row.querySelector(`#end${day_id}`).value;

            if (start && lunch_in){
                if (lunch_out && end) {
                    console.log("work all day");
                }
                else if (!lunch_out && !end){
                    (console.log("work in the morning olny"));
                }
                else {
                    console.log("incomplete day");
                }
            }
            else if (!start && !lunch_in) {
                if (lunch_out && end) {
                    console.log("work in the afternoon");
                }
                else if (!lunch_out && !end){
                    console.log("work not at all");
                }
                else {
                    console.log("incomplete day");
                }
            }
            else if (start && !lunch_in ) {
                if (!lunch_out && end){
                    console.log("work all day without launch pause");
                }
                else {
                    console.log("incomplete day");
                }
            }
            else {
                console.log("incomplete day");
            }
            
      
            return false;
        })
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

// function validateFormEdit() {
//     alert("i am here")
//     // e.preventDefault();
//     // const date = document.forms['update_time'];
//     const forms = document.querySelectorAll(".update_time")
//     // const hhh = date['start'].value
//     consolee.log(forms)
//     if (date['start'].value === null || date['start'].value === "") {
//         alert('Please choose a start time.');
//         return false;
//     }
// };
 
