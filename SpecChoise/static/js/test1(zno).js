$(function () {
    $('a#calculate').bind('click', function () {
        $.getJSON($SCRIPT_ROOT + '/_spec_gener', {
            math: document.querySelector('#math').checked,
            physics: (document.querySelector('#physics').checked),
            ukrainian_history: (document.querySelector('#ukrainian_history').checked),
            foreign_lang: (document.querySelector('#foreign_lang').checked),
            geography: (document.querySelector('#geography').checked),
            chemistry: (document.querySelector('#chemistry').checked),
            biology: (document.querySelector('#biology').checked),
        }, function (data) {
            $("div.result").empty()
            for (var i = 0; i < data.speciality.length; i++) {
                $(".result").append("<div class='speciality'>" + data.speciality[i] + "</div>");
                $(".result").append("<div class='subjects'>" + data.subjects[i] + "</div><br>");

            }
        });
        return false;
    });
});