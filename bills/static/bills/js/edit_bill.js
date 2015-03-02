$('#bill-form').submit(function (event) {
    event.preventDefault();
    console.log("form submitted!");
});

$('#all-entries-button').click(function () {
    var cb = $('#all-entries-checkbox');
    cb.prop('checked', !cb.prop('checked')).trigger('change');
});

$('#all-entries-checkbox').change(function () {
    $('.entry-checkbox').prop('checked', $(this).prop('checked'));
});

$('#all-entries-checkbox').click(function (event) {
    event.stopPropagation();
});

$('#new-entry-button').click(function (event) {
    var ord = $('#entries > li').length + 1
    var template = $('#entry-template').html();
    console.log(ord);
    var entry = Mustache.render(template, { ord: ord });
    $('#entries').append(entry);
});

$('#remove-entries-button').click(function (event) {
    $('#entries li').has('.entry-checkbox:checked').remove();
})

$('#entries').sortable({
    handle: ".entry-handle",
    update: function (event, ui) {
        $('#entries .entry-ord').each(function (i) {
            $(this).prop('value', i);
        })
    },
});