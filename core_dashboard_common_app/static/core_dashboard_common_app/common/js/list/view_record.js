/**
 * View record for admin.
 */

openViewRecord = function() {
    var $registryRow = $(this).closest('tr');
    var objectID = $registryRow.attr("objectid");
    window.location = viewRecordUrl + '?id=' + objectID;
};

$(".view-record-btn").on('click', openViewRecord);
