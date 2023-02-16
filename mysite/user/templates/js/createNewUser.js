const createURL = 'http://127.0.0.1:8000/api/v2/auth/users/'

const btn = document.querySelector('.js-registerbtn');
const email = document.querySelector('.js-email');
const passwordOne = document.querySelector('.js-password-one');
const passwordTwo = document.querySelector('.js-password-two');
const name = document.querySelector('.js-name');


btn.addEventListener('click', () => {
    const options = {
        method: 'POST',
        body: JSON.stringify({
            'email': email,
            'username': name,
            'password': passwordOne
        }),
        headers: {
            "Content-Type": "application/json; charset=UTF-8"
        }
    }

    fetch(createURL, options)
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(() => {
            console.log('error')
        });
})
