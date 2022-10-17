function showdiv(div) {
    if (document.querySelector(`#${div}`).style.display == 'block') {
        document.querySelector(`#${div}`).style.display = 'none';
    }
    else
        document.querySelector(`#${div}`).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function(button){
            showdiv(this.dataset.div)
        }
    });
});