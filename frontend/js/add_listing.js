const form=document.getElementById("listingForm");

form.addEventListener("submit",async(e)=>{

e.preventDefault();

const body={

title:title.value,

description:description.value,

rent:Number(rent.value),

city:city.value,

area:area.value,

property_type:property_type.value,

owner_name:owner_name.value,

owner_phone:owner_phone.value

};

const response=await fetch("http://127.0.0.1:5000/listings",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(body)

});

const data=await response.json();

alert(data.message);

if(response.ok){

window.location.href="dashboard.html";

}

});