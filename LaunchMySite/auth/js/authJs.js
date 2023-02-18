const createURL = 'http://127.0.0.1:8000/api/v2/auth/users/'

const btn = document.querySelector('.js-registerbtn');


btn.addEventListener('click', () => {
    const email = document.querySelector('.js-email').value;
    const passwordOne = document.querySelector('.js-password-one').value;
    const passwordTwo = document.querySelector('.js-password-two').value;
    const name = document.querySelector('.js-name').value;

    const password = (passwordOne === passwordTwo) ? passwordOne : alert('Повторите пароль!')

    const options = {
        method: 'POST',
        body: JSON.stringify({
            'email': email,
            'username': name,
            'password': password

        }),
        headers: {
            "Content-Type": "application/json; charset=UTF-8"
        }

    }

    fetch(createURL, options)
        .then(response => response.json())
        .then(json => console.log(json))
        .then(window.location.href = 'http://127.0.0.1:8000/api-auth/login/')
        .catch(() => {
            console.log('error')
        });
})
