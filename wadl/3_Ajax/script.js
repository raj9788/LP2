function saveData() {
  // Get form input values
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var phoneno = document.getElementById("phoneno").value;

  // Create an object to hold the data
  var user = {
    name: name,
    email: email,
    password: password,
    phoneno: phoneno,
  };

  // Make an AJAX POST request to save the data
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "save-data.php");
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send(JSON.stringify(user));

  // Save the data to local storage
  var users = JSON.parse(localStorage.getItem("userslist")) || [];
  users.push(user);
  localStorage.setItem("userslist", JSON.stringify(users));

  //  function showData(){
  // Redirect to the data list page
  //}
  //localStorage.clear();
}
