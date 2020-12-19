function decir(texto){
  document.getElementById('hablar').addEventListener("click",()=>{
    decir(document.getElementById("texto").value);
 });
 document.getElementById('hablar2').addEventListener("click",()=>{
    decir(document.getElementById("texto2").value);
 });
       speechSynthesis.speak(new SpeechSynthesisUtterance(texto));
}