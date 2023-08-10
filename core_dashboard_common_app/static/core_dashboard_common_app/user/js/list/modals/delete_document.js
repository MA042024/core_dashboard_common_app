
/**
 * Open the modal before deleting the document
 */
openDeleteDocument = function () {
    var $recordRow = $(this).closest('tr');
    $('.'+functional_object+'-id').val($recordRow.attr("objectid"));
    $("#delete_banner_errors").hide();
    $("#delete-result-modal").modal("show");
};

/**
 * AJAX call, delete a curated document
 * @param result_id
 */
delete_document = function(){
    var icon = $("[id^='delete-document-yes'] > i").attr("class");
    // Show loading spinner
    showSpinner($("[id^='delete-document-yes'] > i"))
	$.ajax({
        url : dashboardDeleteDocumentUrl,
        type : "POST",
        dataType: "json",
        data : {
        	document_id: getSelectedDocument(),
            functional_object: functional_object,

            // get query class name
            document_type: $('.nav-tabs .active').attr("title")

        },
		success: function(data){
            location.reload();
	    },
        error:function(data){
            $("#delete-result-modal").modal("hide");
            let error_message = JSON.parse(data.responseText);
            $.notify(error_message.message, "danger");
        }
    }).always(function() {
        // get old button icon
        hideSpinner($("[id^='delete-document-yes'] > i"), icon)
    });
};


$('.delete-document-btn').on('click', openDeleteDocument);
$('#delete-document-yes').on('click', delete_document);
