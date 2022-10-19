// "shows hidden divs"
function showdiv(div){
    document.querySelector(`#${div}`).style.display = 'block';
}
// triggers to show hidden divs
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function(button){
            showdiv(this.dataset.div)
        }
    });
});