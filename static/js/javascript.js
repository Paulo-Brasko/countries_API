// Global Variables
var countriesListDropDown;
var counter = 0;

function setup() {
    getAllCountriesButton = document.getElementById("getAllCountries");
    getAllCountriesButton.addEventListener("click", fetchListOfCountries);
}

function fetchListOfCountries() {
    fetch("https://restcountries.com/v3.1/all")
        .then(res => res.json())
        .then(data => {
            // for (let i = 0; i < data.length; i++) {
                fetch("http://127.0.0.1:5000/addCountryToDatabase", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data[counter])
                })
                    // .then(response => response.json())
                    .then(data => {
                        console.log('Success:', data);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });

                    counter = counter + 1;
           // }
        })
        .catch(err => console.log("Error:", err));
}

function initializeDropDown(listOfCountries) {
    let options = "";
    for (let i = 0; i < listOfCountries.length; i++) {
        options += `<option value="${listOfCountries[i]}">${listOfCountries[i]}</option>`;
    }
    countriesListDropDown.innerHTML = options;
    countriesListDropDown.selectedIndex = Math.floor(Math.random() * listOfCountries.length);
    displayCountryInfo(countriesListDropDown[countriesListDropDown.selectedIndex].value);
}
function newCountrySelection(event) {
    displayCountryInfo(event.target.value);
}
function displayCountryInfo(countryName) {
    let url = `https://restcountries.com/v3.1/name/${countryName}`;
    fetch(url)
        .then(res => res.json())
        .then(data => {
            countryData = data[0];
            document.getElementById("flag-container").src = countryData.flags["png"];
            document.getElementById("flag-container").alt = `Flag of ${countryData.name}`;
            document.getElementById("capital").innerHTML = countryData.capital;
            document.getElementById("population").innerHTML = countryData.population.toLocaleString("en-US");
            let key = Object.keys(countryData.currencies)[0];
            let currencyName = countryData.currencies[key].name;
            let currencySymbol = countryData.currencies[key].symbol;
            document.getElementById("currencies").innerHTML = `${currencyName} - ${currencySymbol}`;
            document.getElementById("region").innerHTML = countryData.region;
            document.getElementById("subregion").innerHTML = countryData.subregion;
            document.getElementById("googleMap").href = countryData.maps["googleMaps"];
        })
        .catch(err => console.log("Error:", err));
}

window.addEventListener('load', setup);