/**
 * Open document for text editor.
 */

$(".open-record-btn").on('click',function() {
    redirectToTextEditor(openRecordUrl,$(this),"id")
});

$(".open-record-draft-btn").on('click',function() {
    redirectToTextEditor(openFormUrl,$(this),"data_id")
});

$(".open-form-btn").on('click',function() {
    redirectToTextEditor(openFormUrl,$(this),"id")
});

redirectToTextEditor = function(openUrl, selector, param) {
    var objectID = selector.closest('tr').attr("objectid");
    var icon = selector.find( "i" ).attr("class");
    showSpinner(selector.find("i"))
    window.location = openUrl + '?'+param+'=' + objectID;
    hideSpinner(selector.find("i"), icon)
};
