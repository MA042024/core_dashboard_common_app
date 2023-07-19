/**
 * Get the URL to go to the edit page
 */
openEditRecord = function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");
    var editBtn = $(this).find( "i" )
    var icon = $(editBtn).attr("class");

    // Show loading spinner
    showSpinner($(this).find("i"))
    $.ajax({
        url : editRecordUrl,
        type : "POST",
        dataType: "json",
        data : {
            "id": objectID
        },
        success: function(data){
            window.location = data.url;
        },
        error:function(data){
            let jsonResponse = JSON.parse(data.responseText);
            $.notify(jsonResponse.message, "danger");
        }
    }).always(function() {
        // get old button icon
        hideSpinner(editBtn, icon)
    });
};

$(".edit-record-btn").on('click', openEditRecord);