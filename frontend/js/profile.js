const user = JSON.parse(localStorage.getItem("user"));

if (!user) {
    window.location.href = "login.html";
}

const form = document.getElementById("profileForm");

let profileExists = false;

// Load profile if it already exists
async function loadProfile() {

    const response = await fetch(
        `http://127.0.0.1:5000/profile/${user.id}`
    );

    if (response.ok) {

        const profile = await response.json();

        profileExists = true;

        age.value = profile.age;
        gender.value = profile.gender;
        occupation.value = profile.occupation;
        budget.value = profile.budget;
        food_preference.value = profile.food_preference;
        smoking.value = profile.smoking;
        drinking.value = profile.drinking;
        pets.value = profile.pets;
        sleep_schedule.value = profile.sleep_schedule;
        cleanliness.value = profile.cleanliness;
        languages.value = profile.languages;
        bio.value = profile.bio || "";

        document.querySelector("button").innerText = "Update Profile";
    }

}

loadProfile();

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    const body = {

        user_id: user.id,
        age: Number(age.value),
        gender: gender.value,
        occupation: occupation.value,
        budget: Number(budget.value),
        food_preference: food_preference.value,
        smoking: smoking.value,
        drinking: drinking.value,
        pets: pets.value,
        sleep_schedule: sleep_schedule.value,
        cleanliness: cleanliness.value,
        languages: languages.value,
        bio: bio.value

    };

    const url = profileExists
        ? `http://127.0.0.1:5000/profile/${user.id}`
        : "http://127.0.0.1:5000/profile";

    const method = profileExists ? "PUT" : "POST";

    const response = await fetch(url, {

        method: method,

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(body)

    });

    const data = await response.json();

    alert(data.message);

    if (response.ok) {
        window.location.href = "dashboard.html";
    }

});