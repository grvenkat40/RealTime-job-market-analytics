const API_BASE  = "http://127.0.0.1:8000/analytics"

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