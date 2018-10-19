function reactingSubmitButton(){
    var message =  document.getElementById("say").value;
    console.log(message);
    if (message === ""){
         document.getElementById("send").value = "Send Quiet Hugg"; 
    }
    else if (message === "Hello there"){
        document.getElementById("send").value = "General Kenobi"; 
    }
    else if (message === "Somebody"){
        document.getElementById("send").value = "Once told me"; 
    }
    else{
        document.getElementById("send").value = "Send Hugg";
    }
}