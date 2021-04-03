function searchTable(id_table) {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    cards = document.getElementById("grid").getElementsByTagName("div")
    filter = input.value.toUpperCase();
   
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < cards.length; i++) {
      card_name = cards[i].getElementsByTagName("h2")[0];
      if (card_name) {
        txtValue = card_name.textContent || card_name.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          cards[i].style.display = "";
        } else {
          cards[i].style.display = "none";
        }
      }
    }
  }

  function addRowHandlers(url) {
    var grid = document.getElementById("grid");
    var divs = grid.getElementsByTagName("div")
    x = divs[0]
    for (i = 0; i < divs.length; i++) {
        var div = divs[i].children[0].getElementsByTagName("span")[0].innerTex;
        var createClickHandler = 
            function(div) 
            {
                return function() { 
                                        var id = div.getElementsByTagName("span")[0].innerText.replace(/\D/g,"")
                                        window.location.href = url+id;
                                 };
            };

            divs[i].children[0].onclick = createClickHandler(divs[i]);
    }
}

if (window.location.href.includes("dog")){
  console.log("dog list")
  window.onload = addRowHandlers("/controller/dog/");
} else {
  console.log("member list")
  window.onload = addRowHandlers("/controller/member/");
}

console.log("delete input")
document.getElementById("myInput").value = ""