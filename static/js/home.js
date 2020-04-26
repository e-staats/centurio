function hello() {
    document.querySelector('h1').innerHTML = "Hold up"
}

function count() {
    counter++;
    document.querySelector('#counter').innerHTML = counter
}

document.addEventListener('DOMContentLoaded', function () {
    $("#account-button").on('click', open_menu)
});

function open_menu() {
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