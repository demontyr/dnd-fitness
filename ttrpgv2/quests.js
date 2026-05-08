// =====================
// QUEST DATA
// =====================

const dailyPool = [
    { text: "Walk 10,000 steps", xp: 10, gold: 5 },
    { text: "Drink 2 liters of water", xp: 5, gold: 3 },
    { text: "Do 20 push-ups", xp: 15, gold: 7 },
    { text: "Stretch 10 minutes", xp: 8, gold: 4 }
];

const weeklyPool = [
    { text: "Workout 3 times", xp: 50, gold: 20 },
    { text: "Run 5km", xp: 35, gold: 15 },
    { text: "100 pushups this week", xp: 45, gold: 18 }
];

const encountersPool = [
    {
        text: "A bandit ambushes you!",
        options: [
            { text: "Fight! (15 squats)", xp: 10, gold: 5, stamina: 25 },
            { text: "Run! (Jumping jacks)", xp: 7, gold: 3, stamina: 15 }
        ]
    }
];

// =====================
// ACTIVE STATE
// =====================

let activeDaily = [];
let activeWeekly = [];

let selectedDaily = null;
let selectedWeekly = null;

// prevents double weekly completion bug
let weeklyLock = false;


// =====================
// SAFETY HELPERS
// =====================

function clampStamina() {
    const c = gameState.character;
    if (!c) return;

    if (c.stamina > c.maxStamina) c.stamina = c.maxStamina;
    if (c.stamina < 0) c.stamina = 0;
}


// =====================
// UI UPDATE
// =====================

function updateUI() {
    const c = gameState.character;
    if (!c) return;

    document.getElementById("status").innerHTML = `
        <h2>Status</h2>
        <p>Name: ${c.name}</p>
        <p>Level: ${c.level}</p>
        <p>XP: ${c.xp}</p>
        <p>Gold: ${c.gold}</p>
        <p>Stamina: ${c.stamina}/${c.maxStamina}</p>
    `;
}


// =====================
// DAILY QUESTS
// =====================

function viewDaily() {
    activeDaily = [...dailyPool]
        .sort(() => Math.random() - 0.5)
        .slice(0, 3);

    let html = "<h2>Daily Quests</h2>";

    activeDaily.forEach((quest, index) => {
        html += `
            <p>
                ${quest.text}
                <button onclick="selectDaily(${index})">Select</button>
            </p>
        `;
    });

    document.getElementById("output").innerHTML = html;
}

function selectDaily(index) {
    if (selectedDaily) {
        alert("I already have a daily quest to finish.");
        return;
    }

    selectedDaily = activeDaily[index];
    saveGame();
    alert("Daily Quest Selected");
}


// =====================
// WEEKLY QUESTS
// =====================

function viewWeekly() {
    activeWeekly = [...weeklyPool]
        .sort(() => Math.random() - 0.5)
        .slice(0, 3);

    let html = "<h2>Weekly Quests</h2>";

    activeWeekly.forEach((quest, index) => {
        html += `
            <p>
                ${quest.text}
                <button onclick="selectWeekly(${index})">Select</button>
            </p>
        `;
    });

    document.getElementById("output").innerHTML = html;
}

function selectWeekly(index) {
    if (selectedWeekly) {
        alert("I already have a Weekly quest to finish.");
        return;
    }

    selectedWeekly = activeWeekly[index];
    saveGame();
    alert("Weekly Quest Selected");
}


// =====================
// SELECTED VIEW
// =====================

function viewSelected() {
    let html = "<h2>Selected Quests</h2>";

    if (selectedDaily) {
        html += `
            <p>
                DAILY: ${selectedDaily.text}
                <button onclick="completeDaily()">Complete</button>
                <button onclick="dropDaily()">Drop</button>
            </p>
        `;
    } else {
        html += "<p>DAILY: No quest selected</p>";
    }

    if (selectedWeekly) {
        html += `
            <p>
                WEEKLY: ${selectedWeekly.text}
                <button onclick="completeWeekly()">Complete</button>
                <button onclick="dropWeekly()">Drop</button>
            </p>
        `;
    } else {
        html += "<p>WEEKLY: No quest selected</p>";
    }

    document.getElementById("output").innerHTML = html;
}


// =====================
// DROP QUESTS
// =====================

function dropDaily() {
    if (!confirm("Drop current daily quest?")) return;

    selectedDaily = null;
    saveGame();
    viewSelected();
}

function dropWeekly() {
    if (!confirm("Drop current weekly quest?")) return;

    selectedWeekly = null;
    saveGame();
    viewSelected();
}


// =====================
// COMPLETE DAILY
// =====================

function completeDaily() {
    if (!selectedDaily || !gameState.character) return;

    rewardPlayer(selectedDaily.xp, selectedDaily.gold);

    alert(`Completed: ${selectedDaily.text}`);

    selectedDaily = null;
    saveGame();
    viewSelected();
}


// =====================
// COMPLETE WEEKLY (FIXED)
// =====================

function completeWeekly() {
    if (weeklyLock) return;
    weeklyLock = true;

    if (!selectedWeekly || !gameState.character) {
        weeklyLock = false;
        return;
    }

    rewardPlayer(selectedWeekly.xp, selectedWeekly.gold);

    alert(`Completed: ${selectedWeekly.text}`);

    selectedWeekly = null;
    saveGame();
    viewSelected();

    weeklyLock = false;
}


// =====================
// RANDOM ENCOUNTER
// =====================

function randomEncounter() {
    const e = encountersPool[
        Math.floor(Math.random() * encountersPool.length)
    ];

    let html = `<h2>${e.text}</h2>`;

    e.options.forEach((option, index) => {
        html += `
            <button onclick="doEncounter(${index})">
                ${option.text}
            </button>
            <br><br>
        `;
    });

    document.getElementById("output").innerHTML = html;
}


// =====================
// ENCOUNTER ACTION
// =====================

function doEncounter(optionIndex) {
    const e = encountersPool[0];
    const option = e.options[optionIndex];
    const c = gameState.character;

    if (!c) return;

    if (c.stamina < option.stamina) {
        alert("Too tired for this encounter!");
        return;
    }

    c.stamina -= option.stamina;
    clampStamina();

    rewardPlayer(option.xp, option.gold);

    alert(`Encounter Completed! -${option.stamina} stamina`);
}


// =====================
// REWARD SYSTEM
// =====================

function rewardPlayer(xp, gold) {
    const c = gameState.character;
    if (!c) return;

    c.xp += xp;
    c.gold += gold;

    checkLevelUp();

    clampStamina();

    saveGame();
    updateUI();
}


// =====================
// LEVEL UP SYSTEM
// =====================

function checkLevelUp() {
    const c = gameState.character;
    if (!c) return;

    const xpToNext = c.level * 50;

    if (c.xp >= xpToNext) {
        c.xp -= xpToNext;
        c.level++;

        c.maxStamina += 10;
        c.stamina = c.maxStamina;

        alert(`LEVEL UP! You are now level ${c.level}`);
    }
}