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

});


function filterIdeas(url){
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    success: function (data){
      $("#idea-list").html(data.html_idea_list);
    }
  });
};

$('body').on('click', 'li', function() {
      $('li.active').removeClass('active');
      $(this).addClass('active');
});
