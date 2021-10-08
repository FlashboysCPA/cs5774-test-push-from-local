$(document).ready(function(){
    //new code for attending event on events page
    $('div.lostpost-attendancepts button.attend').click(function (){
        var scoreDiv = $(this).siblings('div.attendancescore');

        var scoreNum = parseInt($(scoreDiv).text());
        scoreNum++;
        console.log(scoreNum);

        $(scoreDiv).text(scoreNum);

        var successMsg = $('<p class="attend-success">I Am Attending!</p>')
        $(successMsg).appendTo( $(this).parent() ).fadeOut('slow', function (){
            $(this).remove();
        }) ;
    });


    //new code for downvote
    $('div.lostpost-pts button.downvote').click(function (){
        var scoreDiv = $(this).siblings('div.score');

        var scoreNum = parseInt($(scoreDiv).text());
        scoreNum--;

        console.log(scoreNum);

        $(scoreDiv).text(scoreNum);

        var successMsg = $('<p class="downvote-success">Downvote Successful! :(</p>')
        $(successMsg).appendTo( $(this).parent() ).fadeOut('slow', function (){
            $(this).remove();
        }) ;
    });

    //event handler for upvote button- need to do downvote button still
    //jquery for points related to score
    $('div.lostpost-pts button.upvote').click(function (){
        var scoreDiv = $(this).siblings('div.score');

        var scoreNum = parseInt($(scoreDiv).text());
        scoreNum++;

        console.log(scoreNum);

        $(scoreDiv).text(scoreNum);

        var successMsg = $('<p class="upvote-success">Upvote Successful! :)</p>')
        // $(this).parent().append(successMsg)
        $(successMsg).appendTo( $(this).parent() ).fadeOut('slow', function (){
            $(this).remove();
        }) ;
    });

    //    jquery and event delegation to add new child elements
    $('div.lostpost-follow button.follow').click(function (){
        var successMsg = $('<p class="follow-success">Follow Successful! :)</p>')
        $(successMsg).appendTo( $(this).parent() ).fadeOut('slow', function (){
            $(this).remove();
        }) ;
    });

    //    check querystring
    checkQueryString();

    //    check querystring that is in header
    checkHeaderQueryString();
})
//function for search that is located in header of home page or index that is using traverse logic
function checkHeaderQueryString(){
    var querystring = window.location.search;
    // console.log(querystring);

    var urlParams = new URLSearchParams(querystring);
    if (urlParams.has("header-search-page")){
        var keyword = urlParams.get("header-search-page");
        if (keyword=='dog'){
            window.alert("Great! You searched 'dog'!");
        }
        else{
            window.alert("ERROR! You did NOT search 'dog'!")
        }
    }
}


//function for search and results on a separate page-uses dom traversal with has in code
function checkQueryString(){
    var querystring = window.location.search;
    // console.log(querystring);

    var urlParams = new URLSearchParams(querystring);
    if (urlParams.has("search-page")){
        var keyword = urlParams.get("search-page");
        if (keyword=='dog'){
            window.alert("Great! You searched 'dog'!");
        }
        else{
            window.alert("ERROR! You did NOT search 'dog'!")
        }
    }
}