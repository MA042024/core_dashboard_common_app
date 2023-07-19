
/**
 * Open the upload file modal
 */
openUploadFile = function () {
    $("#file-upload-modal").modal("show");
};

/**
 * AJAX call, delete a curated document
 * @param result_id
 */
upload_file = function(){
    var formData = new FormData($( "#file-upload-form" )[0]);

	$.ajax({
        url : uploadFileUrl,
        type : "POST",
        dataType: "json",
        processData: false,
        contentType: false,
        data : formData,
		success: function(data){
            location.reload(true);
	    },
        error:function(data){
            var error_message;
            try{
                error_message = JSON.parse(data.responseText).message;
            } catch (e) {
                error_message = "Unable to upload this file."
            }
            $.notify(error_message, "danger");
        }
    });
};


$('#upload-blob-btn').on('click', openUploadFile);
$('#file-upload-yes').on('click', upload_file);
