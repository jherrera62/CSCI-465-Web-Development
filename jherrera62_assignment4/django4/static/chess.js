function makeMove()
{
  source = document.getElementById("src").value;
  dest = document.getElementById("dst").value;
  document.getElementById(dest).innerHTML = document.getElementById(source).innerHTML;
  document.getElementById(source).innerHTML="&nbsp";
}
function resetBoard()
{
  window.location.reload()
}
