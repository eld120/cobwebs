export {submitCustomerData, getCustomerData}
import { getCookie } from "./utils.js"
// Get list of billing and shipping addresses

// creates or updates billing or shipping addresses

const customerData = Alpine.store("customerData");
// Gets customer data
async function getCustomerData(url, uuid) {
  const request = await fetch(`/${url}/${uuid}/`);

  const response = await request.json();


  Alpine.store("customerData", {

    customerDBA: response.dba,
    customerUUID: response.uuid,
    customerName: response.name,
    customerBillingAddress: response.billing_address,
    customerShippingAddresses: response.shipping_addresses,
    customerShippingAddressList: response.shipping_addresses_list,
    customerActive: response.active,
    customerActiveOptions: response.active_options,
    customerCustomerType: response.customer_type,
    customerCustomerTypeOptions: response.customer_type_options,
    customerStartDate: response.start_date,
    customerEndDate: response.end_date,
    customerCreatedBy: response.created_by,

})
}

async function submitCustomerData(uuid='') {
  if (uuid) {
    const response = await fetch(`/api1/customers/${uuid}/`, {
      method: "PUT", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: "follow", // manual, *follow, error
      referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    })
    return response.json(); // parses JSO
  }
  const response = await fetch(`/api1/customers/`, {
    method: "POST",
    mode: "cors",
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  })
  return response.json(); // parses JSO
  }
