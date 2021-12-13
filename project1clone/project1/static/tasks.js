function confirmDeleteModal(id) {
  $('#deleteModal').modal();
  $('#deleteButton').html('<a href="?delete='+id+'" class="btn btn-danger" onclick="return closeDeleteModal('+id+')">Delete</a>');
}

function closeDeleteModal(id) {
  $('#deleteModal').modal('hide');
  return true
}
function thisformsubmit()
{
  hide=document.getElementById("id_tasks_view_hide_completed").value;
  if(hide)
  {
    document.getElementById(hide)=False;
  }
  else {
      document.getElementById(hide)=True;
  }
}
