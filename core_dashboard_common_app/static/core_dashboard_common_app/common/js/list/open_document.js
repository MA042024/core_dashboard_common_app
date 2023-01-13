/**
 * Open document for text editor.
 */

$(".open-template-btn").on('click',function(){
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("object-id");
    showSpinner($(this).find("i"))
    window.location = openTemplateUrl + '?id=' + objectID;
});


$(".open-record-btn").on('click',function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");
    showSpinner($(this).find("i"))
    window.location = openRecordUrl + '?id=' + objectID;
});

$(".open-form-btn").on('click',function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");
    showSpinner($(this).find("i"))
    window.location = openFormUrl + '?id=' + objectID;
});

