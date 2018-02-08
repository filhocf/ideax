/*
$("#modal-idea").on("submit", ".js-book-create-form", function () {
  var form = $(this);
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    dataType: 'json',
    success: function (data) {
      if (data.form_is_valid) {
        alert("Book created!");  // <-- This is just a placeholder for now for testing
      }
      else {
        $("#modal-idea .modal-content").html(data.html_form);
      }
    }
  });
  return false;
});
*/

function openModal (url) {
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#modal-idea").modal("show");
    },
    success: function (data) {
      $("#modal-idea .modal-content").html(data.html_form);
    }
  });
}

function vote(url, id) {
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    success: function (data) {
      $(id).html(data.qtde_votes);
    }
  });
}
