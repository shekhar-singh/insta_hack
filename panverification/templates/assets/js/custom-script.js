$(document).ready(function(){
	$("#edit_name").hide();
  	$("#edit_dob").hide();
  	$("#edit_pan").hide();
  	$("#details_correct").hide();
  	$("#hr_line").hide();
});
function valueChecked(){
  	if($('.name1').is(":checked")){
     	$("#edit_name").show(300);
     	$("#details_correct").show(300);
     	$("#hr_line").show(300);
  	}else{
     	$("#edit_name").hide(300);
  	}
  	if($(".dob1").is(":checked")){
     	$("#edit_dob").show(300);
     	$("#details_correct").show(300);
     	$("#hr_line").show(300);
  	}else{
     	$("#edit_dob").hide(300);
  	}
  	if($(".pan1").is(":checked")){
     	$("#edit_pan").show(300);
     	$("#details_correct").show(300);
     	$("#hr_line").show(300);
  	}else{
     	$("#edit_pan").hide(300);
  	}
  	if(!$('.name1').is(":checked") && !$(".dob1").is(":checked") && !$(".pan1").is(":checked")){
  		$("#details_correct").hide(300);
  		$("#hr_line").hide(300);
  	}
}