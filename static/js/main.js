
$(document).ready(function() {
    $('input[name="option"]').change(function() {
        var selectedOption = $('input[name="option"]:checked').val();
        $.ajax({
            url: '/option/' + selectedOption + '/',
            type: 'get',
            dataType: 'html',
            success: function(data) {
                $('#option-content').html(data);
            }
        });
    })
});

