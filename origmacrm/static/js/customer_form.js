// Get list of billing and shipping addresses

// creates or updates billing or shipping addresses

const customerData = Alpine.store("customerData");
// Gets customer data
async function getCustomerData(url, uuid) {
  const request = await fetch(`/${url}/${uuid}/`);
  const response = request.json();
  return Alpine.store("customerData", {
    customerDBA: response.data.dba,
    customerName: response.data.name,
    customerUUID: response.data.uuid,
    customerBillingAddress: response.data.billing_address,
    customerShippingAddress: response.data.shipping_addresses,
    customerActive: response.data.active,
    customerCustomerType: response.data.customer_type,
    customerStartDate: response.data.start_date,
    customerEndDate: response.data.end_date,
    customerCreatedBy: response.data.created_by,

})
}



// async function setCustomerData(url, uuid = null) {
//   if (uuid === null) {
//   }
//  }
