$(document).ready(function(){
    $('.liker').on('click', function(event){
    	
    	event.preventDefault();
	    $.ajax({
	     	    url:'/addlike/',
	     	    cache: false, 
	     	    data: {id: $(this).data('id'),
	     	    	   model: $(this).data('model'),
	     	    		csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
	     	    type: 'POST', 
	     	    success: function(html){
	    		    
	    		    $('.liker').hide() ;
	    		    $('.likes_count').html(html) ;
	    		}
	   
	    });
    });
});

 // $.ajax({
	//     	    url:'/jobs/',
	//     	    cache: false,
	//     	    data: {name:'ajax'},
	//     	    type: 'POST',
	//     	    success: function(html){
	//     		    $('.jobs_list').append(html);
	//     		    $('.switcher').html('Скрыть')
	//     	}
	//     });