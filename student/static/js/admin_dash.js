var create_btn=document.getElementById('create');
var result_btn=document.getElementById('show');

create_btn.onclick=()=>{
    let x=document.getElementById('edit');
    x.style.display="none";
    let y=document.getElementById('edit');
    y.style.display="block";
}
result_btn.onclick=()=>{
    let x=document.getElementById('edit');
    x.style.display="none";
    let y=document.getElementById('rec');
    y.style.display="block";
}