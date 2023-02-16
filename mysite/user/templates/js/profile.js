function useRequest(url, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);

    xhr.onload = function () {
        if (xhr.status !== 200) {
            console.log(`Статус ответа ${xhr.status}`)
        } else {
            const result = JSON.parse(xhr.response);
            if (callback) {
                callback(result)
            }
        }
    }


    xhr.onprogress = function (event) {
        console.log(`Загружено ${event.loaded} из ${event.total}`)
    };

    xhr.onerror = function () {
        console.log('Ошибка! Статус ответа: ', xhr.status);
    };

    xhr.send();
}

const resultNode = document.querySelector('.j-result');
const btnNode = document.querySelector('.j-btn-request');

function displayResult(apiData) {
    let cards = '';
    apiData.forEach(item => {
        const cardBlock = `
        <div class="card">
        <img src="${item.photo}"
        class="card-image"/>
        <p>${item.user}</p>
        <p>${item.about}</p>

        </div>
        `;
        cards = cards + cardBlock
    });
    console.log(cards)
    resultNode.innerHTML = cards;
}

btnNode.addEventListener('click', () => {
    useRequest('http://127.0.0.1:8000/api/v2/profile/', displayResult);
})