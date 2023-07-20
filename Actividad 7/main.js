let textInputCount = 0;

function addTextInput() {
    textInputCount++;
    const container = document.getElementById('text-input-container');
    const textarea = document.createElement('textarea');
    textarea.id = 'text-input-' + textInputCount;
    textarea.className = 'form-control mb-3';
    textarea.rows = '4';
    textarea.cols = '50';
    textarea.placeholder = 'Escribe el texto aquí...';
    container.appendChild(textarea);
}

function analyzeText() {
    const textInputs = [];
    for (let i = 1; i <= textInputCount; i++) {
        const textInput = document.getElementById('text-input-' + i).value;
        textInputs.push(textInput);
    }

    fetch('http://localhost:8000/analyze/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(textInputs)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const resultElement = document.getElementById('result');
        resultElement.innerHTML = generateTable(data);
    })
    .catch(e => {
        console.log('There was a problem with the fetch operation: ' + e.message);
    });
}

function generateTable(data) {
    let html = '<h3>Analisis de texto</h3>';
    html += generateTableFromData(data['Analisis de texto']);
    html += '<h3 class="mt-4">Eaggles</h3>';
    html += generateTableFromData(data['Eaggles']);
    return html;
}

function generateTableFromData(data) {
    let html = '<table class="table table-striped">';
    // añadir encabezados
    html += '<thead><tr>';
    for (let key in data[0]) {
        html += `<th>${key}</th>`;
    }
    html += '</tr></thead>';
    // añadir datos
    html += '<tbody>';
    for (let row of data) {
        html += '<tr>';
        for (let key in row) {
            html += `<td>${row[key]}</td>`;
        }
        html += '</tr>';
    }
    html += '</tbody></table>';
    return html;
}

window.onload = addTextInput;
