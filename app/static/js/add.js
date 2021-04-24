var table = [];

function addItem(){
    let seq = document.getElementById('seq').value;
    let tax = document.getElementById('tax').value;
    if(seq && tax) {
        table.push({seq : seq, tax : tax});
        document.getElementById('items').insertAdjacentHTML("beforeend", "<tr><td>" + seq + "</td><td>" + tax + "</td></tr>");
    }
}