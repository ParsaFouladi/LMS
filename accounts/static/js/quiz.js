let category = document.querySelector(".info .category span")
let questionsCount = document.querySelector(".info .count span")
let progress = document.querySelector(".sub")
let bullets = document.querySelector(".sub .spans .bullets")
let questionArea = document.querySelector(".question-area")
let answersArea = document.querySelector(".answers-area")
let button = document.getElementById("btn")
// let resultArea = document.querySelector(".results")
let countDown = document.querySelector(".countdown")
let main = document.querySelector(".main")
let index = 0
let correctCount = 0
let counter
function getData(){
    fetch("html_exam.json")
    .then((response) => response.json())
    .then(data => {

        initiatebullets(data.length)

        getQuestion(data[index], data.length)
        
        timer(5)

        button.onclick = function() {
            let rightAnswer = data[index].right_answer
            console.log(index)
            console.log(data.length)
            index++
            checkAnswer(rightAnswer, data.length)

            questionArea.innerHTML = ""
            answersArea.innerHTML = ""

            if(index < data.length) {

                getQuestion(data[index], data.length)

                handleBullets()
            }
            
            clearInterval(counter)
            timer(5)
            if(index === data.length) showResults(data.length)

        }
    })
}

function initiatebullets(num){
    questionsCount.innerHTML = num
    for(let i = 0; i < num; i++){
        let span = document.createElement("span")
        if(i == 0){
            span.className = "active"
            bullets.append(span)
        } else{
            bullets.append(span)
        }
    }
}

function getQuestion(q){
    let question = document.createElement("h3")
    question.append(q["title"])
    questionArea.append(question)

    for(let i = 0; i < 4; i++){
        let mainDiv = document.createElement("div")
        mainDiv.className = "answer"

        let radio = document.createElement("input")
        radio.type = "radio"
        radio.name = "answer"
        radio.id = `answer_${i}`
        radio.dataset.answer = q[`answer_${i+1}`]
        
        let label  = document.createElement("label")
        label.htmlFor = `answer_${i}`
        label.append(q[`answer_${i+1}`])

        mainDiv.append(radio, label)
        answersArea.append(mainDiv)
    }
}

function checkAnswer(right){
    let answers = document.getElementsByName("answer")
    let theChosenAnswer

    for(let i = 0; i < answers.length; i++){
        if(answers[i].checked){
            theChosenAnswer = answers[i].dataset.answer
        }
    }
    if(right === theChosenAnswer){
        correctCount++
    }
}

function handleBullets(){
    let spans = document.querySelectorAll(".sub .spans .bullets span")
    let spansArray = Array.from(spans)
    spansArray.forEach((span, i) => {
        if(index === i){
            span.classList.add("active")
        }
    })
}

function showResults(qCount){

    questionArea.remove()
    answersArea.remove()
    button.remove()
    progress.remove()

    let result;

    if(correctCount > (qCount / 2) && correctCount < qCount){
        result = `<span class="green">Nice</span>, you answered ${correctCount} out of ${qCount}`
    } else if(correctCount === qCount){
        result = `<span class="blue">Perfect</span>, you answered ${correctCount} out of ${qCount}!`
    } else{
        result = `<span class="red">Unfortunately</span>, you answered ${correctCount} out of ${qCount}!`
    }

    let resultArea = document.createElement("div")
    resultArea.className = "results"
    resultArea.innerHTML = result
    resultArea.style.padding = '15px'
    main.append(resultArea)

    // resultArea.innerHTML = result

}

function timer(time){

    let minutes, seconds

    

    counter = setInterval(() => {
        
        minutes = parseInt(time / 60)
        seconds = parseInt(time % 60)

        minutes = minutes < 10 ? `0${minutes}` : minutes
        seconds = seconds < 10 ? `0${seconds}` : seconds

        countDown.innerHTML = `<h3>Remaining Time</h3> ${minutes} : ${seconds}`
        // countDown.append(`${minutes} : ${seconds}`)

        if(--time < 0){
            clearInterval(counter)
            button.click()
        }

    }, 1000);
}


getData()