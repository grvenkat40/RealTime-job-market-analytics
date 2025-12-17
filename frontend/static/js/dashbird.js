const jobform = document.getElementById("jobform");
const statusdiv = document.getElementById("status");

const API_BASE = "https://realtime-job-market-analytics.onrender.com";

jobform.addEventListener("submit", function(event){
    event.preventDefault();

    const roleInput = document.getElementById("role").value;
    const cityInput = document.getElementById("city").value;

    if(!roleInput){
        statusdiv.textContent = "Please enter a job role.";
        return;
    }
    // --- Send Data to Backend ---
    triggerScrape(roleInput, cityInput);
});

// Function to handle the actual API communication
function triggerScrape(role, city){
    // const  TEST_BASE = "https://realtime-job-market-analytics.onrender.com";
    const SCRAPE_URL = `${API_BASE}/scrape`;
    statusdiv.textContent = "Searching for jobs... Please wait.";

    fetch(SCRAPE_URL,{
        method:"POST",
        headers : {
            "Content-Type":"application/json"
        },
        body : JSON.stringify({
            role:role,
            city:city
        })
    })
    .then(response =>{
        if(!response.ok){
            throw new Error(`Server responded with status : ${response.status}`);
        }
        return response.json();
    })
    .then(data =>{
        statusdiv.textContent = "Scraping in progress… updating dashboard shortly.";
        setTimeout(refreshCharts, 10000);
    })
    .catch(error =>{
        statusdiv.textContent = `Error during search: ${error.message}`;
        console.error("Fetch error", error);
    });
}

function refreshCharts(){
    loadLocationCharts();
    loadCompanyCharts();
    loadSkillsCharts()
    statusdiv.textContent = "Dashboard updated with latest data.";
}

// const API_BASE  = "https://realtime-job-market-analytics.onrender.com/analytics"

function loadLocationCharts(){
    fetch(`${API_BASE}/locations`)
        .then(res => res.json())
        .then(data => {
            new Chart(document.getElementById("locationChart"),{
                type:'bar',
                data:{
                    labels:data.map(d => d.location),
                    datasets:[{
                        data:data.map(d => d.count)
                    }]
                }
        });
        });
    }

function loadCompanyCharts(){
    fetch(`${API_BASE}/companies`)
        .then(res => res.json())
        .then(data => {
            new Chart(document.getElementById('companyChart'), {
                type :'bar',
                data:{
                    labels : data.map(d => d.company),
                    datasets:[{
                        data:data.map(d => d.count)
                    }]
                }
            });
        });
}

function loadSkillsCharts(){
    fetch(`${API_BASE}/skills`)
        .then(res => res.json())
        .then(data => {
            new Chart(document.getElementById("skillChart"), {
                type:'bar',
                data:{
                    labels:data.map(d => d.skills),
                    datasets:[{
                        data : data.map(d => d.count)
                    }]
                }
            });
        });
}

refreshCharts()

const themetoggle = document.getElementById("toggleTheme");
if(localStorage.getItem("theme") === "dark"){
    document.body.classList.add("dark");
    themetoggle.textContent="☀️";
}
themetoggle.addEventListener("click", ()=>{
    document.body.classList.toggle("dark");
    const isDark = document.body.classList.contains("dark");
    themetoggle.textContent = isDark ? "☀️" : "🌙";
    localStorage.setItem("theme",isDark ? "dark" : "light");
});
