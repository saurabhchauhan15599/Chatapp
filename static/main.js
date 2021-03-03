var socket = io(
  location.protocol + "//" + document.domain + ":" + location.port
);

// socket.on("connect", function () {
//   socket.emit("my event", { data: "I'm connected!" });
// });

function send() {
  let msgBox = document.getElementById("msgBox");
  socket.emit("msg", msgBox.value);
  msgBox.value = "";
}

socket.on("push", function (data) {
  let msgList = document.getElementById("msgList");
  msgList.innerHTML += "<p>" + data + "</p>";
});

function fetchUsers() {
  fetch("/users").then(function (res) {
    res.json().then(function (data) {
      console.log(data);
    });
  });
}
