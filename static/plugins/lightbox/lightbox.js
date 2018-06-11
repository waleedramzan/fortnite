// Gameforest lightbox plugin by yakuzi
// Author: https://yakuthemes.com
// Version: 1.0.3
(function($) {
	"use strict";

  $.fn.lightbox = function(light) {

  	var current_url = window.location.href;
  	var is_media = current_url.indexOf("media");

	  var current, size, animation, slideNum;

	  $(this).click(function(e) {
	    e.preventDefault();

			var option = $(this).data("lightbox"),
					comment = '', title = '';

	    if ($(this).data("animation")) {
	      animation = $(this).data("animation");
	    } else {
	      animation = 'fadeIn animate2';
	    }

         //  '<div class="title_cosmetics">'+ option.title +'</div>' +
			//   '<div class="title_cosmetics">'+ option.description +'</div>'
	    if ( option.disqus == true ) {
	      	if(is_media < 1) {
                comment = '<div class="lightbox-comment">' +
                    '<div class = lightbox-all>' +
                    '<div class = lightbox-title>Title:</div>' +
                    '<div id="title_cosmetics"></div>' +
                    '<div class = lightbox-obtained>Obtained:</div>' +
                    '<div id="obtained_cosmetics"></div>' +
                    '<div class = lightbox-type>Type:</div>' +
                    '<div id="type_cosmetics"></div>' +
                    '<div class = lightbox-rarity>Rarity:</div>' +
                    '<div id="rarity_cosmetics"></div>' + '</div>' +
                    '<div id="disqus_thread"></div>' +
                    '<script>' +
                    "(function() {var d = document, s = d.createElement('script');s.src = 'https://fortnitego-com.disqus.com/embed.js';s.setAttribute('data-timestamp', +new Date());(d.head || d.body).appendChild(s);})();" +
                    '</script>' +
                    '<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>' +
                    '<script id="dsq-count-scr" src="https://' + light.disqus + '.disqus.com/count.js" async></script>' +
                    '</div>';
            }
            else if(is_media > 1){
	      		comment = '<div class="lightbox-comment">' +
                    '<div class = lightbox-all>' +
                    '<div class = lightbox-title>Title:</div>' +
                    '<div id="title_cosmetics"></div>' +
                    '<div id="disqus_thread"></div>' +
                    '<script>' +
                    "(function() {var d = document, s = d.createElement('script');s.src = 'https://fortnitego-com.disqus.com/embed.js';s.setAttribute('data-timestamp', +new Date());(d.head || d.body).appendChild(s);})();" +
                    '</script>' +
                    '<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>' +
                    '<script id="dsq-count-scr" src="https://' + light.disqus + '.disqus.com/count.js" async></script>' +
                    '</div>';
			}
	    }

	    if ( option.facebook == true ) {
	      comment = '<div id="fb-root"></div>' +
	      '<script>(function(d, s, id) {' +
	      'var js, fjs = d.getElementsByTagName(s)[0];'+
	      'if (d.getElementById(id)) return;'+
	      'js = d.createElement(s); js.id = id;'+
	      'js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.9";'+
	      'fjs.parentNode.insertBefore(js, fjs);'+
	      '}(document, \'script\', \'facebook-jssdk\'));</script>'+
	      '<div class="lightbox-comment">' +
	      '<div class="fb-comments" data-href="https://developers.facebook.com/docs/plugins/comments#configurator" data-numposts="5"></div>' +
	      '</div>';
	    }

	    slideNum = $("[data-lightbox*='\"gallery\": \"" + option.gallery + "\"']").index(this);
	    var lightbox = '<div class="lightbox custom_lightbox">' +
	      '<div class="lightbox-overlay animated fadeIn fast"></div>' +
				'<a class="lightbox-close animated fadeIn fast close_custom" href="#"><i class="fa fa-times"></i></a>' +
	      '<div>' +
	        '<div class="lightbox-block animated ' + animation + ' fast">' +
	          '<div class="lightbox-img">' +
	            '<ul></ul>' +
	          '</div>'+ comment + '</div>' +
	      '</div>' +
	    '</div>';

	    $('body').append(lightbox);

	    if ( option.gallery ) {
	      $('.lightbox-img').append(
	        '<a class="lightbox-prev"><i class="fa fa-chevron-left"></i></a>' +
	        '<a class="lightbox-next"><i class="fa fa-chevron-right"></i></a>'
	      );
	      $('body').find("[data-lightbox*='\"gallery\": \"" + option.gallery + "\"']").each(function() {

	      	if(JSON.parse($(this).attr('data-lightbox')).image == "true") {
                $('.lightbox ul').append(
                    '<li>' +
                    '<img rarity="' + JSON.parse($(this).attr('data-lightbox')).rarity + '" type="' + JSON.parse($(this).attr('data-lightbox')).type + '" obtained="' + JSON.parse($(this).attr('data-lightbox')).obtained + '"  description="' + JSON.parse($(this).attr('data-lightbox')).description + '" title="' + JSON.parse($(this).attr('data-lightbox')).title + '"  src="' + $(this).attr('href') + '">' +
                    '</li>'
                );
            }
            else if(JSON.parse($(this).attr('data-lightbox')).video == "true"){
	      		$('.lightbox ul').append(
	      			'<li class="lightbox-video">' +
					  '<div class="embed-responsive embed-responsive-16by9" title="' + JSON.parse($(this).attr('data-lightbox')).title + '">' +
					  '<img style="display: none" title="' + JSON.parse($(this).attr('data-lightbox')).title +'">'+
						'<iframe class="embed-responsive-item" src="' + $(this).attr('src') + '" allowfullscreen></iframe>' +
					  '</div>' +
					'</li>'
	      			// '<li>' +
                    // '<video width="400" controls>' +
					// '<source rarity="' + JSON.parse($(this).attr('data-lightbox')).rarity + '" type="' + JSON.parse($(this).attr('data-lightbox')).type + '" obtained="' + JSON.parse($(this).attr('data-lightbox')).obtained + '"  description="' + JSON.parse($(this).attr('data-lightbox')).description + '" title="' + JSON.parse($(this).attr('data-lightbox')).title + '"  src="' + $(this).attr('src') + '">' +
                    // '</video>'+
					// '</li>'
                );
			}
	      });
	    }

			var video = '',
					matches = '',
					source = $(this).attr('href');

			if (matches = source.match(/\/\/.*?youtube\.[a-z]+\/watch\?v=([^&\s]+)/) || source.match(/youtu\.be\/(.*)/)) {
	      video = 'https://www.youtube.com/embed/' + matches[1] + '?rel=0&amp;amp;autoplay=1&amp;amp;showinfo=0';
	    }

			if (matches = source.match(/\/\/.*?twitch\.[a-z]+\/\?channel=([^&\s]+)/)) {
				video = 'https://player.twitch.tv/?channel=' + matches[1];
			}

	    if ( video ) {
	      $('.lightbox ul').append(
	        '<li class="lightbox-video">' +
	          '<div class="embed-responsive embed-responsive-16by9">' +
	          '<iframe class="embed-responsive-item" src="' + video + '" allowfullscreen></iframe>' +
	          '</div>' +
	        '</li>'
	      );
	    }

	    if ( !(option.gallery) && !( video ) ) {
	      $('.lightbox ul').append(
	        '<li>' +
	          '<img src="' + $(this).attr('href') + '"">' +
	        '</li>'
	      );
	    }

	    size = $('.lightbox ul > li').length;

	    $('.lightbox ul > li').hide();
	    $('.lightbox ul > li:eq(' + slideNum + ')').show();

        if(is_media > 1) {
            $('#title_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + slideNum + ') img').attr('title');
        }
        else if(is_media < 1) {
            $('#title_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + slideNum + ') img').attr('title');
            $('#obtained_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + slideNum + ') img').attr('obtained');
            $('#type_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + slideNum + ') img').attr('type');
            $('#rarity_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + slideNum + ') img').attr('rarity');
        }
	    current = slideNum;
	  });

	  $('body').on('click', '.lightbox-overlay, .lightbox-close', function() {
	    if ($(this).data("animation")) {
	      animation = $(this).data("animation");
	    } else {
	      animation = 'fadeIn animate2';
	    }

	    $(this).parent().find('.lightbox-overlay').removeClass('fadeIn').addClass('fadeOut');
	    $(this).parent().find('.lightbox-block').removeClass(animation).addClass('fadeOut');
	    $(this).parent().find('.lightbox-close').removeClass('fadeIn').addClass('fadeOut');

	  	setTimeout(function(){
	      $('.lightbox').remove();
	  	}, 600);
	    return false;
	  });

	  $('body').on('click', '.lightbox-next, .lightbox-prev', function(e) {
	    e.preventDefault();
	    e.stopPropagation();

	    var dest;

	    if ($(this).hasClass('lightbox-prev')) {
	      dest = current - 1;
	      if (dest < 0) {
	        dest = size - 1;
	      }
	    } else {
	      dest = current + 1;
	      if (dest > size - 1) {
	        dest = 0;
	      }
	    }

	    if(is_media > 1) {
            $('#title_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + dest + ') img').attr('title');
        }
        else if(is_media < 1){
	    	$('#title_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + dest + ') img').attr('title');
            $('#obtained_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + dest + ') img').attr('obtained');
            $('#type_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + dest + ') img').attr('type');
            $('#rarity_cosmetics')[0].innerHTML = $('.lightbox ul > li:eq(' + dest + ') img').attr('rarity');
		}
	    $('.lightbox ul > li:eq(' + current + ')').hide();
	    $('.lightbox ul > li:eq(' + dest + ')').show();

	    current = dest;
	  });

	  return this;
	};
})(window.jQuery);
