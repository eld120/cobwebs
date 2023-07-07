import { getAddressURL } from "./utils.js";

// DOM
const objectUUID = document.querySelector("#customerUUID");
const updateTag = document.querySelector("#updateTag")
const addAddressBtn = document.querySelectorAll(".add-btn")
const addressModal = document.querySelector('#createAddressModal')
const addressForm = document.querySelector("#addressForm");

// event listeners on the DOM
if (objectUUID != null && updateTag != null) {
  let custUUID = objectUUID.value;

  document
    .querySelector("#billingAddressButton")
    .addEventListener("click", () => getAddressURL(custUUID, "billing"));

  document
    .querySelector("#shippingAddressButton")
    .addEventListener("click", () => getAddressURL(custUUID, "shipping"));
}
addAddressBtn.forEach((element) => {
    element.addEventListener("click", ()=> {


    })
});

// event resetting address model on close
addressModal.addEventListener('hidden.bs.modal', ()=>{
    addressForm.reset()
  })


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
