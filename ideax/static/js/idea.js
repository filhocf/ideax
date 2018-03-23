$(window).scroll(function(){
if($(window).scrollTop() >= $('.main-header').outerHeight()) {
  var scroll = $(window).outerWidth() - $('body').outerWidth();
  $('.phase-filter').addClass('fixed');
  $('.phase-filter').css("width", $(window).outerWidth() - scroll);
}else{
  $('.phase-filter').removeClass('fixed');
  $('.phase-filter').css("width", "100%");
}
});


$(document).mouseup(function (e)
{
    var container = $(".idea-options");

    if (!container.is(e.target) && container.has(e.target).length === 0){
        $( ".idea-options input" ).prop( "checked", false ); //to uncheck
    }
});


function openModal (url){
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    beforeSend: function (){
      $("#modal-idea").modal("show");
    },
    success: function (data){
      $("#modal-idea .modal-content").html(data.html_form);
    }
  });
}

function vote(url, idLike, idDislike, aLike, aDislike){
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    success: function (data){
      $(idLike).html(data.qtde_votes_likes);
      $(idDislike).html(data.qtde_votes_dislikes);

      if (data.class == null){
        $(aLike).removeClass("fas").addClass("far");
        $(aDislike).removeClass("fas").addClass("far");
      } else if (data.class == true){
        $(aLike).addClass("fas");
        $(aDislike).removeClass("fas").addClass("far");
      }else {
        $(aLike).removeClass("fas").addClass("far");
        $(aDislike).addClass("fas");
      }
    }
  });
}

$(function () {

  var loadForm = function(){
    var btn = $(this);
    var idModal = btn.attr("data-modal");
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function (){
          $(idModal).modal("show");
      },
      success: function (data){
        var idModalContent = idModal + " .modal-content";
        $(idModalContent).html(data.html_form);
      }
    });
  };

  var saveForm = function(){
    var form = $(this);
    var idModal = form.attr("data-modal");
    var idDivList = form.attr("data-list-div");
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data){
        if(data.form_is_valid){
           $(idDivList).html(data.html_list);
           $(idModal).modal("hide");
        }else{
          var idModalContent = idModal + " .modal-content";
          $(idModalContent).html(data.html_form);
        }
      }
    });
    return false;
  };

  $(".js-create-idea").click(loadForm);
  $("#modal-idea-crud").on("submit", ".js-idea-create-form", saveForm);

  $(document).on("click", ".js-update-idea", loadForm);
  $("#modal-idea-crud").on("submit", ".js-idea-update-form", saveForm);

  $(document).on("click", ".js-remove-idea", loadForm);
  $("#modal-idea-crud").on("submit", ".js-idea-remove-form", saveForm);

  $(".js-create-category").click(loadForm);
  $("#modal-category-crud").on("submit", ".js-category-create-form", saveForm);

  $(document).on("click", ".js-update-category", loadForm);
  $("#modal-category-crud").on("submit", ".js-category-update-form", saveForm);

  $(document).on("click", ".js-remove-category", loadForm);
  $("#modal-category-crud").on("submit", ".js-category-remove-form", saveForm);

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  function submitEvent(event, form) {
    event.preventDefault();
    var $form = form;
    var data = $form.data();
    url = $form.attr("action");
    commentContent = $form.find("textarea#commentContent").val();

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
    });

    var doPost = $.post(url, {
        ideiaId : data.ideaId,
        parentId: data.parentId,
        commentContent: commentContent
    });

    doPost.done(function (response) {
        var errorLabel = $form.find("span#postResponse");
        if (response.msg) {
            errorLabel.text(response.msg);
            errorLabel.removeAttr('style');
        }
        refleshCommentList(event, form)
    });
  }

  function refleshCommentList(event, form){
    var urlRequest = '/idea/comments/' + form.data().ideaId;
    $.ajax({
      url: urlRequest,
      dataType: 'json',
      success: function (data){
        $("#comments-area").html(data.html_list);
      }
    });
  }

  $("#commentForm").submit(function (event) {
    submitEvent(event, $(this));

  });

  var newCommentForm = '<form id="commentFormReply" class="form-horizontal" \
                              action="/post/comment/"\
                              >\
                              <fieldset>\
                              <div class="form-group comment-group">\
                                  <label for="commentContent" class="col-lg-2 control-label">New comment</label>\
                                  <div class="col-lg-10">\
                                      <textarea class="form-control" rows="3" id="commentContent"></textarea>\
                                      <span id="postResponse" class="text-success" style="display: none"></span>\
                                  </div>\
                              </div>\
                              <div class="form-group">\
                                  <div class="col-lg-10 col-lg-offset-2">\
                                      <button type="submit" class="btn btn-primary">Submit</button>\
                                  </div>\
                              </div>\
                          </fieldset>\
                      </form>';

  $(document).on("click", 'a[name="replyButton"]', function () {
    var $mediaBody = $(this).parent();
    if ($mediaBody.find('#commentFormReply').length == 0) {
        $mediaBody.parent().find(".reply-container:first").append(newCommentForm);
        var $form = $mediaBody.find('#commentFormReply');
        $form.data('idea-id', $(this).attr("data-idea-id"));
        $form.data('parent-id', $(this).attr("data-parent-id"));
        /*$form.on("submit", function (event) {
            submitEvent(event, $(this));
            refleshCommentList(event, $(this))

        });*/
    } else {
        $commentForm = $mediaBody.find('#commentFormReply:first');
        if ($commentForm.attr('style') == null) {
            $commentForm.css('display', 'none')
        } else {
            $commentForm.removeAttr('style')
        }
    }

  });

  $(document).on("submit", "#commentFormReply", function (event) {
    submitEvent(event, $(this));
  });

});
