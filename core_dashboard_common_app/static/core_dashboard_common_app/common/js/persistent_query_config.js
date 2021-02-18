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

    // get persistent query type
    var query_type = $("#persistent-query-type").val()

    // FIXME : make the redirect url correctly

    // make the redirect url
    var redirect_url = window.origin+"/explore/"+query_type+"/results-redirect?id="+id;

    $("#persistent-query-link").val(redirect_url);
    $("#rename_tools").hide();
    return true;
}


let getDocumentId = function () {
    id = $(this).closest('button').attr("objectid");
   }

