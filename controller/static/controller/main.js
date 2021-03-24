function addRowHandlers() {
    var grid = document.getElementById("grid");
    var divs = divs.getElementsByTagName("div")
    for (i = 0; i < divs.length; i++) {
        var div = divs[i].children[0].getElementsByTagName("span")[0].innerTex;
        var createClickHandler = 
            function(div) 
            {
                return function() { 
                                        var id = div.getElementsByTagName("span")[0].innerText.replace(/\D/g,"")
                                        window.location.href = "/controller/member/"+id;
                                 };
            };

        currentRow.onclick = createClickHandler(div);
    }
}

window.onload = addRowHandlers(div);

