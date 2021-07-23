function create_grid(){
	var rows = [];
	var colStr = null;
	for(var j = 0; j <= 10; j++) {
		  colStr = "";
		  var characters = 'ABCDEFGHIJKLMNOPQRSTUVXYZ';
		  for (var i = 0; i <= 10; i++){
			  var random = parseInt(Math.random()*characters.length);
			  var letter = characters.charAt(random); //returning random letter
			  var cell = '<td>' + letter + '</td>';
			  colStr += cell;
		  };
		  rows.push('<tr>' + colStr + '</tr>');
	}

	document.getElementById('wsBox').innerHTML += rows.join("");
}
