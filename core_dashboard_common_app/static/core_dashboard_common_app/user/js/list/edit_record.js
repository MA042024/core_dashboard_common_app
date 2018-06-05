/**
 * Get the URL to go to the edit page
 */
openEditRecord = function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");

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
            var myArr = JSON.parse(data.responseText);
            $.notify(myArr.message, {style: myArr.tags });
        }
    });
};

$(".edit-record-btn").on('click', openEditRecord);