/* 
hotspots.json format:
{
    "State": [
        {
            "suburb": "String", 
            "start_date": "String", 
            "start_time": "String"
        }
    ]
}
*/
$.getJSON("./backend/info_corner/scraper/hotspots.json", function(hotspots) {

    generateAllTables();
    
    function generateAllTables() {
        for (let key of Object.keys(hotspots)) {
            if (key != "Last updated") {
                generateStateTable(hotspots[key], key);
            }
        }

        let hotspots_div = document.getElementById("hotspots_container");
        let update_div = document.getElementById("Last updated");
        let update_msg = document.createElement("p");
        update_msg.innerHTML = `Last updated at ${hotspots["Last updated"]} from `;

        let url = document.createElement("a");
        url.href = "https://www.qld.gov.au/health/conditions/health-alerts/coronavirus-covid-19/current-status/hotspots-covid-19";
        let url_text = document.createTextNode("https://www.qld.gov.au/health/conditions/health-alerts/coronavirus-covid-19/current-status/hotspots-covid-19");
        url.appendChild(url_text);
        
        update_msg.appendChild(url);

        update_div.appendChild(update_msg);

        hotspots_div.appendChild(update_div);
    }
    
    function generateStateTable(state_dict, state_id) {
        let div_container = document.getElementById(state_id);
    
        if (state_dict.length == 0) {
            let message = document.createElement("p");
            message.innerHTML = "No current declared hotspots.";
            div_container.appendChild(message);
    
        } else {
            // generate table
            let table = document.createElement("table");
            
            // create table head
            let t_head = document.createElement("thead");
    
            // create row for head
            let h_row = document.createElement("tr");
    
            // add column headings to row of table head
            let headings = ["Suburb", "Date Declared", "Time Declared"]
            for (let i = 0; i < 3; i++) {
                let th = document.createElement("th");
                th.innerHTML = headings[i];
                h_row.appendChild(th);
            }
            t_head.appendChild(h_row);
            table.appendChild(t_head);
    
            // table body
            let t_body = document.createElement("tbody");
            for (i = 0; i < state_dict.length; i++) {
                let b_row = document.createElement("tr");
    
                let suburb = document.createElement("td");
                suburb.innerHTML = state_dict[i]["suburb"];
                b_row.appendChild(suburb);
    
                let date = document.createElement("td");
                date.innerHTML = state_dict[i]["start_date"];
                b_row.appendChild(date);
    
                let time = document.createElement("td");
                time.innerHTML = state_dict[i]["start_time"];
                b_row.appendChild(time);
    
                t_body.appendChild(b_row);
            }
            table.appendChild(t_body);
    
            // Add table to the div container
            div_container.appendChild(table);
        }
    }

});