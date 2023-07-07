export { getAddressURL, getAddressData, submitAddressData };

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

async function submitAddressData(url, dataObject, httpVerb) {
  if (httpVerb == "POST") {
    await axios
      .post(url, {
        address_1: dataObject.addressOne,
        address_2: dataObject.addressTwo,
        city: dataObject.addressCity,
        state: dataObject.addressState,
        zip_code: dataObject.addressZipCode,
        phone: dataObject.addressPhone,
        email: dataObject.addressEmail,
      })
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
