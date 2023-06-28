

// DOM URL
const objectUUID = document.querySelector('#customerUUID')
if (objectUUID != null){
    custUUID = objectUUID.value

    // event listeners on the DOM
document
.querySelector("#billingAddressButton")
.addEventListener("click", ()=> getAddressData(custUUID, 'billing').then((data)=> console.log(data)));

document
.querySelector("#shippingAddressButton")
.addEventListener("click", ()=> getAddressData(custUUID, 'billing').then((data)=> console.log(data)));
//   .catch((error) => console.log(error));

}

async function getAddressData(url, type) {
    let customerData = await axios.get('/api1/customers/'+ url).catch((error) => console.log(error))


    return customerData.


  }



// document.querySelector("#addressForm").addEventListener('click', ()=> console.log("FOUND IT"))

// document.querySelector("#addressForm").addEventListener('submit',
//     (formData) => formData.preventDefault() )

async function getAddress(url) {
  let addressData = await axios
    .get(url)
    .then((res) => console.log(res))
    .catch((err) => console.log(err));

  // return{
  // 'addressOne': addressData.address_1,
  // 'addressTwo' : addressData.address_2 ,
  // 'city' : addressData.city,
  // 'state' :  addressData.state,
  // 'zipCode' : addressData.zip_code,
  // 'phoneNumber' : addressData.phone,
  // 'emailAddress' : addressData.email,
  // }
}

// document.addEventListener("alpine:init", () => {
//   Alpine.store( 'addressData' , {
//     'addressOne': addressOne,
//     'addressTwo' : addressTwo ,
//     'city' : city,
//     'state' :  state,
//     'zipCode' : zipCode,
//     'phoneNumber' : phoneNumber,
//     'emailAddress' : emailAddress,}
//   );
// });
