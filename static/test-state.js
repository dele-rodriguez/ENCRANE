const mode = document.querySelector("#mode")
const type =document.querySelector("#type")
const course =document.querySelector("#course")

const process_form = document.querySelector("form button")

mode.addEventListener("change", function(){
  if (mode.value == "Exam Mode"){
    type.innerHTML = `
      <option value="">----------------</option>
      <option value="Objective">Objective</option>
    `
    type.disabled = false
  }else if (mode.value == "Study Mode"){
  type.innerHTML = `
    <option value="">----------------</option>
    <option value="Objective">Objective</option>
    <option value="Theory">Theory</option>
   `
   type.disabled = false
  }else{
    type.innerHTML = `<option value="">----------------</option>`
    type.disabled = true
  }
})

process_form.addEventListener("click", function(e){
  if(!mode.value || !type.value || !course.value){
    e.preventDefault()
    document.querySelector(".configure-exam-state").style.display = "block"
  }
})
