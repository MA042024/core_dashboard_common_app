/**
 * Open document for text editor.
 */

$(".open-template-btn").on('click',function(){
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("object-id");
    var icon = $(this).find( "i" ).attr("class");
    showSpinner($(this).find("i"))
    window.location = openTemplateUrl + '?id=' + objectID;
    hideSpinner($(this).find("i"), icon)
});


$(".open-record-btn").on('click',function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");
    var icon = $(this).find( "i" ).attr("class");
    showSpinner($(this).find("i"))
    window.location = openRecordUrl + '?id=' + objectID;
    hideSpinner($(this).find("i"), icon)
});

$(".open-form-btn").on('click',function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");
    var icon = $(this).find( "i" ).attr("class");
    showSpinner($(this).find("i"))
    window.location = openFormUrl + '?id=' + objectID;
    hideSpinner($(this).find("i"), icon)
});

