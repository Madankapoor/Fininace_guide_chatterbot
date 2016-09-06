var date = new Date();
document.getElementById('clear-button').onclick=chatclear
function getTime()
{
	var hours = date.getHours();
    var hours = hours; 
    var mid='am';
    if(hours==0){ //At 00 hours we need to show 12 am
    hours=12;
    }
    else if(hours>12)
    {
    hours=hours-12;
    mid='pm';
    }
    var str =  hours + ":" + date.getMinutes() + " "+mid+"  " +date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear() ;
    return str;
}
 function GetReply(){
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
	  if (xhttp.readyState == 4 && xhttp.status == 200) 
	  {
		var breply=document.createElement("DIV");
		var arequest=document.createElement("DIV");
		var reply=xhttp.responseText ;
		var TextArea=document.getElementById("chat-textarea");
		arequest.innerHTML="<div class='userrequest'>"+document.getElementById("message_box").value+"</div><br><sub>"+getTime()+"</sub>";
		breply.innerHTML="<div class='botreply'>"+reply+"</div><br><sub>"+getTime()+"</sub>";
		arequest.className="messageuser";
		breply.className="messagebot";
		TextArea.appendChild(arequest);
		TextArea.appendChild(breply);
		document.getElementById("message_box").value = ""
		$('#chat-textarea').animate({scrollTop: $('#chat-textarea').get(0).scrollHeight}, 500);
	  }
	 };
	  xhttp.open("POST", "/reply", true);
	  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	  xhttp.send("message_box="+document.getElementById("message_box").value);
	}	
	
	function chatclear()
	{
		document.getElementById("chat-textarea").innerHTML="";
	}