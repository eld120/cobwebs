export { getAddressURL, getAddressData };


async function getAddressURL(url, type) {

    let customerURL = await axios.get('/api1/customers/'+ url)//.catch((error) => console.log(error))

    if (type == 'billing'){
        return getAddressData(customerURL.data.billing_address)
    }
    else if( type == 'shipping'){
        return getAddressData(customerURL.data.shipping_address)
    }
    else{
        return null
    }


  }



async function getAddressData(url){
    let addressURL = await axios.get(url)//.catch((err)=> console.log(err))

    console.log(addressURL.data.city)
    return Alpine.store('addressData', {
        addressOne: addressURL.data.address_1,
        addressTwo: addressURL.data.address_2,
        addressCity: addressURL.data.city,
        addressState: addressURL.data.state,
        addressZipCode: addressURL.data.zip_code,
        addressPhone: addressURL.data.phone,
        addressEmail: addressURL.data.email,

    })
}
