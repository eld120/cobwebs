import { getAddressURL, getCookie, submitAddressData } from "./utils.js";

// DOM
const objectUUID = document.querySelector("#customerUUID");
const updateTag = document.querySelector("#updateTag")

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


const addressModal = document.querySelector('#createAddressModal')
const addressForm = document.querySelector("#addressForm");
const addressButton = document.querySelector('#addressFormSubmit');

// event resetting address model on close
addressModal.addEventListener('hidden.bs.modal', ()=>{
    addressForm.reset()
  })

// event submission to handle creation/updating addresses
addressButton.addEventListener('click', ()=>{
  // desperately need POST vs PUT handling/UX thought process
  submitAddressData('/api1/addresses/', 'POST')
  const modal = bootstrap.Modal.getInstance(addressModal)
  modal.hide()
  addressForm.reset()

})
