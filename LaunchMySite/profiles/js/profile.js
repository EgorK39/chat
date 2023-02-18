function useRequest(url) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);

    xhr.onload = function () {
        if (xhr.status !== 200) {
            console.log(`Статус ответа ${xhr.status}`)
        } else {
            const result = JSON.parse(xhr.response);
            console.log(result)
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


document.addEventListener("DOMContentLoaded", () => {
    useRequest('http://127.0.0.1:8000/api/v2/profiles/');
})