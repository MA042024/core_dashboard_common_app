

openEditQueryModal = function () {
    var $recordRow = $(this).closest('tr');

    $('.'+functional_object+'-id').val($recordRow.attr("objectid"));
    $("#rename-persistent-query-modal").modal("show");

    // get query old name
    var persistent_query_name = $.trim($recordRow.find('.persistent-query-name').text())

    // set old name on the popup
    if (persistent_query_name != 'None'){
        $("#query_name").val(persistent_query_name)
    }
    else  $("#query_name").val("")

    // get persistent query class
    var persistent_query_class_name = $('.nav-tabs .active').attr("title")

    // get only the type of the query e.g : example, keyword ...
    var query_type = $("#persistent-query-type").val()

    // get persistent query id
    var persistent_query_id = getSelectedDocument()

    // FIXME : make the redirect url correctly

    // make REST API link
    renameUrl =  window.origin+"/explore/"+query_type+"/rest/persistent_query_"+query_type+"/"+persistent_query_id+"/"
};

/**
 * AJAX call, edit a query
 * @param result_id
 */

edit_document = function(){
	$.ajax({
        url : renameUrl,
        type : "PATCH",
        dataType: "json",
        data : {
            "name": $("#query_name").val()

        },
		success: function(data){
		         location.reload(true);
	    },
        error:function(data){
            $("#edit_query_errors").html(JSON.parse(data.responseText).message.name);
            $("#edit_query_banner_errors").show(500)
        }
    });
};

$(".edit-query-btn").on('click', openEditQueryModal);
$('#edit-query-save').on('click', edit_document);


