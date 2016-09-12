var detailsAdded=""; 
var categorySelected=1;
var filtern = 1;

function add(){
    if(document.getElementById("dead").checked)
        categorySelected = 1;
    else if(document.getElementById("injured").checked)
        categorySelected = 2;
    else if(document.getElementById("haven").checked)
        categorySelected = 3;
    else if(document.getElementById("firstAid").checked)
        categorySelected = 4;
    
    if(document.getElementById("textarea1").value.length < 32)
    {
    detailsAdded = document.getElementById("textarea1").value;
    
    document.getElementById("saveWaypoints").click();}
    else {window.alert("بیش از حد مجاز");
    document.getElementById("textarea1").value = "";
    }
};

  $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
  });
  
function filter(n)
{
  if(n==1)
  {
      filtern = 1;
      initialize();
  }  
  else if(n==2)
  {
      filtern = 2;
      initialize();
  }
  else if(n==3)
  {
      filtern = 3;
      initialize();
  }    
  else if(n==4)
  {
      filtern = 4;
      initialize();
  }  
};