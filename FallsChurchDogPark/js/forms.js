//event delegation to actually click on child elements that don’t actually exist yet
var $form = $('.form');
var $eventname = $('.eventname');
var $eventdate = $('.eventdate');
var $events = $('.events');



$form.on('submit', function (e) {
    e.preventDefault();

    var $li = $('<li>');
    var $eventnameH2 = $('<h2>').html('Event: '+$eventname.val());
    console.log($eventnameH2)

    var $eventdateP = $('<p>').html('Date: '+$eventdate.val());

    var $eventtype = $('[name="eventtype"]:checked')
    console.log($eventtype.val())

    $li.append($eventnameH2).append($eventdateP).addClass($eventtype.val());
    $events.append($li);
});

$events.on('click', 'li', function (){
    $(this).toggleClass('js-highlight');
});