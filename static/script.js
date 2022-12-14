function getCookie(cname) {
	let name = cname + "=";
	let decodedCookie = decodeURIComponent(document.cookie);
	let ca = decodedCookie.split(';');
	for(let i = 0; i <ca.length; i++) {
	let c = ca[i];
	while (c.charAt(0) == ' ') {
			c = c.substring(1);
	}
	if (c.indexOf(name) == 0) {
	  return c.substring(name.length, c.length);
		}
	}
	return "";
}

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	let expires = "expires="+ d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


var token = getCookie("token")
if (token && token != "None") {
	let xhr = new XMLHttpRequest();
	let url = "/auth/check";
	xhr.open("GET", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.setRequestHeader("token", token);
	xhr.send(JSON.stringify())
	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4) {
			if (xhr.status === 200) {
				var butt = document.getElementById('login-button')
				butt.innerHTML = parseJwt(token).username
				butt.setAttribute('href', "/web/profile")
				butt = document.getElementById('register-button')
				butt.innerHTML = "Выйти"
				butt.setAttribute('href', "#")
				butt.setAttribute('onclick', 'exit()')
			}
		}
	}
}

function exit() {
	alert("exit")
	// document.cookie = "token=None;"
	// window.location = "/web"
}
