Pconst modal = document.querySelector('.modal');

const showModal = document.querySelector('.show-modal');
const closeModal = document.querySelectorAll('.close-modal');

showModal.addEventListener('click', function (){
    modal.classList.remove('hidden')
});

closeModal.forEach(close => {
    close.addEventListener('click', function (){
    modal.classList.add('hidden')
    });
});
var id = -1
$('#addressTable').find('tr').click( function(){
    id = this.children[0].innerText
    $("#address").val(id)
    });

$('#update_but').click( function(){
    $("#address").prop("disabled",false)
    
})