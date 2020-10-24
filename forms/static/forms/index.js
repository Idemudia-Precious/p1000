document.addEventListener('DOMContentLoaded', function(){
  document.querySelector('.mathematics').addEventListener('click', () => load_mathematics());
  document.querySelector('.english').addEventListener('click', () => load_english());
  document.querySelector('.quantitative').addEventListener('click', () => load_quantitative());
  document.querySelector('.verbal').addEventListener('click', () => load_verbal());

  load_mathematics();
  countdown(0, 59, 59);
});

function countdown(hr, mm, ss) {
  var interval = setInterval(function () {
    if(hr == 0 && mm == 0 && ss == 0)clearInterval(interval);
    ss--;
    if(ss == 0){
      ss = 59;
      mm--;
      if(mm == 0){
        mm = 59;
        hr --;
      }
    }
    if(hr.toString().length < 2) hr = "0"+hr;
    if(mm.toString().length < 2) mm = "0"+mm;
    if(ss.toString().length < 2) ss = "0"+ss;
    $("#timer").html(hr+" : "+mm+" : "+ss);
    //document.querySelector("#timer").innerHTML = `hr+" : "+mm+" : "+ss`
  }, 1000);
}

function load_mathematics() {
  document.querySelector('.mathematics2').style.display='block';
  document.querySelector('.verbal2').style.display='none';
  document.querySelector('.quantitative2').style.display='none';
  document.querySelector('.english2').style.display='none';
}
function load_english() {
  document.querySelector('.mathematics2').style.display='none';
  document.querySelector('.verbal2').style.display='none';
  document.querySelector('.quantitative2').style.display='none';
  document.querySelector('.english2').style.display='block';
}
function load_quantitative() {
  document.querySelector('.mathematics2').style.display='none';
  document.querySelector('.verbal2').style.display='none';
  document.querySelector('.quantitative2').style.display='block';
  document.querySelector('.english2').style.display='none';
}
function load_verbal() {
  document.querySelector('.mathematics2').style.display='none';
  document.querySelector('.verbal2').style.display='block';
  document.querySelector('.quantitative2').style.display='none';
  document.querySelector('.english2').style.display='none';
}
