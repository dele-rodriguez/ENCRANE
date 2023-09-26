const q_num = document.querySelectorAll("span.q-num")
const toggle_btn = document.querySelectorAll(".buttons")
const toggle_btn_btn = document.querySelectorAll(".buttons button")
for(let i = 0; i<q_num.length; i++){
  q_num[i].innerText = i + 1 + ". "
}

for(let i = 0; i < toggle_btn.length; i++){
  toggle_btn[i].addEventListener("click", function(){
    let answer =  toggle_btn[i].nextElementSibling
    if(answer.style.display == "flex"){
      answer.style.display = "none"
      toggle_btn_btn[i].innerText = "Show Answer"
    }else{
      answer.style.display = "flex"
      toggle_btn_btn[i].innerText = "Hide Answer"
    }
  })
}
