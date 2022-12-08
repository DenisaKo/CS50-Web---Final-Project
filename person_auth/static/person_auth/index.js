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
// console.log(pic_first)