const mobileScreen = window.matchMedia("(max-width: 990px )");
$(document).ready(function () {
    $(".dashboard-nav-dropdown-toggle").click(function () {
        $(this).closest(".dashboard-nav-dropdown")
            .toggleClass("show")
            .find(".dashboard-nav-dropdown")
            .removeClass("show");
        $(this).parent()
            .siblings()
            .removeClass("show");
    });
    $(".menu-toggle").click(function () {
        if (mobileScreen.matches) {
            $(".dashboard-nav").toggleClass("mobile-show");
        } else {
            $(".dashboard").toggleClass("dashboard-compact");
        }
    });
});

// localStorage.setItem('sale_id', JSON.stringify(1900));
// var id = JSON.parse(localStorage.getItem('sale_id'));
// let s_id=document.getElementById("sale_id");
// sid=Number(id);
// console.log(sid.toString())
// s_id.value=sid;
function newBill()
{
localStorage.setItem('name', JSON.stringify(""));
localStorage.setItem('phone_no', JSON.stringify(""));
localStorage.setItem('age', JSON.stringify(""));
}
let s_id=document.getElementById("sale_id");
var id = JSON.parse(localStorage.getItem('sale_id'));
sid=Number(id);
s_id.value=sid;
function newId()
{
    var id = JSON.parse(localStorage.getItem('sale_id'));
    let s_id=document.getElementById("sale_id");
    sid=Number(id)+1;
    console.log(sid.toString())
    s_id.value=sid;
    localStorage.setItem('sale_id', JSON.stringify(sid));
}
function retain()
{
    console.log("1")
    var cname=document.getElementById('cname').value;
    localStorage.setItem('name', JSON.stringify(cname));
    var str=JSON.parse(localStorage.getItem('name'));
    console.log(str)
    var cname1=document.getElementById('cname');
    cname1.value=str;
}

