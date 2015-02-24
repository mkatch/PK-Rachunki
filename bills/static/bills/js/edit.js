$('.datepicker').datepicker({
    format: "d.mm.yyyy",
    todayBtn: "linked",
    language: "pl",
    autoclose: true,
    todayHighlight: true
});

$('#all-entries-button').click(function () {
    console.log("YoMama!");
    var cb = $('#all-entries-checkbox');
    cb.prop("checked", !cb.prop("checked")).trigger("change");
});

$('#all-entries-checkbox').change(function () {
    var checked = $(this).prop("checked");
    var slaves = $('.entry-checkbox');
    for (var i = 0; i < slaves.length; ++i) {
        slaves.prop("checked", checked);
    }
});

$('#all-entries-checkbox').click(function (event) {
    event.stopPropagation();
});

$('#entries').sortable({
    handle: ".entry-handle",
});