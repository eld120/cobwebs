export { getAddressData, getAddressFromCustomer, submitAddressData };
import { getCookie } from "./utils.js";

async function getAddressData(url, type) {
  // Going to need to handle a single address being returned as well as an array of addresses <- idk if this is true anymore
  const addressData = await axios.get(`${url}`).catch((err) => console.log(err));

  if (type === 'billing'){
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
    addressUUID: addressData.data.uuid,
    addressActive: addressData.data.active,
    addressStartDate: addressData.data.start_date,
    addressEndDate: addressData.data.end_date,
  });}
  else{
    return Alpine.store("addressData",{
      shippingAddressList: [...addressData.data]
    })
  }
}

// the address data retrieval could/should be moved into Django
// minimally a single api call could/should solve this
async function getAddressFromCustomer(uuid, type) {
  // returns a given customer's address data object
  const customerURL = await axios
    .get(`/api1/customers/${uuid}/`)
    .catch((error) => console.log(error));

  if (type === "billing") {
    return getAddressData(customerURL.data.billing_address, 'billing');
  } else if (type === "shipping") {
    return getAddressData(customerURL.data.shipping_addresses, 'shipping');
  } else {
    throw new Error("500 Error or missing address type");
  }
}

// POST or PUT address data to /api1/
async function submitAddressData(url) {
  const dataObject = Alpine.store("addressData");
  const httpVerb = Alpine.store("createOrUpdate");

  if (httpVerb.method === "POST") {
    await axios
      .post(
        url,
        {
          primary: dataObject.addressPrimary ? "y" : "n",
          name: dataObject.addressName,
          address_1: dataObject.addressOne,
          address_2: dataObject.addressTwo,
          city: dataObject.addressCity,
          state: dataObject.addressState,
          zip_code: dataObject.addressZipCode,
          phone: dataObject.addressPhone,
          email: dataObject.addressEmail,
          active: dataObject.addressActive,
          start_date: dataObject.addressStartDate,
          end_date: dataObject.addressEndDate,
        },
        {
          headers: { "X-CSRFToken": getCookie("csrftoken") },
          mode: "same-origin",
        }
      )
      // need error handling
      .catch((error) => console.log(error));
  } else {
    await axios
      .put(
        url + dataObject.addressUUID + "/",
        {
          primary: dataObject.addressPrimary ? "y" : "n",
          name: dataObject.addressName,
          address_1: dataObject.addressOne,
          address_2: dataObject.addressTwo,
          city: dataObject.addressCity,
          state: dataObject.addressState,
          zip_code: dataObject.addressZipCode,
          phone: dataObject.addressPhone,
          email: dataObject.addressEmail,
          active: dataObject.addressActive,
          start_date: dataObject.addressStartDate,
          end_date: dataObject.addressEndDate,
        },
        {
          headers: { "X-CSRFToken": getCookie("csrftoken") },
          mode: "same-origin",
        }
      )
      .catch((error) => console.log(error));
  }
}
