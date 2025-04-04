
setInterval(() => {
    fetch("/data/update")
    .then(response => response.json())
    .then(data => {
        const temp = data.cpu_temp;
        const max_temp = 45;
        const deg = temp * 270 / max_temp - 30;
        document.querySelector(".gauge .pointer .hand").style.transform = `rotate(${deg}deg)`;
    })
    
}, 200);
