document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll("#day")
    for (const button of buttons) {
        $(button).one('click', complete_day)
    }
});

function complete_day () {
    $.ajax({
        type: "POST",
        url: "/_complete_day",
        data: { 'attempt_id': $(this).attr('data-attempt'),
            'attempt_day_id': $(this).attr('name') },
        dataType: "json",
        context: this,
        success: function (response) {
            // TODO
            $(this).removeClass('btn btn-outline-success btn-sm align-self-end').addClass('btn btn-success btn-sm align-self-end');
            $(this).prop('disabled', true)
            $(this).html("Completed")
        },
        error: function (rs, e) {
            console.log(rs);
        }
    });
}