function startTimer(duration, display) {
    var start = Date.now(),
        diff,
        minutes,
        seconds;
    function timer() {
        // get the number of seconds that have elapsed since
        // startTimer() was called
        diff = duration - (((Date.now() - start) / 1000) | 0);

        // does the same job as parseInt truncates the float
        minutes = (diff / 60) | 0;
        seconds = (diff % 60) | 0;

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (diff <= 0) {
            // add one second so that the count down starts at the full duration
            // example 05:00 not 04:59
            start = Date.now() + 1000;
        }
    };
    // we don't want to wait a full second before the timer starts
    timer();
    setInterval(timer, 1000);
}

$('.environment').on('change', function () {
    $.ajax({
        url: '/environment/set',
        dataType: 'json',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({ "environment": this.value, "_csrf_token": $('[name=_csrf_token]').val() }),
        processData: false,
        success: function (data, textStatus, jQxhr) {

            // Changes to do if the request is successful
            if ($('.environment').val() == 'dev'){
                $('.footer').css('background-color', '#63602b');
            };
            if ($('.environment').val() == 'prod') {
                $('.footer').css('background-color', '#343b40');
            };

            // Update the CSRF token in the HTML for the next request
            $('[name=_csrf_token]').val(data._csrf_token);
        },
        error: function (jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
            console.log($('[name=_csrf_token]').val());
            
            // Update the CSRF token with the new one - this is unique per request
            $.getJSON('/csrf/token', function(data){
                $('[name=_csrf_token]').val(data.csrf_token);
            });
        }
    });
})