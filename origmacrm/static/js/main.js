import { getAddressURL, submitAddressData, validateFormButton } from "./utils.js";

// Customer id/uuid DOM element and Create/Update flag
const customerUUID = document.querySelector("#customerUUID");
const updateFlag = document.querySelector("#updateFlag")

// event listeners on the DOM
if (customerUUID != null && updateFlag != null) {
  let custUUID = customerUUID.value;

  document
    .querySelector("#billingAddressButton")
    .addEventListener("click", () => getAddressURL(custUUID, "billing"));

  document
    .querySelector("#shippingAddressButton")
    .addEventListener("click", () => getAddressURL(custUUID, "shipping"));
}

// address Modal and form DOM elements
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
  // need to implement error handling in the form before the modal is hidden/reset

  modal.hide()
  addressForm.reset()

})

// event to validate whether all input fields contain values
addressModal.addEventListener('input', () =>{
  validateFormButton(addressForm, addressButton)

}
)
