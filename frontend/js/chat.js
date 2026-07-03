const user = JSON.parse(localStorage.getItem("user"));

if(!user){

window.location.href="login.html";

}

const form=document.getElementById("chatForm");

async function loadMessages(){

const response=await fetch("http://127.0.0.1:5000/chat");

const data=await response.json();

const box=document.getElementById("messages");

box.innerHTML="";

data.forEach(msg=>{

box.innerHTML+=`

<p>

<b>${msg.sender_id}</b>

:

${msg.message}

</p>

`;

});

}

loadMessages();

form.addEventListener("submit",async(e)=>{

e.preventDefault();

const response=await fetch("http://127.0.0.1:5000/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

sender_id:user.id,

receiver_id:1,

message:message.value

})

});

const data=await response.json();

alert(data.message);

message.value="";

loadMessages();

});