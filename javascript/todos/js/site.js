$(document).ready(function() {
  $('#input').on("keypress", function(event) {
    if (event.which === 13) {
      var item = $("<li/>");
      item.text($(this).val());

      var checkbox = $("<input type='checkbox'>");
      checkbox.click(function() {
      $(this).parent().toggleClass("strike");
      });
      item.prepend(checkbox);

      var remove = $("<button/>");
      remove.text('Remove');
      remove.click(function() {
      $(this).parent().remove();
      });

      $('#todos').append(item);
      $('#todos').append(remove);
      $(this).val("");

    }
  });
});
