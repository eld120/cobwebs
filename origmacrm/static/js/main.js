import { enableFormButton, createOrUpdate } from "./utils.js";
import { getAddressFromCustomer, submitAddressData } from "./address_form.js";

// Customer id/uuid DOM element and Create/Update flag
const customerUUID = document.querySelector("#customerUUID");
const updateFlag = document.querySelector("#updateFlag");
const billingButton = document.querySelector("#billingAddressButton");
const shippingButton = document.querySelector("#shippingAddressButton");
// customer/address form address listeners
if (customerUUID != null && updateFlag != null) {
  let custUUID = customerUUID.value;
  billingButton.addEventListener("click", () =>
    getAddressFromCustomer(custUUID, "billing")
  );
  shippingButton.addEventListener("click", () =>
    getAddressFromCustomer(custUUID, "shipping")
  );
}

// address Modal and form DOM elements
const addressModal = document.querySelector("#createAddressModal");
const addressForm = document.querySelector("#addressForm");
const addressButton = document.querySelector("#addressFormSubmit");
if (addressModal) {
  // event resetting address model on close
  addressModal.addEventListener("hidden.bs.modal", () => {
    addressForm.reset();
  });

  addressButton.addEventListener("click", () => {
    submitAddressData("/api1/addresses/");
    const modal = bootstrap.Modal.getInstance(addressModal);
    // need to implement error handling in the form before the modal is hidden/reset
    modal.hide();
    addressForm.reset();
  });
  // event to validate whether all input fields contain values
  addressModal.addEventListener("input", () => {
    enableFormButton(addressForm, addressButton);
  });

  // sets Address Modal title to Create or Update
  const updateButtonArray = [billingButton, shippingButton];
  const createButtonArray = document.querySelectorAll(".add-btn");
  updateButtonArray.forEach((element) => {
    element.addEventListener("click", (element) => createOrUpdate(element));
  });
  createButtonArray.forEach((element) => {
    element.addEventListener("click", () => createOrUpdate(element));
  });
}
