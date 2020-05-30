// Get modal element
var modal1 = document.getElementById('simpleModal');
// get open modal button
var modalBtn = document.getElementById('modalBtn');
// get close button
var closeBtn = document.getElementsByClassName('closeBtn')[0];

//listen for open click
modalBtn.addEventListener('click', openModal);

//listen for close click
closeBtn.addEventListener('click', closeModal);

// listen for outside click
window.addEventListener('click', clickOutside);

//function to open modal
function openModal(){
    modal1.style.display = 'block';
}

//function to close modal
function closeModal(){
    modal1.style.display = 'none';
}

//function for click outside modal
function clickOutside(e){
    if(e.target == modal1){
        modal1.style.display = 'none';
    }
}