export { getAddressFromCustomer, submitAddressData, validateFormButton, createOrUpdate };

async function getAddressFromCustomer(uuid, type) {
  // returns a given customer's address data object
  const customerURL = await axios
    .get("/api1/customers/" + uuid)
    .catch((error) => console.log(error));

  if (type == "billing") {
    return addressDataHelper(customerURL.data.billing_address);
  } else if (type == "shipping") {
    return addressDataHelper(customerURL.data.shipping_address);
  } else {
    throw new Error("500 Error or missing address type");
  }
}

async function addressDataHelper(url) {
  const addressData = await axios.get(url).catch((err) => console.log(err));

  return Alpine.store("addressData", {
    addressOne: addressData.data.address_1,
    addressTwo: addressData.data.address_2,
    addressCity: addressData.data.city,
    addressState: addressData.data.state,
    addressZipCode: addressData.data.zip_code,
    addressPhone: addressData.data.phone,
    addressEmail: addressData.data.email,
  });
}

async function submitAddressData(url, httpVerb) {
  const dataObject = Alpine.store("addressData")

  if (httpVerb == "POST") {
    await axios
      .post(url, {
        // csrf token
        address_1: dataObject.addressOne,
        address_2: dataObject.addressTwo,
        city: dataObject.addressCity,
        state: dataObject.addressState,
        zip_code: dataObject.addressZipCode,
        phone: dataObject.addressPhone,
        email: dataObject.addressEmail,
      },
      {
        headers:{'X-CSRFToken': getCookie('csrftoken')},
        mode: 'same-origin'
      }
        )
        // need error handling
      .catch((error) => console.log(error));
  } else {
    await axios
      .put(url, {
        address_1: dataObject.addressOne,
        address_2: dataObject.addressTwo,
        city: dataObject.addressCity,
        state: dataObject.addressState,
        zip_code: dataObject.addressZipCode,
        phone: dataObject.addressPhone,
        email: dataObject.addressEmail,
      })
      .catch((error) => console.log(error));
  }
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function validateFormButton(formElement, buttonElement){
  let requiredInputs = formElement.querySelectorAll("[required]");
  let emptyInputs = [...requiredInputs].filter(ele => ele.value.trim() == "");
  buttonElement.disabled = true
  if (emptyInputs.length == 0 && formElement.checkValidity()){
    buttonElement.disabled = false;
  }
}


function createOrUpdate(button){

  if (button.id == ''){
    // a button without an id is equal to an empty string
    Alpine.store('createOrUpdate',{
      title: 'Create Address'
    })
  }else{
    // update buttons have a specific element ID
    Alpine.store('createOrUpdate',{
      title: 'Update Address'
  })
}}


// handles POST/PUT on the client based on create/update
function postOrPut(button){
  if (button.id == ''){

  }
  else{

  }

}
