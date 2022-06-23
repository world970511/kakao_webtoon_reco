$("label img").on("click", function() {
    $("#" + $(this).parents("label").attr("for")).click();
  });

 $( 'input:checkbox[name="selected"]' ).on( "click", function() {
 if($( 'input:checkbox[name="selected"]:checked' ).length > 9)
  {
    $('#submitnBtn').removeAttr('disabled');
  }
  else
  {
    $('#submitnBtn').attr("disabled",true); 
  }  
});