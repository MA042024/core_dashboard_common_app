/**
 * Load controllers for the persistent query button
 */

$(document).ready(function() {
    var id = "";
    $('.share-btn').on('click', getDocumentId);
    initSharingModal(
        configurePersistentQueryModal, "#persistent-query", "#persistent-query-modal",
        "#persistent-query-link", "#persistent-query-submit"

    );
});



let configurePersistentQueryModal = function() {

    // get persistent query class name
    var tab_name = $('.nav-tabs .active').attr("title")

    // get persistent query path
    var query_path = $("#persistent-query-path").val()

    // make the redirect url
    var redirect_url = window.origin+query_path+"results-redirect?id="+id;

    $("#persistent-query-link").val(redirect_url);
    $("#rename_tools").hide();
    return true;
}


let getDocumentId = function () {
    id = $(this).closest('button').attr("objectid");
   }

