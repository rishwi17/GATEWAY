const user = document.querySelectorAll('#id_username')
const flat = document.querySelectorAll('#id_flatNo')
const email = document.querySelectorAll('#id_email')
const password1 = document.querySelectorAll('#id_password1')
const password2 = document.querySelectorAll('#id_password2')

function addcl() {
    let parent = this.parentNode.parentNode
    parent.classList.add('focus')
}

function remcl() {
    let parent = this.parentNode.parentNode
    if (this.value == '') {
        parent.classList.remove('focus')
    }
}

user.forEach((input) => {
    input.addEventListener('focus', addcl)
    input.addEventListener('blur', remcl)
})

email.forEach((input) => {
    input.addEventListener('focus', addcl)
    input.addEventListener('blur', remcl)
})

password1.forEach((input) => {
    input.addEventListener('focus', addcl)
    input.addEventListener('blur', remcl)
})

password2.forEach((input) => {
    input.addEventListener('focus', addcl)
    input.addEventListener('blur', remcl)
})

flat.forEach((input) => {
    input.addEventListener('focus', addcl)
    input.addEventListener('blur', remcl)
})
