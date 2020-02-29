/**
 * VUE JS example usage
 * import feeapi from 'feeapi';
 * Object.defineProperty(Vue.prototype, '$feeapi', { value: feeapi });
 * usage:
 * this.$feeapi.method();
 **/
const axios = require('axios');
const HTTP = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/'
});

function rawHttp(url, method, params, onSuccess, onError) {
  if (method === 'POST') {
    HTTP.post(url, params).then(function (response) {
      onSuccess(response.data);
    }).catch(function (e) {
      onError(e);
    })
  } else if (method === "GET") {
    HTTP.get(url, params).then(function (response) {
      onSuccess(response.data);
    }).catch(function (e) {
      onError(e);
    })
  } else if (method === "PUT") {
    HTTP.put(url, params).then(function (response) {
      onSuccess(response.data);
    }).catch(function (e) {
      onError(e);
    })
  }
}

feeapi = {
  feedback: {
    /**
     * return all data about new item
     * @param text Инфа об отзыве
     * @param onSuccess функция которая будет вызванная при успешном запросе
     * @param onError функция которая будет вызванная при не успешном запросе
     */
    add: function (text, onSuccess = null, onError = null) {
      rawHttp('feedback/', 'POST', {'text': text, 'rate': 0, 'status': 0}, onSuccess, onError);
    },
    /**
     * вернёт отзыв по id
     * @param id отзыва
     * @param onSuccess функция которая будет вызванная при успешном запросе
     * @param onError функция которая будет вызванная при не успешном запросе
     */
    getById: function (id, onSuccess = null, onError = null) {
      rawHttp(`feedback/${id}/`, 'GET', {}, onSuccess, onError);
    },
    /**
     * вернёт отзыв по id
     * @param status статус отзыва:
     * (0 - Не прочитано)
     * (1 - Принятно)
     * (2 - Отклонено)
     * @param onSuccess функция которая будет вызванная при успешном запросе
     * @param onError функция которая будет вызванная при не успешном запросе
     */
    filterByStatus: function (status, onSuccess = null, onError = null) {
      rawHttp(`feedback/`, 'GET', {'status': status}, onSuccess, onError);
    },
    /**
     * Вернёт все записи в БД
     * @param onSuccess функция которая будет вызванная при успешном запросе
     * @param onError функция которая будет вызванная при не успешном запросе
     */
    all: function (onSuccess = null, onError = null) {
      rawHttp(`feedback/`, 'GET', {}, onSuccess, onError);
    },
    /**
     * Обновляет статус отзыва
     * @param id отзыва
     * @param status новый статус отзыва
     * (0 - Не прочитано)
     * (1 - Принятно)
     * (2 - Отклонено)
     * @param onSuccess функция которая будет вызванная при успешном запросе
     * @param onError функция которая будет вызванная при не успешном запросе
     */
    changeStatus: function (id, status, onSuccess = null, onError = null) {
      rawHttp(`feedback/${id}/`, 'PUT', {'status': status}, onSuccess, onError);
    }
  }
};

// feeapi.feedback.add('test', (r) => console.log(r), (e) => console.log(e));
feeapi.feedback.getById(2, (r) => console.log(r), (e) => console.log(e));
// feeapi.feedback.filterByStatus(0, (r) => console.log(r), (e) => console.log(e));
// feeapi.feedback.all((r) => console.log(r), (e) => console.log(e));
// feeapi.feedback.changeStatus(1, 2, (r) => console.log(r), (e) => console.log(e));

