$('.datepicker').datepicker({
    format: "d.mm.yyyy",
    todayBtn: "linked",
    language: "pl",
    autoclose: true,
    todayHighlight: true
});

$('#entries-body').sortable({
    helper: function(event, elem) {
        var nameNode = elem.children(".name")[0];
        return nameNode.cloneNode(true);
    },
});