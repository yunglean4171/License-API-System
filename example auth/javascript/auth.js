const axios = require('axios');

const lkey = "123";
const id = "456";

axios.get("http://127.0.0.1:5000/"+lkey+"/"+id)
  .then(response => {
    if (response.data == "true") {
        console.log("access granted")
    } else if (response.data == "false") {
        console.log("access denied")
    }
  })
  .catch(error => {
    if (error.response) {
      //get HTTP error code
      console.log(error.reponse.status)
    } else {
      console.log(error.message)
    }
  })