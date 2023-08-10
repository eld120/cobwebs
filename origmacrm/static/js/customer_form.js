// Get list of billing and shipping addresses

// creates or updates billing or shipping addresses

const customerData = Alpine.store('customerData')
// Gets customer data
async function getCustomerData(url, uuid){
   const request = await fetch(`/${url}/${uuid}/`)
   const response = await request.json()
   return Alpine.store('customerData',{
    customerDBA: response.data.dba,
    customerName: response.data.name,
    customerUUID: response.data.uuid,
    customerBillingAddress: response.data.billing_address,
    customerShippingAddress: response.data.shipping_addresses,
    customerActive: response.data.active,
    customerCustomerType: response.data.customer_type,
    customerStartDate: response.data.start_date,
    customerEndDate: response.data.end_date,
   })
}

// fetch data that should update form state or options
async function customerFormData(url){
    const request = await fetch(`${url}`)
    const response = request.json()
    return Alpine.store('customerData',{
        // customerIndustryOptions: response.data.???,
        // customerActiveOptions: response.data.???,
        // customerBillingList: response.data.???,
        // customerShippingList: response.data.???,
        // customerPrimaryOptions: response.data.???,
        //
    })
}

async function setCustomerData(url, uuid=null){
    if(uuid === null){

    }
}
