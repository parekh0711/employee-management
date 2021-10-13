var bcrypt = dcodeIO.bcrypt;
console.log("Hello HR");
const backendURL = "http://localhost:8000";

const login = async () => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const type = document.getElementById("typer").value;
  console.log(username, password, type);

  if (username === "" || password === "" || type === "") {
    return;
  }
  // Make login request and send response
  await fetch(backendURL + "/login", {
    method: "POST",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
    },
    body: JSON.stringify({
      username: username,
      type: type === "Super Admin" ? "admin" : "junior",
    }),
  }).then(async (res) => {
    const data = await res.json();
    console.log(data);
    if (Object.keys(data).length == 0) {
      alert("Wrong credentials");
      return;
    }
    await bcrypt.compare(password, data["passwd"], (err, res) => {
      if (err) {
        console.error(err);
        return;
      }
      alert("Login Success");
      const page =
        type === "Super Admin"
          ? "/frontend/ad_home.html"
          : "/frontend/jr_home.html";
      if (res == true) {
        localStorage.setItem("user", JSON.stringify(username));
        window.history.pushState(
          { data: "Logged in" },
          "Login Successful",
          window.location.origin + page
        );
        window.location.reload();
      } else {
        alert("Wrong credentials");
      }
      return res;
    });
  });
};

const register = async () => {
  const email = document.getElementById("email").value;
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const type = document.getElementById("typer").value;

  if (username === "" || password === "" || type === "" || email === "") {
    return;
  }
  console.log(type);

  console.log(username, password, email);
  const rounds = 10;
  await bcrypt.hash(password, rounds, async (err, hash) => {
    if (err) {
      console.error(err);
      return;
    }
    await fetch(backendURL + `/register`, {
      mode: "no-cors",
      method: "POST",
      body: JSON.stringify({
        username: username,
        passwd: hash,
        emailid: email,
        type: type === "Super Admin" ? "admin" : "junior",
      }),
    }).then((res) => {
      alert("Registered successfully");
      console.log(res);
    });
  });
  // Make register request with data
};
