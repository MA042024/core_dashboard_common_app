function initUser() {
    if ( ! $.fn.dataTable.isDataTable( '#table-' + object + '-user' )) {
        $('#table-' + object + '-user').DataTable({
            "scrollY": "226px",
            "iDisplayLength": 5,
            "scrollCollapse": true,
            "lengthMenu": [5, 10, 15, 20],
            "columnDefs": [
                {"className": "dt-center", "targets": 0}
            ],
            order: [[1, 'asc']],
            "columns": getColumns()
        });
    }
}

/**
 * Return the definition of the columns
 */
function getColumns() {
    if (numberColumns == "6") {
        return [ null, null, null, null, null, { "orderable": false } ];
    }
    if (numberColumns == "5") {
        return [ null, null, null, null, { "orderable": false } ];
    }
    if (numberColumns == "4") {
        return [ null, null, null, { "orderable": false } ];
    }
    return [null, null, {"orderable": false}]

}