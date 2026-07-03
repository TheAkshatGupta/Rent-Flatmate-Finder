const form = document.getElementById("registerForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const body = {

        full_name: full_name.value,

        email: email.value,

        phone: phone.value,

        password: password.value,

        role: role.value

    };

    const response = await fetch("http://127.0.0.1:5000/register", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(body)

    });

    const data = await response.json();

    alert(data.message);

    if (response.ok) {

        window.location.href = "login.html";

    }

});