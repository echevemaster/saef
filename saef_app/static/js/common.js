$(function()
{
    function delete_item(id,url) {
        var id = id;
        $('#dialog-confirm').dialog({
            resizable:false,
            height:200,
            modal: true,
            buttons: {
                "Eliminar?": function() {
                    $.get(url, { item : id } );
                },
                Cancelar: function() {
                    $(this).dialog("close");
                }
            }

        })
    };

    $(function()
        $(".delete_item_user").click(function() {
            delete_item(this.id,"/admin/user/delete")
         }
        )
    )
});