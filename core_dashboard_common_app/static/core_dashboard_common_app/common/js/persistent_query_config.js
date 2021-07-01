/**
 * Load controllers for the persistent query button
 */

$(document).ready(function() {
    var persistent_query_id = null;
    var persistent_query_name = null;
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
    var query_path = $("#persistent-query-path").val();

    var suffixUrl = null

    if (persistent_query_name != ''){
       suffixUrl = "results-redirect?name="+persistent_query_name;
    }
    else  suffixUrl ="results-redirect?id="+persistent_query_id;

    // make the redirect url
    var redirect_url = window.origin+query_path+suffixUrl;

    $("#persistent-query-link").val(redirect_url);
    $("#rename_tools").hide();
    return true;
}


let getDocumentId = function () {
    // get query id
    persistent_query_id = $(this).closest('button').attr("objectid");
    // get query name
    persistent_query_name = $.trim($(this).closest('tr').find('.persistent-query-name').val())
   }

