const employees = Array.from(document.querySelectorAll('.employee_info'));
const popUp = document.querySelector('#popUp div.card');
// console.log(popUp);

function showEmployeeInfo(event){
    // event.stopPropagation();
    // event.preventDefault();
    // let host = window.location.host;
    let req = new XMLHttpRequest();

    req.open('GET', event.currentTarget.href, false);
    req.send();
    // var headers = req.getAllResponseHeaders().toLowerCase();
    
    console.log(req.getAllResponseHeaders());
}

// employees.forEach(employee => {
//     employee.addEventListener("click", showEmployeeInfo)
// })
