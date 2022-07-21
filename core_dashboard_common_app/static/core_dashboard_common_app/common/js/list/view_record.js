/**
 * View record for admin.
 */

openViewRecord = function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");
    var icon = $(this).find( "i" ).attr("class");
    // Show loading spinner
    showSpinner($(this).find("i"))
    window.location = viewRecordUrl + '?id=' + objectID;
    hideSpinner($(this).find("i"), icon)
};

$(".view-record-btn").on('click', openViewRecord);
