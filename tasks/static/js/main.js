function initCheckbox() {
 $('.task_box input[type="checkbox"]').click(function (event) {
  var box = $(this);
  var myurl = "http://127.0.0.1:8000/";
  $.ajax({
   type: 'POST',
   cache: false,
   dataType: 'json',
   url: myurl,
   data: {
    'pk': box.attr('data-task-id'),
    'present': box.is(':checked') ? '1': '',
    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
   }
  });
 });
}

/*$(function () {
    $('input:checkbox').on('change', function () {
        var input = $(this).next('span'),
            task_input = $('.content').next('span');
        if (this.checked) {
                $(".content").wrap("<strike>");
                $(".content").fadeOut("slow");
        } else {
            $(task_input).css('textDecoration', 'none');
        }
    })
});*/


/*$(".task_box").click(function () {
    $(".task_link, .task_box").wrap("<strike>").fadeOut("slow");
 //   $(".tasks, .checkboxes").hide();
 //   location.reload();
});*/

function delTask() {
    $('.task_box input[type="checkbox"]').click(function (event) {
        $( "input:checked" ).css("text-decoration", "line-through").wrap("<strike>").fadeOut("slow").hide();
    });
}

function initEditTask() {
    $('a.edit-form-link').click(function (event) {
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function (data, status, xhr) {
                // check if we got successful response from the server
                if (status != 'success') {
                    alert('Server error! Please try later.');
                    return false;
                }

                // update modal window with arrived content from the server
                var modal = $('#myModal'),
                    html = $(data), form = html.find('#ajax_form');
                console.log(form);

                modal.find('.modal-title').html("<h3>Edit task</h3>");
                modal.find('.modal-body').html(form);

                modal.modal('show');
            },

            'error': function () {
                alert('Server error! Please try later.');
                return false
            }
        });

        return false;
    });
}


 $(document).ready(function(){
     initCheckbox();
     initEditTask();
     delTask();
 });