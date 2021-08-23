

    
    $('#add-author').click(function () {
        window.open('/items/add_author/', '_blank', 'height=400,width=500,left=300,top=200', true);
    })   


parent.addEventListener("focus", function(){

    // CREDIT jcubic stackoverflow

    window.onbeforeunload = function() {
        window.sessionStorage.setItem("title", $('#id_title').val());
    
};

location.reload();
});

parent.onload = function() {

    let fillTitle = sessionStorage.getItem("title");
    if (fillTitle !== null) $('#id_title').val(fillTitle);

    // ...
}

function closeSubmit(){
    setTimeout(() => {
        window.close()
    }, 100);
}
