const btn = document.getElementById("btn_click")
const text_input = document.getElementById("text_input")
const rezult = document.getElementById("rezult")
let message = ""

function btnClickReaction() {
    alert(message)
    rezult.innerHTML = message
}

btn.addEventListener('click', btnClickReaction)

text_input.addEventListener('input', function(event) {
    message = event.target.value
    console.log(event.target.value)
})

document.addEventListener('keydown', function(event) {
    if (event.keyCode === 13) {
        console.log("salam", event.key)
    }
    console.log(event.key)
})