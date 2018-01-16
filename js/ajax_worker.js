(function worker() {
  $.get('/is_ready', function(data) {
    $('#result').val(data.isReady);
    if(data.isReady){
        $('#dl').attr("href", "/download");
    }
    else {
        setTimeout(worker, 5000);
    }
  });
})();
