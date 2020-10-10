$(document).ready(function(){

    // handle upload of audio cover

    $('#upload-audio-cover').click(function(event){
      $('#choose-audio-cover').click()
      return false;
    });

    $('#choose-audio-cover').on('change', function(){
        var file = this.files[0];
        var fileReader = new FileReader();

        fileReader.onload = function(e){
            $('#audio-cover-img').attr('src', e.target.result);
        }

        fileReader.readAsDataURL(file);
    });    

    //handle upload of audio file

    $('#upload-audio-file').click(function(event){
        $('#choose-audio-file').click();
        return false;
        
    });

    $('#choose-audio-file').on('change', function(){
        var file = this.files[0];
        $('#audio-file-name').html(file.name);
    });

  });