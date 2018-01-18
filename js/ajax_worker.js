(function worker() {
  $.get('/is_ready', function(data) {
    //$('#result').val(data.isReady);
    if(data.isReady){
        $('#dl').attr('href', '/download');
        $('#dl').text('file is ready');
        $('#dl').css('color', 'green');
    }
    else {
        setTimeout(worker, 1000);
    }
  });
})();
