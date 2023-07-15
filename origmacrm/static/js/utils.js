export { getAddressURL, getAddressData, submitAddressData, validateFormButton };

async function getAddressURL(url, type) {
  let customerURL = await axios
    .get("/api1/customers/" + url)
    .catch((error) => console.log(error));

  if (type == "billing") {
    return getAddressData(customerURL.data.billing_address);
  } else if (type == "shipping") {
    return getAddressData(customerURL.data.shipping_address);
  } else {
    throw new Error("500 Error or missing address type");
  }
}

async function getAddressData(url) {
  let addressURL = await axios.get(url).catch((err) => console.log(err));

  return Alpine.store("addressData", {
    addressOne: addressURL.data.address_1,
    addressTwo: addressURL.data.address_2,
    addressCity: addressURL.data.city,
    addressState: addressURL.data.state,
    addressZipCode: addressURL.data.zip_code,
    addressPhone: addressURL.data.phone,
    addressEmail: addressURL.data.email,
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
  console.log('inside the function')
  let requiredInputs = formElement.querySelectorAll("[required]");
  let emptyInputs = [...requiredInputs].filter(ele => ele.value.trim() == "");
  if (emptyInputs.length == 0){
    buttonElement.disabled = false;
    console.log('winner')
  }
}
