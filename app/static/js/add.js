var id = 0;
function addItem(){
    id++;
    let seq = document.getElementById('seq').value;
    let tax = document.getElementById('tax').value;
    console.log(seq);
    if(seq && tax) {
        document.getElementById('items').insertAdjacentHTML('beforeend', '<tr><td>' + seq + '</td><td>' + tax + '</td></tr>');
        let formData = new FormData();
        formData.append('id', id);
        formData.append('seq', seq);
        formData.append('tax', tax);
        fetch('/addItem', {method: 'POST', body: formData});
    }

}