const form = document.querySelector('.needs-validation')

form.addEventListener('submit', (event) => {
  event.preventDefault()
  event.stopPropagation()
  form.classList.add('was-validated')

  if (form.checkValidity()) {
    alert('Pedido ingresado correctamente')
    form.reset()
    form.classList.remove('was-validated')
  }

}, false)
