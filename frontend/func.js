async function generate_letter() {
  const fname = document.getElementById("fname").value;
  const lname = document.getElementById("lname").value;
  const doj = document.getElementById("doj").value;
  const ctc = document.getElementById("ctc").value;
  const position = document.getElementById("position").value;
  const address = document.getElementById("address").value;
  var today = new Date();
  var date =
    today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();

  await fetch("http://localhost:8000/generate-letter", {
    method: "POST",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
      Accept: "application/pdf",
    },
    body: JSON.stringify({
      type: "offer",
      data: {
        hr_id: 123,
        letter_date: date,
        emp_address: address,
        emp_name: fname + " " + lname,
        emp_designation: position,
        joining_date: doj,
        emp_ctc: ctc,
      },
    }),
  })
    .then((response) => response.blob())
    .then((blob) => {
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = "file.pdf";
      document.body.appendChild(a);
      a.click();
      a.remove();
    });

  alert("Returning");
}

async function submit_data() {
  const fname = document.getElementById("fname").value;
  const lname = document.getElementById("lname").value;
  const doj = document.getElementById("doj").value;
  const ctc = document.getElementById("ctc").value;
  const position = document.getElementById("position").value;
  const address = document.getElementById("address").value;

  // if(fname === "" || lname === "" || date == "" || ctc == "" || position == "" || address == "") {
  //     return
  // }

  var today = new Date();
  var date =
    today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();
  await fetch("http://localhost:8000/submit-form", {
    method: "POST",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
    },
    body: JSON.stringify({
      type: "offer",
      data: {
        hr_id: 123,
        letter_date: date,
        emp_address: address,
        emp_name: fname + " " + lname,
        emp_designation: position,
        joining_date: doj,
        emp_ctc: ctc,
      },
    }),
  })
    .then(async (res) => {
      alert("Form submitted for approval");
    })
    .catch((err) => {
      console.log(err);
      alert("Some error occured. Try again");
    });
}

async function get_breakup() {
  const ctc = document.getElementById("ctc").value;
  await fetch("http://localhost:8000/ctc", {
    method: "POST",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
    },
    body: JSON.stringify({
      ctc: ctc,
    }),
  }).then(async (res) => {
    const data = await res.json();
    console.log(data);
    alert(JSON.stringify(data));
  });
}
