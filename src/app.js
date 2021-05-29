function geturl() {
  var url = document.getElementById("url").value
  eel.download(url)(setImage)
}
