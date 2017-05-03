function confirmAlbumDelete(varList)
{
    var elt= varList.split(',');
    $(".modal-body #hiddenValue").val(elt[0]);
    $(".modal-body #img").attr("src",elt[1]);
    $(".modal-body #albumName").text(elt[2]);
    $(".modal-body #artist").text(elt[3]);
    $(".modal-body #genre").text(elt[4]);
}

function albumDelete()
{
    var id=$(".modal-body #hiddenValue").val();
    var form_id='#fd-'+id
    $(form_id).submit();
    $('#confirm-submit').modal('toggle');
}