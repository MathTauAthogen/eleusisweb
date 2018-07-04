function load(){
	var id = window.prompt("Please enter a game id.");
	$.post("/ajax/id",JSON.stringify({"id":id}),function(resp){if(JSON.parse(resp)['valid']=='true'){window.alert("We're not done with this yet.");login();}else if(JSON.parse(resp)['valid']=='false'){window.alert("That is an invalid game id.");load();}});
}
function login(){
	var username = window.prompt("Please enter a/your username.");
	$.post("/ajax/user",JSON.stringify({"name":name}),function(resp){if(JSON.parse(resp)['valid']=='true'){pass();}else if(JSON.parse(resp)['valid']=='false'){pass2();}});
}
function pass(){
	var password = window.prompt("Please enter your password.");
	$.post("/ajax/pass",JSON.stringify({"pass":password}), )
}

function pass2(){
	var password = window.prompt("Please enter a password.");
	$.post("/ajax/user",JSON.stringify({"name":name}))
}