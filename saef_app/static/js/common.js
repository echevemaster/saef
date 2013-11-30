$(function()
{
    function delete_item(id,url,url_redirect) {
        var id = id;
        $('#dialog-confirm').dialog({
            resizable:false,
            height:200,
            modal: true,
            buttons: {
                "Eliminar?": function() {
                    $.get(url, { item : id }, function(){ 
                        window.location.replace(url_redirect)
                    });
                },
                Cancelar: function() {
                    $(this).dialog("close");
                }
            }

        })
    };

    $(function()
        $(".delete_item_user").click(function() {
            delete_item(this.id,"/admin/user/delete","/admin/user")
         }
        )
    )

    $(function()
        $(".delete_item_category").click(function() {
            delete_item(this.id,"/admin/category/delete","/admin/categories")
         }
        )
    )

});