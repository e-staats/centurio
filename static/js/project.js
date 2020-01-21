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

