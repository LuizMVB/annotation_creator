var id = 0;
function addItem(){
    id++;
    let seq = document.getElementById('seq').value;
    let tax = document.getElementById('tax').value;
    if(seq && tax) {
        document.getElementById('items').insertAdjacentHTML('beforeend', '<tr><td>' + seq + '</td><td>' + tax + '</td></tr>');
        fetch('/addItem/' + id + '/' + seq + '/' + tax);
    }

}