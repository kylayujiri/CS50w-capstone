document.addEventListener('DOMContentLoaded', () => {

  // event handler for register and login

  if (document.querySelector('#register-button') != null) {
    document.querySelector('#register-button').onclick = () => {
      modalFunctionality('register');
      return false;
    }
  }

  if (document.querySelector('#login-button') != null) {
    document.querySelector('#login-button').onclick = () => {
      modalFunctionality('login');
      return false;
    }
  }


});


function modalFunctionality(modalType, message="") {
  // called when register or login buttons are pressed
  // modalType will be 'register' or 'login'

  // clear out the form fields
  if (message != "") {
    document.querySelector('#modal-alert').innerHTML = message;
    document.querySelector('#modal-alert').style.display = 'block';
  } else {
    document.querySelector('#modal-alert').style.display = 'none';

    document.querySelector('#modal-username').value = '';
    document.querySelector('#modal-email').value = '';
    document.querySelector('#modal-password').value = '';
    document.querySelector('#modal-confirm').value = '';
  }

  // edit the modal depending on if its register or login
  if (modalType === 'login') {
    document.querySelector('#modal-email').style.display = 'none';
    document.querySelector('#modal-confirm').style.display = 'none';

    document.querySelector('#modal-label').innerHTML = "Login";

    document.querySelector('#modal-span').innerHTML = "Don't";

    document.querySelector('#modal-link').innerHTML = "Sign up";

    document.querySelector('#submit-modal').innerHTML = "Login";
  } else {
    document.querySelector('#modal-email').style.display = 'block';
    document.querySelector('#modal-confirm').style.display = 'block';

    document.querySelector('#modal-label').innerHTML = "Register";

    document.querySelector('#modal-span').innerHTML = "Already";

    document.querySelector('#modal-link').innerHTML = "Log in";

    document.querySelector('#submit-modal').innerHTML = "Register";
  }

  // show the modal
  $("#reg-modal").modal("show");

  // if the user presses cancel, close the modal
  document.querySelector('#cancel-modal').onclick = () => {
    $('#reg-modal').modal("hide");
  }

  // if the user presses #modal-link, switch the modal
  document.querySelector('#modal-link').onclick = () => {
    if (modalType === 'register') {
      modalFunctionality('login');
    } else {
      modalFunctionality('register');
    }

    return false;
  }

  // if the user submits the modal
  document.querySelector('#submit-modal').onclick = event => {
    event.preventDefault();

    const formUsername = document.querySelector('#modal-username');
    const formPassword = document.querySelector('#modal-password');

    if (modalType === 'register') {

      const formEmail = document.querySelector('#modal-email');
      const formConfirm = document.querySelector('#modal-confirm');

      fetch('/portfolio/register', {
        method: 'POST',
        body: JSON.stringify({
          username: formUsername.value,
          email: formEmail.value,
          password: formPassword.value,
          confirm: formConfirm.value,
          // how to send csrf token?
        })
      })
      .then(response => response.json())
      .then(result => {
        // print result
        console.log(result);

        if (result.message != null && result.message != "User created successfully.") {
          modalFunctionality(modalType, result.message)
        } else {
          // close modal
          $('#reg-modal').modal('hide');

          // scroll to top of page
          window.scrollTo(0,0);

          // display alert
          // TODO
        }

      })

    } else {

      fetch('/login', {
        method: 'POST',
        body: JSON.stringify({
          username: formUsername.value,
          password: formPassword.value,
        })
      })
      .then(response => response.json())
      .then(result => {
        // print result
        console.log(result);

        if (result.message != null && result.message != "User logged in successfully") {
          modalFunctionality(modalType, result.message)
        }

        // close modal
        $('#reg-modal').modal('hide');

      })

    }

  }

}
