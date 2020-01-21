function complete_day () {
    $.ajax({
        type: "POST",
        url: "/_complete_day",
        data: { 'attempt_id': $(this).attr('data-attempt'),
            'attempt_day_id': $(this).attr('name') },
        dataType: "json",
        success: function (response) {
            // TODO
            $(this).innerHTML = "Hold up"
        },
        error: function (rs, e) {
            console.log(rs);
        }
    });
}