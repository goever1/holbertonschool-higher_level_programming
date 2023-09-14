const tag = document.getElementById('red_header');
const header = document.querySelector('header');
tag.addEventListener('click', () => {
  header.classList.toggle('red');
});
