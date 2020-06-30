function contact() {
    document.getElementById("home-page").style.display = "none";
    document.getElementById("contact").style.display = "block";
    document.getElementById("jobs").style.display = "none";
    document.getElementById("login-form").style.display = "none";
    document.getElementById("sign-form").style.display = "none";
    
}
function homepage(){
    document.getElementById("home-page").style.display = "block";
    document.getElementById("contact").style.display = "none";
    document.getElementById("jobs").style.display = "none";
    document.getElementById("login-form").style.display = "none";
    document.getElementById("sign-form").style.display = "none";
}
function jobs(){
    document.getElementById("jobs").style.display = "block";
    document.getElementById("contact").style.display = "none";
    document.getElementById("home-page").style.display = "none";
    document.getElementById("login-form").style.display = "none";
    document.getElementById("sign-form").style.display = "none";
}
function login(){
    document.getElementById("jobs").style.display = "none";
    document.getElementById("contact").style.display = "none";
    document.getElementById("home-page").style.display = "none";
    document.getElementById("login-form").style.display = "block";
    document.getElementById("sign-form").style.display = "none";
}
function signup(){
    document.getElementById("jobs").style.display = "none";
    document.getElementById("contact").style.display = "none";
    document.getElementById("home-page").style.display = "none";
    document.getElementById("login-form").style.display = "none";
    document.getElementById("sign-form").style.display = "block";
}