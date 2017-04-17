$(document).ready(
    function() {

        $(".likebutton").click(
            function() {

                $.ajax({
                url: document.location.href + "inc",
                success: function(data, textStatus, jqXHR) {
                            $(".likescount")[0].innerHTML = data;
                }});

                $(".likebutton").hide();
            }
        );

        if ($(".likescount").size() != 0) {
            window.setInterval(
                function() {
                    $.ajax({
                        url: document.location.href + "getlikescount",
                        success: function(data, textStatus, jqXHR) {
                            $(".likescount")[0].innerHTML = data;
                        }
                    });
                },
                2000
            );
        }

        $(".commentsdiv").load("comments");
        if ($(".commentsdiv").size() != 0) {
            window.setInterval(
                function() {
                    $(".commentsdiv").load("comments");
                },
                2000
            );

        }

        $(".for_creating_post_form").load("addpost");

        $(".catselect").chosen();

        $(document).on("submit", ".ajax_add_post_form", function() {
            $.ajax({url: $(this).attr('action'), method: 'POST', data: $('form').serialize(),
            success: function(data, textStatus, jqXHR) {
                if (data == "OK") {
                    location.reload();
                } else {
                    $(".for_creating_post_form").html(data);
                }
            }});
            return false;
        });



    }

)