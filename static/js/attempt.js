document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll("#start-complete")
    for (const button of buttons) {
        $(button).one('click', start_complete)
    }
});

function start_complete() {
    var day = $(this).attr('name')
    var attempt = $(this).attr('data-attempt')
    var new_button = $('<button />', {
        value: attempt,
        id: 'day',
        name: day,
        html: 'Complete',
        data: {
            'attempt': attempt,
        },
        class: 'btn btn-outline-success btn-sm align-self-end complete',
        on: {
            click: complete_day
        }
    });
    console.log(new_button)
    new_button.insertAfter($(this))
    $(this).after("<div class='row'><textarea id='" + day + "' rows='4' cols='50' name='description' type='text' placeholder=' How did it go?'></textarea></div>")
    $(this).remove()
}


function complete_day() {
    day = $(this).attr('name')
    var info = $('#' + day).val();
    console.log($(this))
    console.log(info)

    $.ajax({
        type: "POST",
        url: "/_complete_day",
        data: {
            'attempt_id': $(this).attr('value'),
            'attempt_day_id': $(this).attr('name'),
            'comment': info
        },
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