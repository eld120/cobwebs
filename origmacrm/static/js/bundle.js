(function () {
  'use strict';

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  function enableFormButton(formElement, buttonElement) {
    // enables/disables address submit button
    let requiredInputs = formElement.querySelectorAll("[required]");
    let emptyInputs = [...requiredInputs].filter((ele) => ele.value.trim() == "");
    buttonElement.disabled = true;
    if (emptyInputs.length === 0 && formElement.checkValidity()) {
      buttonElement.disabled = false;
    }
  }

  // POST or PUT address data to /api1/
  async function submitAddressData(url) {
    const dataObject = Alpine.store("addressData");
    const httpVerb = Alpine.store("createOrUpdate");

    if (httpVerb.method === "POST") {
      await axios
        .post(
          url,
          {
            primary: dataObject.addressPrimary ? "y" : "n",
            name: dataObject.addressName,
            address_1: dataObject.addressOne,
            address_2: dataObject.addressTwo,
            city: dataObject.addressCity,
            state: dataObject.addressState,
            zip_code: dataObject.addressZipCode,
            phone: dataObject.addressPhone,
            email: dataObject.addressEmail,
            active: dataObject.addressActive,
            start_date: dataObject.addressStartDate,
            end_date: dataObject.addressEndDate,
          },
          {
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            mode: "same-origin",
          }
        )
        // need error handling
        .catch((error) => console.log(error));
    } else {
      await axios
        .put(
          url + dataObject.addressUUID + "/",
          {
            primary: dataObject.addressPrimary ? "y" : "n",
            name: dataObject.addressName,
            address_1: dataObject.addressOne,
            address_2: dataObject.addressTwo,
            city: dataObject.addressCity,
            state: dataObject.addressState,
            zip_code: dataObject.addressZipCode,
            phone: dataObject.addressPhone,
            email: dataObject.addressEmail,
            active: dataObject.addressActive,
            start_date: dataObject.addressStartDate,
            end_date: dataObject.addressEndDate,
          },
          {
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            mode: "same-origin",
          }
        )
        .catch((error) => console.log(error));
    }
  }

  // Get list of billing and shipping addresses

  // creates or updates billing or shipping addresses

  Alpine.store("customerData");
  // Gets customer data
  async function getCustomerData(url, uuid) {
    const request = await fetch(`/${url}/${uuid}/`);

    const response = await request.json();


    Alpine.store("customerData", {

      customerDBA: response.dba,
      customerUUID: response.uuid,
      customerName: response.name,
      customerBillingAddress: response.billing_address,
      customerShippingAddresses: response.shipping_addresses,
      customerShippingAddressList: response.shipping_addresses_list,
      customerActive: response.active,
      customerActiveOptions: response.active_options,
      customerCustomerType: response.customer_type,
      customerCustomerTypeOptions: response.customer_type_options,
      customerStartDate: response.start_date,
      customerEndDate: response.end_date,
      customerCreatedBy: response.created_by,

  });
  }

  // Customer id/uuid DOM element and Create/Update flag


  document.querySelector("#billingAddressButton");
  document.querySelector("#shippingAddressButton");


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
  //   const updateButtonArray = [billingButton, shippingButton];
  //   const createButtonArray = document.querySelectorAll(".add-btn");
  //   updateButtonArray.forEach((element) => {
  //     element.addEventListener("click", (element) => createOrUpdate(element));
  //   });
  //   createButtonArray.forEach((element) => {
  //     element.addEventListener("click", () => createOrUpdate(element));
  //   });
  }

  const customerUUID = document.querySelector('#customerUUID');
  document.addEventListener('DOMContentLoaded', () => {

    getCustomerData(`api1/customers`, customerUUID.value);
  });

})();
