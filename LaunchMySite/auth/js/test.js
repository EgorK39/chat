const btn = document.querySelector('.js-registerbtn');


btn.addEventListener('click', () => {
    const email = document.querySelector('.js-email').value;
    const passwordOne = document.querySelector('.js-password-one').value;
    const passwordTwo = document.querySelector('.js-password-two').value;
    const name = document.querySelector('.js-name').value;

    const password = (passwordOne === passwordTwo) ? passwordOne : alert('Повторите пароль!')
    console.log(email, name, password)
    console.log(typeof (email), typeof (name), typeof (password))

})
