// fetching the date
const display = document.getElementById('time');
const time = new Date();
const year = time.getFullYear();
const month = time.getUTCMonth();
const day = time.getUTCDate();
// display date on the UI
const html = '<h4>%day%.%month%.%year%<br>___<h4>';
let newHtml = html.replace('%day%', day);
newHtml = newHtml.replace('%month%', month);
newHtml = newHtml.replace('%year%', year);
display.insertAdjacentHTML('afterend', newHtml);
