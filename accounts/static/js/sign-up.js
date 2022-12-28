//let country = document.getElementById("country")

// get the data of the countries
document.addEventListener("DOMContentLoaded", () =>{
    fetch("https://restcountries.com/v3.1/all")
    .then(response => response.json())
    // .then(data => {
    //     let output = `<option>select a country</option>`
    //     let arr = []
    //     let i = 0
    //     data.forEach(country => {
            
    //         arr.push(country.name.common)
    //     })
    //     arr.sort()
    //     arr.forEach(country => {
    //         output += `<option>${country}</option>`
    //     })
    //     country.innerHTML = output
    // })
})