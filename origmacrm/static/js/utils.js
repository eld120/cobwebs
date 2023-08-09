export { getAddressFromCustomer, submitAddressData, enableFormButton, createOrUpdate };


// the address data retrieval could/should be moved into Django
// minimally a single api call could/should solve this
async function getAddressFromCustomer(uuid, type) {
  // returns a given customer's address data object
  const customerURL = await axios
    .get("/api1/customers/" + uuid)
    .catch((error) => console.log(error));

  if (type === "billing") {
    return getAddressData(customerURL.data.billing_address);
  } else if (type === "shipping") {
    return getAddressData(customerURL.data.shipping_addresses);
  } else {
    throw new Error("500 Error or missing address type");
  }
}

async function getAddressData(url) {
  // Going to need to handle a single address being returned as well as an array of addresses <- idk if this is true anymore
  const addressData = await axios.get(url).catch((err) => console.log(err));

  return Alpine.store("addressData", {
    addressPrimary: addressData.data.primary,
    addressName: addressData.data.name,
    addressOne: addressData.data.address_1,
    addressTwo: addressData.data.address_2,
    addressCity: addressData.data.city,
    addressState: addressData.data.state,
    addressZipCode: addressData.data.zip_code,
    addressPhone: addressData.data.phone,
    addressEmail: addressData.data.email,
    addressUUID: addressData.data.uuid
  });
}

async function submitAddressData(url) {
  const dataObject = Alpine.store("addressData")
  const httpVerb = Alpine.store('createOrUpdate')

if (httpVerb.method === "POST") {
    await axios
      .post(url, {
        primary:  dataObject.addressPrimary ? "y" : "n",
        name: dataObject.addressName,
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
    console.log(httpVerb)
    await axios
      .put(url + dataObject.addressUUID+'/', {
        primary: dataObject.addressPrimary ? "y" : "n",
        name: dataObject.addressName,
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

function enableFormButton(formElement, buttonElement){
  // enables/disables address submit button
  let requiredInputs = formElement.querySelectorAll("[required]");
  let emptyInputs = [...requiredInputs].filter(ele => ele.value.trim() == "");
  buttonElement.disabled = true
  if (emptyInputs.length === 0 && formElement.checkValidity()){
    buttonElement.disabled = false;
  }
}


function createOrUpdate(button){
  if (button.id === ''){
    // a button without an id is equal to an empty string
    Alpine.store('createOrUpdate',{
      title: "Create Address",
      method: 'POST'
    })
  }else{
    // update buttons have a specific element ID
    Alpine.store('createOrUpdate',{
      title: "Update Address",
      method: 'PUT'
  })
}}
