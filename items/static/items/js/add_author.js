$('#add-author').click(function () {
    window.open('/items/add_author/', '_blank', 'height=400,width=500,left=300,top=200', true);
})


parent.addEventListener("focus", function () {
    // CREDIT jcubic stackoverflow
    window.onbeforeunload = function () {
        window.sessionStorage.setItem("title", $('#id_title').val());
        window.sessionStorage.setItem("description", $('#id_description').val());
        window.sessionStorage.setItem("price", $('#id_price').val());
        window.sessionStorage.setItem("set_sale_price", $('#id_set_sale_price').val());
        window.sessionStorage.setItem("discount", $('#id_discount').val());
        // end credit
    };
    location.reload();
});

parent.onload = function () {
    let fillTitle = sessionStorage.getItem("title");
    let fillDescription = sessionStorage.getItem("description");
    let fillPrice = sessionStorage.getItem("price");
    let fillSetSalePrice = sessionStorage.getItem("set_sale_price");
    let fillDiscount = sessionStorage.getItem("discount");
    if (fillTitle !== null) $('#id_title').val(fillTitle);
    if (fillDescription !== null) $('#id_description').val(fillTitle);
    if (fillPrice !== null) $('#id_price').val(fillTitle);
    if (fillSetSalePrice !== null) $('#id_set_sale_price').val(fillTitle);
    if (fillDiscount !== null) $('#id_discount').val(fillTitle);
}

function closeSubmit() {
    setTimeout(() => {
        window.close()
    }, 100);
}