/**
* Count the number of checked checkboxes to allow any actions
*/

function countChecked() {
      var numberChecked = $('*[id^="actionCheckbox"] input:checked').length;
      if (numberChecked == 0) {
        $("#id_actions").fadeTo(200, 0);
        document.getElementById("dropdownMenu1").disabled=true;
      } else {
        $("#id_actions").fadeTo(200, 1);
        document.getElementById("dropdownMenu1").disabled=false;
      }
}
