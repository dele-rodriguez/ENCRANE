setInterval(function(){
  $.ajax({
    type: 'GET',
    url: window.location.href
  })
}, 7000)