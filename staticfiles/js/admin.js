window.onload = function() {
    document.body.onchange = function(event) {
        var target = event.target;
        if (target.matches('input[type="file"]')) {
            var reader = new FileReader();
            reader.onload = function() {
                if (reader.readyState == 2) {
                    var imagePreview = target.closest('tr').getElementsByClassName("field-image_display")[0];
                    imagePreview.innerHTML = '<img src="' + reader.result + '" width="50" height="50">';
                }
            }
            reader.readAsDataURL(target.files[0]);
        }
    }
}