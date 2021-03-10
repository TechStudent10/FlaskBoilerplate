async function SetFlask(element, endpoint, method='GET', body=null, headers={}) {
    const requestOptions = {
        method: method,
        headers: headers
    }
    if (body !== null) {
        requestOptions['body'] = JSON.stringify(body);
    }
    let result = null;
    const request = await fetch(endpoint, requestOptions).then(res => res.json()).then(data => {
        result = data.result;
    });
    element.innerHTML += `<p>${result}</p>`;
}