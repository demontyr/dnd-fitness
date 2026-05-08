let creationStep = 0;

function renderQuiz() {
    const quizDiv = document.getElementById("quiz");

    if (creationStep === 0) {
        quizDiv.innerHTML = `
            <h2>Character Creation</h2>
            <button onclick="askName()">Start Character</button>
        `;
    }

    else if (creationStep === 1) {
        quizDiv.innerHTML = `
            <h2>Confirm Your Name</h2>
            <p>You are: <strong>${gameState.tempName}</strong></p>

            <button onclick="confirmName()">Yes</button>
            <button onclick="askName()">Change Name</button>
        `;
    }

    else if (creationStep === 2) {
        quizDiv.innerHTML = `
            <h2>Character Creation</h2>
            <p>Name: <strong>${gameState.character.name}</strong></p>
            <p>Ready to generate stats?</p>

            <button onclick="generateCharacter()">Roll Stats</button>
        `;
    }

    else if (creationStep === 3) {
        const c = gameState.character;

        quizDiv.innerHTML = `
            <h2>Review Your Stats</h2>

            <p><strong>Strength:</strong> ${c.strength}</p>
            <p><strong>Dexterity:</strong> ${c.dexterity}</p>
            <p><strong>Constitution:</strong> ${c.constitution}</p>
            <p><strong>Intelligence:</strong> ${c.intelligence}</p>
            <p><strong>Wisdom:</strong> ${c.wisdom}</p>
            <p><strong>Charisma:</strong> ${c.charisma}</p>

            <button onclick="confirmStats()">Confirm</button>
            <button onclick="rerollStats()">Reroll</button>
        `;
    }
}



function generateCharacter() {
    gameState.character.strength = rollStat();
    gameState.character.dexterity = rollStat();
    gameState.character.constitution = rollStat();
    gameState.character.intelligence = rollStat();
    gameState.character.wisdom = rollStat();
    gameState.character.charisma = rollStat();

    creationStep = 3; 
    renderQuiz();
}


function rollStat() {
    return Math.floor(Math.random() * 20) + 1;
}

function askName() {
    const name = prompt("What do they call you?");
    
    if (!name) return askName(); 

    gameState.tempName = name;
    creationStep = 1;
    renderQuiz();
}

function confirmName() {
    gameState.character = {
        name: gameState.tempName,
        strength: 0,
        dexterity: 0,
        constitution: 0,
        intelligence: 0,
        wisdom: 0,
        charisma: 0,
        stamina: 100,
        maxStamina: 100,
        level: 1,
        xp: 0,
        gold: 0
    };

    creationStep = 2;
    renderQuiz();
}

function confirmStats() {
    gameState.quizCompleted = true;

    saveGame();
    showGame();
}

function rerollStats() {
    generateCharacter();
}