$(document).ready(function(){
    var audio = new Audio(audio_url);

    audio.addEventListener('loadedmetadata', function() {
        var minutes = "0" + Math.floor(audio.duration / 60);
        var seconds = "0" + Math.floor(audio.duration % 60);
        var dur = minutes.substr(-2) + ":" + seconds.substr(-2);
        $('#duration').html(dur);
    });

    $('#play').on('click', function(e){
        e.preventDefault();
        audio.is
        audio.play();

        // $(this).replaceWith('<a id="pause" class="align-self-center ml-2"><img id="pause-img" height=30 width=30></a>');
        // $('#pause-img').attr('src', '/images/pause.svg');
    });

    
});