$('form input[type="checkbox"]').click(function () {
    var label = $('label[for="'+$(this).attr('id')+'"]');
    $(label).animate({ 'margin': '0' }, 100);
    $(label).animate({ 'margin': '5px' }, 100);
  });

