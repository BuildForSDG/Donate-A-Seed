//fetching the date
let display = document.getElementById("time")
let time = new Date()
let year = time.getFullYear()
let month = time.getUTCMonth()
let day = time.getUTCDate()
//display date on the UI
let html = '<h4>%day%.%month%.%year%<br>___<h4>'
newHtml = html.replace('%day%', day)
newHtml = newHtml.replace('%month%', month)
newHtml = newHtml.replace('%year%', year)
display.insertAdjacentHTML('afterend', newHtml)