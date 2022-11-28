function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	let expires = "expires="+ d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function form_submitted() {
	const json = {
		username: document.getElementById('username-field').value,
		password: document.getElementById('password-field').value
	}
	let xhr = new XMLHttpRequest()
	let url = "/auth/register"
	xhr.open("POST", url, true)
	xhr.setRequestHeader("Content-Type", "application/json")
	xhr.send(JSON.stringify(json))
	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4) {
			switch (xhr.status){
				case 200 :
					response = JSON.parse(this.response)
					if (response.hasOwnProperty("token")) {
						setCookie("token", response["token"], 30)
						document.getElementById("message-box").innerHTML = "Вы зарегистрировались"
						setTimeout(function(){
							window.location = "/web"
						},1000)
					} else {
						document.getElementById("message-box").innerHTML = "Регистрация не удалась, попробуйте еще раз"
					}
				break
				case 403 :
					document.getElementById("message-box").innerHTML = "Данный юзернейм уже занят"
				break
				default :
					document.getElementById("message-box").innerHTML = "Регистрация не удалась, попробуйте еще раз"
			}
		}
	}
}
