// Custom scripts
$(document).ready(function () {

    // Login check
    showSpinner();
    $.get('http://127.0.0.1:5001/drive2photos-12345/us-central1/login', (data) => {
        console.log(data)
    })
    hideSpinner();

    //Show / Hide spinner
    function showSpinner() {
        $('.spinner').show();
    }

    function hideSpinner() {
        $('.spinner').hide();
    }

    // On button click, get value 
    // of input control Show alert 
    // message box 
    $("#submitButton").click(function () {
        var inputString = $("#topFolderInput").val();
        alert(inputString);
    });
}); 
