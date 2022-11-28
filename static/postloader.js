let xhr = new XMLHttpRequest();
let url = "/post"
xhr.open("GET", url, true)
xhr.send(JSON.stringify())
xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
		post = document.getElementById('protopost')
		response = JSON.parse(this.response)
		for (let key in response) {
			// alert(response[key]["text"])
			post.getElementById("post-title") = response[key]["text"]
			post.querySelector('post-text').innerHTML = response[key]["text"]
		}
	}
}
