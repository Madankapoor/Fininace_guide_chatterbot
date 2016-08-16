	
		 
		 function GetReply(){
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
	  if (xhttp.readyState == 4 && xhttp.status == 200) 
	  {
		var breply=document.createElement("DIV");
		var arequest=document.createElement("DIV");
		var reply=xhttp.responseText ;
		var TextArea=document.getElementById("chat-textarea");
		
		arequest.innerHTML=document.getElementById("message_box").value;
		breply.innerHTML=reply;
		arequest.className="userrequest";
		breply.className="botreply";
		TextArea.appendChild(arequest);
		TextArea.appendChild(breply);
		document.getElementById("message_box").value = ""
		$('#chat-textarea').animate({scrollTop: $('#chat-textarea').get(0).scrollHeight}, 500);
	  }
	 };
	  xhttp.open("POST", "/replyalone", true);
	  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	  xhttp.send("message_box="+document.getElementById("message_box").value);
	}	