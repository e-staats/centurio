document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll("#attempt")
    for (const button of buttons) {
        button.onclick = attempt_project
    }
});
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector("#test_project_maker").onclick = make_test_projects
});

function attempt_project () {
    $.ajax({
        type: "POST",
        url: "/_attempt_project",
        data: { 'link_identifier': $(this).attr('name') },
        dataType: "json",
        success: function (response) {
            window.location = response.redirect_url;
        },
        error: function (rs, e) {
            console.log(rs);
        }
    });
}

function make_test_projects () {
    $.ajax({
        type: "POST",
        url: "/_make_test_projects",
        dataType: "json",
        success: function (response) {
            window.location = response.redirect_url;
        },
        error: function (rs, e) {
            console.log(rs);
        }
    });
}

