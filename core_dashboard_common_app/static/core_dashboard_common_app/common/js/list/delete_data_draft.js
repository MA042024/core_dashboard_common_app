/**
 * Get the URL to delete draft
 */
deleteDraft = function(deleteUrl) {
    $.ajax({
        url : deleteUrl,
        type : "DELETE",
        dataType: "json",
        success: function(data){
            location.reload();
        },
        error:function(data){
            var myArr = JSON.parse(data.responseText);
            $.notify(myArr.message, "danger");
        }
    })
};

$(".delete-draft-btn").on('click', function(){
        deleteDraft(deleteRecordDraftUrl.replace("pk",$(this).attr("objectid")))
});
$(".delete-data-draft-list-btn").on('click', function(){
        deleteDraft(deleteRecordDraftListUrl.replace("pk",$(this).attr("objectid")))
});