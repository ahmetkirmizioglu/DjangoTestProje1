    $(document).ready(function () {
        $("#slider > div:gt(0)").hide();
        setInterval(function () {
            $('#slider > div:first')
                .fadeOut(2000)
                .next()
                .fadeIn(2000)
                .end()
                .appendTo('#slider');
        }, 2000);
    });