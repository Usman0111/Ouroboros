$(document).ready(function() {
    const optionalQuestionsStyle = "color:#4286f3; padding: 2em 0em 1em 0em;";
    const optionalQuestionsText = "The following questions are optional. Scroll down to submit your application, or continue to help us improve the event!"
    const optionalQuestionsNode = `<h6 style="${optionalQuestionsStyle}">${optionalQuestionsText}</br></h6>`
    if (!$('#id_race input[value="O"]')[0].checked) {
        $('#id_race_other').parent().hide();
    }
    $('#id_race input[value="O"]').click(function() {
        if ($('#id_race input[value="O"]')[0].checked){
            $('#id_race_other').parent().show();
        }
        else{
            $('#id_race_other').parent().hide();
        }
    });

    if ($('#id_gender').val() !== "X"){
        $('#id_gender_other').parent().hide();
    }
    $('#id_gender').on('change', function(){
         let selection = $('#id_gender').val();
         if (selection === "X"){
            $('#id_gender_other').parent().show();
         }
         else{
             $('#id_gender_other').parent().hide();
         }
    });

    if ($('#id_school option:selected').text() !== "Other"){
        $('#id_school_other').parent().hide();
    }
    $('#id_school').on('change', function(){
         let selection = $('#id_school option:selected').text();
         if (selection === "Other"){
            $('#id_school_other').parent().show();
         }
         else{
             $('#id_school_other').parent().hide();
         }
    });
    // Custom styling for multi-select inputs.
    // Reference: https://select2.org/getting-started/basic-usage
    $('#id_technology_experience').select2();
})