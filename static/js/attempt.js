document.addEventListener('DOMContentLoaded', function () {
    const complete_buttons = $("button.start-complete")
    for (const button of complete_buttons) {
        $(button).one('click', start_complete)
    }
    const comment_buttons = document.querySelectorAll("button.comment")
    for (const button of comment_buttons) {
        $(button).one('click', addComment)
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
    new_button.insertAfter($(this))
    $(this).after("<div class='row'><textarea id='" + day + "' rows='4' cols='75' name='description' type='text' placeholder=' How did it go?'></textarea></div>")
    $(this).remove()
}


function complete_day() {
    day = $(this).attr('name')
    var info = $('#' + day).val();

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
            $('#' + day).before("<div class='col-md-12'>"+info+"</div>")
            $('#' + day).remove()

        },
        error: function (rs, e) {
            console.log(rs);
        }
    });
}

function addComment () {
    var day = $(this).attr('name')
    var attempt = $(this).attr('data-attempt')
    var comment_button = $(this)
    var new_button = $('<button />', {
        value: attempt,
        id: 'day',
        name: day,
        html: "comment",
        data: {
            'attempt': attempt,
        },
        class: "btn btn-info btn-sm align-self-end comment",
        on: {
            click: add_comment.bind(this, comment_button)
        }
    });
    new_button.insertAfter($(this))
    $(this).after("<div class='row'><textarea id='" + day + "' rows='4' cols='75' name='comment' type='text'></textarea></div>")
    $(this).remove()
}

function add_comment(new_button) {
    day = $(this).attr('name')
    var info = $('#' + day).val();

    $.ajax({
        type: "POST",
        url: "/_add_comment",
        data: {
            'attempt_id': $(this).attr('data-attempt'),
            'attempt_day_id': $(this).attr('name'),
            'comment': info
        },
        dataType: "json",
        context: this,
        success: function (response) {
            console.log(this)
            $(this).attr('html', 'test')
            $('#' + day).remove()

        },
        error: function (rs, e) {
            console.log(rs);
        }
    });
}