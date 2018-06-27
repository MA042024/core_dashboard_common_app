/**
 * Init the dropdown menu
 */
function initMenu() {
    resetCheckbox();
    $('.paginate_button ').on('click', resetCheckbox);
    countChecked();
    $('*[id^="actionCheckbox"] input[type=checkbox]').on( "change", countChecked );
}