const user = document.querySelectorAll('#id_username')
const password = document.querySelectorAll('#id_password')

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

password.forEach((input) => {
    input.addEventListener('focus', addcl)
    input.addEventListener('blur', remcl)
})
