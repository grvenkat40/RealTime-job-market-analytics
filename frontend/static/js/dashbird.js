const jobform = document.getElementById("jobform");
const statusdiv = document.getElementById("status");

const API_BASE = "https://realtime-job-market-analytics.onrender.com";

jobform.addEventListener("submit", function(event){
    event.preventDefault();

    const role = document.getElementById("role").value;
    const city = document.getElementById("city").value;

    if(!role){
        statusdiv.textContent = "Please enter a job role.";
        return;
    }
    // --- Send Data to Backend ---
    triggerScrape(role, city);
});
document.querySelectorAll(".preset").forEach(btn =>{
    btn.addEventListener("click", ()=>{
        const role = btn.dataset.role;
        const city = btn.dataset.city;

        document.getElementById("role").value = role;
        document.getElementById("city").value = city;
        triggerScrape(role, city);
    });
});

// Function to handle the actual API communication
function triggerScrape(role, city){
    // const  TEST_BASE = "https://realtime-job-market-analytics.onrender.com";
    const SCRAPE_URL = `${API_BASE}/scrape`;
    statusdiv.textContent = "Searching for jobs... Please wait.";

    const API_KEY = "venkat2040gr@2005";

    fetch(SCRAPE_URL,{
        method:"POST",
        headers : {
            "Content-Type":"application/json",
            "X_API_KEY":API_KEY
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

let = locationChartInstance = null;
let = companyChartInstance = null;
let = skillsChartInstance = null;

function refreshCharts(){
    loadLocationCharts();
    loadCompanyCharts();
    loadSkillsCharts()
    statusdiv.textContent = "Dashboard updated with latest data.";
}

// const API_BASE  = "https://realtime-job-market-analytics.onrender.com/analytics"

function loadLocationCharts(){
    fetch(`${API_BASE}/analytics/locations`)
        .then(res => res.json())
        .then(data => {
            if(locationChartInstance){
                locationChartInstance.destroy();
            }
            locationChartInstance = new Chart(document.getElementById("locationChart"),{
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
    fetch(`${API_BASE}/analytics/companies`)
        .then(res => res.json())
        .then(data => {
            if(companyChartInstance){
                companyChartInstance.destroy();
            }
            companyChartInstance = new Chart(document.getElementById('companyChart'), {
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
    fetch(`${API_BASE}/analytics/skills`)
        .then(res => res.json())
        .then(data => {
            if(skillsChartInstance){
                skillsChartInstance.destroy();
            }
            skillsChartInstance = new Chart(document.getElementById("skillChart"), {
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
