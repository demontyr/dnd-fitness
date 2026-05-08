

let gameState = {
    character: null,
    quizCompleted: false
};


function startGame() {
    const save = localStorage.getItem("fitnessRPG");

    if (!save) {
        showQuiz();
        return;
    }

    gameState = JSON.parse(save);
    routeGame();
}


function routeGame() {
    if (!gameState.character) {
        showQuiz();
        return;
    }

    if (!gameState.quizCompleted) {
        showQuiz();
    } else {
        showGame();
    }
}

function updateMenuText() {
    const save = localStorage.getItem("fitnessRPG");
    const startBtn = document.getElementById("startBtn");

    if (!startBtn) return;

    if (save) {
        startBtn.textContent = "Continue Journey";
    } else {
        startBtn.textContent = "Begin Journey";
    }
}


function showGame() {
    if (!gameState.character) {
        console.error("No character found!");
        showQuiz();
        return;
    }

    document.getElementById("menu").style.display = "none";
    document.getElementById("quiz").style.display = "none";
    document.getElementById("game").style.display = "block";

    if (typeof updateUI === "function") {
        updateUI();
    }
}



function showQuiz() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("game").style.display = "none";
    document.getElementById("quiz").style.display = "block";

    if (typeof renderQuiz === "function") {
        renderQuiz();
    }
}



function saveGame() {
    localStorage.setItem("fitnessRPG", JSON.stringify(gameState));
    updateMenuText();
}



function loadGame() {
    const save = localStorage.getItem("fitnessRPG");

    if (!save) {
        alert("No save file found.");
        return;
    }

    gameState = JSON.parse(save);
    routeGame();
}



function resetGame() {
    const confirmReset = confirm("Reset all progress?");

    if (!confirmReset) return;

    localStorage.removeItem("fitnessRPG");

    updateMenuText(); 

    location.reload();
}

window.onload = () => {
    updateMenuText();
};