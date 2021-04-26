var create_btn=document.getElementById('create');
create_btn.onclick = () =>{
    var disp=document.getElementById('edit');
    disp.style.display="block";
    var records=document.getElementById('rec');
    records.style.display="none";
    var dashboard=document.getElementById('dashboard');
    dashboard.style.display="none";
}

var rec_btn=document.getElementById('show');
rec_btn.onclick = () =>{
    var show=document.getElementById('rec');
    show.style.display="block";
    var ed=document.getElementById('edit');
    ed.style.display="none";
    var dashboard=document.getElementById('dashboard');
    dashboard.style.display="none";
}
var dash_btn=document.getElementById('dash_btn');
dash_btn.onclick = () =>{
    var dashboard=document.getElementById('dashboard');
    dashboard.style.display="block";
    var ed=document.getElementById('edit');
    ed.style.display="none";
    var records=document.getElementById('rec');
    records.style.display="none";
}