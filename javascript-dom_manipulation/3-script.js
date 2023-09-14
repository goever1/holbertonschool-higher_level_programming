let text_color = document.querySelector('header');
let toggle_color = document.querySelector('#toggle_header');

toggle_color.addEventListener('click', color_header);

function color_header() {
  text_color.classList.toggle('red');
  text_color.classList.toggle('green');
};
