export {
  enableFormButton,
  createOrUpdate,
  getCookie
};

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

// toggles the title of the address form - should be moved into the address template
function createOrUpdate(button) {
  if (button.id === "updateFlag") {
    Alpine.store("createOrUpdate", {
      title: "Update Address",
      method: "PUT",
    });

  } else {
    Alpine.store("createOrUpdate", {
      title: "Create Address",
      method: "POST",
    });
  }
}
