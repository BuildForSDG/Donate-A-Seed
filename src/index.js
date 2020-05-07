import app from './app';

const startApp = async () => {
  const header = document.querySelector('[data-app-name]');
  if (!header) return;

  const programName = await app();
  header.textContent = programName;
};

document.addEventListener('DOMContentLoaded', startApp);

window.addEventListener('load', function () {
  document.querySelector('input[type="file"]').addEventListener('change', function () {
    if (this.files && this.files[0]) {
      var img = document.querySelector('img'); // $('img')[0]
      img.src = URL.createObjectURL(this.files[0]); // set src to blob url
      img.onload = imageIsLoaded;
    }
  });
});

function imageIsLoaded() {
  alert(this.src); // blob url
  // update width and height ...
}
