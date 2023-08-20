export { getAddressData, submitAddressData };
import { getCookie } from "./utils.js";

async function getAddressData(url) {
  //
   const request = await fetch(`${url}`).catch((err) => console.log(`-------- getAddressData error -------- ${err}`));
   const addressData = request.json()

  return Alpine.store("addressData", {
    addressUUID: addressData.data.uuid,
    addressPrimary: addressData.data.primary,
    addressName: addressData.data.name,
    addressOne: addressData.data.address_1,
    addressTwo: addressData.data.address_2,
    addressCity: addressData.data.city,
    addressState: addressData.data.state,
    addressZipCode: addressData.data.zip_code,
    addressPhone: addressData.data.phone,
    addressEmail: addressData.data.email,
    addressActive: addressData.data.active,
    addressStartDate: addressData.data.start_date,
    addressEndDate: addressData.data.end_date,
  })
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
