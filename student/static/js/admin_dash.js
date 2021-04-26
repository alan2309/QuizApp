

var rec_btn=document.getElementById('show');
rec_btn.onclick = () =>{
    var show=document.getElementById('rec');
    show.style.display="block";
 
    var dashboard=document.getElementById('dashboard');
    dashboard.style.display="none";
}
var dash_btn=document.getElementById('dash_btn');
dash_btn.onclick = () =>{
    var dashboard=document.getElementById('dashboard');
    dashboard.style.display="block";
    
    var records=document.getElementById('rec');
    records.style.display="none";
}