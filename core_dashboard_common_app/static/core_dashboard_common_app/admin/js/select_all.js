/**
 * Select all checkboxes
 */
function selectAll(source, id) {
    var isChecked = source.checked;
    $('*[id^="actionCheckbox"] input[type=checkbox]').each(function() {
            $(this).prop("checked", isChecked);
        }
    );
}
