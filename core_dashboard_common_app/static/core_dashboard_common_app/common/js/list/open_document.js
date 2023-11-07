/**
 * Open document for text editor.
 */

$(".open-xml-record-btn").on('click',function() {
    redirectToTextEditor(openXMLRecordUrl,$(this),"id")
});

$(".open-json-record-btn").on('click',function() {
    redirectToTextEditor(openJSONRecordUrl,$(this),"id")
});

$(".open-xml-form-btn").on('click',function() {
    redirectToTextEditor(openXMLFormUrl,$(this),"id")
});
$(".open-json-form-btn").on('click',function() {
    redirectToTextEditor(openJSONFormUrl,$(this),"id")
});

redirectToTextEditor = function(openUrl, selector, param) {
    var objectID = selector.closest('tr').attr("objectid");
    var icon = selector.find( "i" ).attr("class");
    showSpinner(selector.find("i"))
    window.location = openUrl + '?'+param+'=' + objectID;
    hideSpinner(selector.find("i"), icon)
};
