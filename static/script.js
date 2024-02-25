const fetch_data = async () => {
  fetch("/get-data", {
    // Adding method type
    method: "POST",

    // Adding body or contents to send
    body: JSON.stringify({
      title: "foo",
      body: "bar",
      userId: 1,
    }),

    // Adding headers to the request
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const tableBody = document
        .getElementById("dataTable")
        .getElementsByTagName("tbody")[0];
      tableBody.innerHTML = '';
      data.forEach((item) => {
        let row = tableBody.insertRow();
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        cell1.innerHTML = item[0];
        cell2.innerHTML = item[1];
      });
    })
    .catch((error) => console.error("Error loading data:", error));
};

let fetched = 0;

const Get_data_btn = document.getElementById("get_data")
Get_data_btn.addEventListener("click", () => {
  const result = fetch_data();
  console.log(result);
  if(fetched == 0){
    fetched = 1;
  } else {
    fetched = 0;
  }
});

setInterval(() => {
  if(fetched == 1){
    Get_data_btn.click()    
  }
}, 5000);