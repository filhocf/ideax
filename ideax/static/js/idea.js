$('.expand-button').on('click', function (evt) {
  let ideaText = evt.currentTarget.parentNode.parentNode.querySelector('p');
  ideaText.classList.toggle('expand');
  //console.log($(evt.currentTarget).parent().parent());
});

(() => {
  let ideaTitle = document.querySelector('#idea-title h1');
  if (ideaTitle !== undefined && ideaTitle !== null) {
    let autorIndex = ideaTitle.textContent.indexOf('Autor:');
    if (autorIndex > 0) {
      let autor = ideaTitle.textContent.substring(autorIndex);
      let title = ideaTitle.textContent.substring(0, autorIndex);
      title = title.substring(0, title.length - 3);
      autor = autor.substring(7);
      console.log('Encontrado');
      console.log(title);
      console.log(autor);
      ideaTitle.textContent = title;
      document.querySelector("#real-author").textContent = `${autor} via `;
    }
  }
})();


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

function getUserTerm(idDivTerm, urlTerm){
  var term;
  $.ajax({
    url: urlTerm,
    type: 'get',
    dataType: 'json',
    success: function (data){
      term = data.term;
      $(idDivTerm).html(term);
    }
  });
  return term;
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

  var submitEvaluation = function(){
    var form = $(this);

    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data){
        var score = data.score_value;
        $("#score").removeClass("hide");
        $("#score_value").html(score.toFixed(2));

        showMessage("#evaluation-message", data.msg, "alert-info");
      },
      error: function(xhr, status, error){
        showMessage("#evaluation-message", xhr.responseJSON.msg , "alert-danger");
      }
    });
    return false;
  };

  //$(".js-create-idea").click(loadForm);
  //$("#modal-idea-crud").on("submit", ".js-idea-create-form", saveForm);

  //$(document).on("click", ".js-update-idea", loadForm);
  //$("#modal-idea-crud").on("submit", ".js-idea-update-form", saveForm);

  $(document).on("click", ".js-remove-idea", loadForm);
  $("#modal-idea-crud").on("submit", ".js-idea-remove-form", saveForm);

  $(".js-create-category").click(loadForm);
  $("#modal-category-crud").on("submit", ".js-category-create-form", saveForm);

  $(document).on("click", ".js-update-category", loadForm);
  $("#modal-category-crud").on("submit", ".js-category-update-form", saveForm);

  $(document).on("click", ".js-remove-category", loadForm);
  $("#modal-category-crud").on("submit", ".js-category-remove-form", saveForm);

  $(document).on("submit", "#evaluation_form", submitEvaluation);


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
        if (response.msg) {
            showMessage("#comment-message", response.msg, "alert-info");
        }
        $("#commentContent").val("");
        refreshCommentList(event, form)
    });

    doPost.fail(function (response){
      if (response.responseJSON.msg) {
          showMessage("#comment-message", response.responseJSON.msg, "alert-danger");
      }
    });
  }

  function showMessage(idDivMessage, message, classMessage){
    $(idDivMessage).html(message);
    $(idDivMessage).css("display","");
    $(idDivMessage).removeClass("alert-danger").removeClass("alert-warning").addClass(classMessage);
  }

  function refreshCommentList(event, form){
    var urlRequest = '/idea/comments/' + form.data().ideaId;
    $.ajax({
      url: urlRequest,
      dataType: 'json',
      success: function (data){
        $("#comments-list").html(data.html_list);
      }
    });
  }

  $(document).on("submit", "#commentForm", function (event) {
    submitEvent(event, $(this));
  });

  var newCommentForm = `
    <form id="commentFormReply" class="form-horizontal" action="/post/comment/">
      <div class="form-group">
        <label for="commentContent">Reply Comment</label>
        <textarea class="form-control" id="commentContent" rows="3"></textarea>
        <span id="postResponse" class="text-success" style="display: none"></span>
      </div>
      <div class="form-group">
        <button type="submit" class="btn btn-primary">Post Reply</button>
      </div>
    </form>
  `;
  // var newCommentForm = '<form id="commentFormReply" class="form-horizontal" \
  //                             action="/post/comment/"\
  //                             >\
  //                             <fieldset>\
  //                             <div class="form-group comment-group">\
  //                                 <label for="commentContent" class="col-lg-2 control-label">Reply</label>\
  //                                 <div class="col-lg-10">\
  //                                     <textarea class="form-control" rows="3" id="commentContent"></textarea>\
  //                                     <span id="postResponse" class="text-success" style="display: none"></span>\
  //                                 </div>\
  //                             </div>\
  //                             <div class="form-group">\
  //                                 <div class="col-lg-10 col-lg-offset-2">\
  //                                     <button type="submit" class="btn btn-primary">Comentar</button>\
  //                                 </div>\
  //                             </div>\
  //                         </fieldset>\
  //                     </form>';

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

  $('iframe').load( function() {
    console.log("iframe css");
      $('iframe').contents().find("head").append($("<style type='text/css'>  .b-agent-demo .b-agent-demo_header{min-height:50px!important;height:50px!important}.b-agent-demo .b-agent-demo_header-icon{top:4px!important}.b-agent-demo .b-agent-demo_header-description{padding-top:0!important}  </style>"));
  });

});


function filterIdeas(url){
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    success: function (data){
      $("#idea-list-group").html(data.html_idea_list);
    }
  });
};

$('body').on('click', 'li', function(ev) {
      $('li.active').removeClass('active');
      $('a.active').removeClass('active');
      ev.target.classList.add("active");
      $(this).addClass('active');
});

$('#idea-tab a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
})

$('#idea-pills-tab a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
})



// tooltip functions

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(function () {
  $('[data-toggle="tooltip"]').tooltip({ trigger: 'click' });
});

// end of tooltip functions

$("#evaluation_form button").click(function(){
  if($(window).scrollTop() > $("#idea-tab").offset().top){
       $('html, body').animate({
          scrollTop: $("#idea-tab").offset().top
      }, 500);
    }
    console.log($("#evaluation-message").offset().top);
  $("#evaluation").animate({
          scrollTop: 0
      }, 500);
});



//chatbot
