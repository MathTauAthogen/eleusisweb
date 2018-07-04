function load(){
	var id = window.prompt("Please enter a game id.");
	$.post("/ajax/id",JSON.stringify({"id":id}),function(resp){if(resp==true){alert("We're not done with this yet.")}else{alert("That is an invalid game id.");load();}});
}