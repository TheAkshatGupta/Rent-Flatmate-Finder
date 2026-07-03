const user = JSON.parse(localStorage.getItem("user"));

if (!user) {

    window.location.href = "login.html";

}

document.getElementById("welcome").innerHTML =
    "Welcome, " + user.full_name;

async function loadListings() {

    const response = await fetch(
        "http://127.0.0.1:5000/listings"
    );

    const listings = await response.json();

    const container =
        document.getElementById("listingContainer");

    container.innerHTML = "";

    listings.forEach(listing => {

        container.innerHTML += `

        <div class="col-md-4 mb-3">

            <div class="card shadow">

                <div class="card-body">

                    <h5>${listing.title}</h5>

                    <p>${listing.description}</p>

                    <h6>₹ ${listing.rent}</h6>

                    <p>${listing.city}</p>

                    <button
                        class="btn btn-primary"
                        onclick="viewCompatibility(${listing.id})">

                        AI Compatibility

                    </button>

                </div>

            </div>

        </div>

        `;

    });

}

async function viewCompatibility(id){

    const response = await fetch(

        `http://127.0.0.1:5000/compatibility/${user.id}/${id}`

    );

    
    const data = await response.json();
    console.log(data);

    alert(

        "Compatibility Score : "

        + data.score +

        "\n\n"

        + data.explanation

    );

}

function logout(){

    localStorage.clear();

    window.location.href="login.html";

}

loadListings();