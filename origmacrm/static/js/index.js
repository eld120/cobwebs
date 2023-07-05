
import { getAddressURL } from "./utils.js";



// DOM
const objectUUID = document.querySelector('#customerUUID')

const addressForm = document.querySelector("#addressForm")

    // event listeners on the DOM
if (objectUUID != null){
        let custUUID = objectUUID.value
        Alpine.store()
document
    .querySelector("#billingAddressButton")
    .addEventListener("click", ()=> getAddressURL(custUUID, 'billing'));

document
    .querySelector("#shippingAddressButton")
    .addEventListener("click", ()=> getAddressURL(custUUID, 'shipping'));
    //   .catch((error) => console.log(error));

}

document.addEventListener('alpine:init', () => {
    Alpine.store('addressData', {
        addressOne: '',
        addressTwo: '',
        addressCity: '',
        addressState: '',
        addressZipCode: '',
        addressPhone: '',
        addressEmail: '',
        })
        }
    )



// document.querySelector("#addressForm").addEventListener('submit',
//     (formData) => formData.preventDefault() )

// async function getAddress(url) {
//   let addressData = await axios
//     .get(url)
//     .then((res) => console.log(res))
//     .catch((err) => console.log(err));

  // return{
  // 'addressOne': addressData.address_1,
  // 'addressTwo' : addressData.address_2 ,
  // 'city' : addressData.city,
  // 'state' :  addressData.state,
  // 'zipCode' : addressData.zip_code,
  // 'phoneNumber' : addressData.phone,
  // 'emailAddress' : addressData.email,
  // }
// }

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
