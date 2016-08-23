var loadeddiv ='quotes'

function getid(div)
{
    return document.getElementById(div);
}

function displaythediv(div)
{
    getid(div).style.display='block';    
}

function hidethediv(div)
{
    getid(div).style.display='none';
}

function loadsauto(div)
{
    hidethediv(div);
    displaythediv(div);
    loadeddiv=div;
}
