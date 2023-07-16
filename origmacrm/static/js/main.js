import { getAddressURL, submitAddressData, validateFormButton, createOrUpdate } from "./utils.js";

// Customer id/uuid DOM element and Create/Update flag
const customerUUID = document.querySelector("#customerUUID");
const updateFlag = document.querySelector("#updateFlag")
const billingButton = document.querySelector("#billingAddressButton")
const shippingButton = document.querySelector("#shippingAddressButton")

// event listeners on the DOM
if (customerUUID != null && updateFlag != null) {
  let custUUID = customerUUID.value;

  billingButton.addEventListener("click", () => getAddressURL(custUUID, "billing"));
  shippingButton.addEventListener("click", () => getAddressURL(custUUID, "shipping"));
}

// address Modal and form DOM elements
const addressModal = document.querySelector('#createAddressModal')
const addressForm = document.querySelector("#addressForm");
const addressButton = document.querySelector('#addressFormSubmit');


if (addressModal) {
// event resetting address model on close
addressModal.addEventListener('hidden.bs.modal', ()=>{
    addressForm.reset()
  })

// event submission to handle creation/updating addresses
addressButton.addEventListener('click', ()=>{
  // desperately need POST vs PUT handling/UX thought process

  submitAddressData('/api1/addresses/', 'POST')
  const modal = bootstrap.Modal.getInstance(addressModal)
  // need to implement error handling in the form before the modal is hidden/reset

  modal.hide()
  addressForm.reset()

})

// event to validate whether all input fields contain values


// addressModal.querySelectorAll('input').forEach((element)=>{
//   element.addEventListener('input', (event)=>{
//     validateFormButton(addressForm, addressButton)
//     })
// })



  addressModal.addEventListener('input', (event) =>{
    validateFormButton(addressForm, addressButton)
    })
}

const updateArray = [billingButton, shippingButton];
const createArray = document.querySelectorAll('.add-btn');
updateArray.forEach((element)=>{
  element.addEventListener('click', ()=>
  createOrUpdate(element))
})
createArray.forEach((element)=>{
  element.addEventListener('click', ()=>
  createOrUpdate(element))
})
