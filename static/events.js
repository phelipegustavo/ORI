function inputCheck(){
	var inputSearch = document.querySelector(".search-input");
	var buttonPrimary = document.querySelector(".primary");
	var spanAlert= document.querySelector(".alertInput");
	console.log("Texto: " + inputSearch.value.toString().length);
	if(inputSearch.value.toString().length < 1){
		event.preventDefault();
		spanAlert.classList.add("alertInput-active"); 	
	}
	else{
		spanAlert.classList.remove(".alertInput-active") ; 	
	}
}

