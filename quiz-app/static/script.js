
aiGeneratedQuestions = [
  {
    question: "Full form of Html?",
    responses: ["Hello to my world", "Hey text my language","Hyper text Markup language","Hyper text Makeup language"],
    correct: "Hyper text Markup language"
  },
  {
    question: "why do we use ReactJs?",
    responses: ["For building UI's","For back-end","For data-bases","It's nothing."],
    correct: "For building UI's"
  },
  {
    question: "Which tag is incorrect?",
    responses: ["<kbd>","<html>","<abbr>","All are correct"],
    correct: "All are correct"
  }
];

// getting referrence

const questionContainer = document.querySelector("h2");
const option1 = document.querySelector("#option1");
const option2 = document.querySelector("#option2");
const option3 = document.querySelector("#option3");
const option4 = document.querySelector("#option4");
const submitButton = document.querySelector("button");
const usersAnswer = document.querySelectorAll(".answer");
const scoreArea = document.querySelector("#ShowScore");


// aiGeneratedQuestions = document.currentScript.getAttribute("questions")
// aiGeneratedQuestions = aiGeneratedQuestions.replaceAll("\'", "\"")
// aiGeneratedQuestions = JSON.parse(aiGeneratedQuestions)

console.log(aiGeneratedQuestions)

// This function is rendering all the texts

let questionCount = 0;
let score = 0;
const mainFunc = () => {
  const list = aiGeneratedQuestions[questionCount];
  
  questionContainer.innerText = list.question;
  option1.innerText = list.responses[0];
  option2.innerText = list.responses[1];
  option3.innerText = list.responses[2];
  option4.innerText = list.responses[3];

  for (let i = 0; i <=3; i++) {
    document.getElementsByClassName("answer")[i].value = list.responses[i]
  }
};

try{
  mainFunc(); 
} 
catch(err) {
  document.getElementsByTagName('ul')[0].innerHTML = "<p>Not connected to quiz generator service</p>"
}

// this function is for answer checking

const goCheckAnswer = () => {
  let answers;
  usersAnswer.forEach((data) => {
    if (data.checked) {
      answers = data.value;
    }
  });
  return answers;
};

const deselectAll = () => {
  usersAnswer.forEach((data) => {
    data.checked = false;
  });
};

submitButton.addEventListener("click", () => {
  const checkAnswer = goCheckAnswer();
  console.log(checkAnswer);

  if (checkAnswer === aiGeneratedQuestions[questionCount].correct) {
    score++;
  }
  questionCount++;
  deselectAll();
  if (questionCount < aiGeneratedQuestions.length) {
    mainFunc();
  } else {
    scoreArea.style.display = "block";
    scoreArea.innerHTML = `
      <h3>Your score is ${score} / ${aiGeneratedQuestions.length}</h3>
      <button class='btn' onclick='location.reload()'>Play Again</button>
      `;
  }
});
