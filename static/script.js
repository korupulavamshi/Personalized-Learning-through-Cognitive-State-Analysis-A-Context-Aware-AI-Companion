let attentiveTime = 0;
let distractedTime = 0;
let distractionCount = 0;
let lastStatus = "";
let currentPage = "video";

let player;

/* =========================
   YouTube API
========================= */
function onYouTubeIframeAPIReady() {
    player = new YT.Player("videoPlayer");
}

function pauseVideo() {
    if (player) player.pauseVideo();
}

function playVideo() {
    if (player) player.playVideo();
}

/* =========================
   Navigation
========================= */
function navigateTo(page) {
    const pages = ["video", "choice", "text", "quiz", "dashboard"];

    pages.forEach(p => {
        document.getElementById(p + "Page").style.display = "none";
    });

    if (page === "video") {
        document.getElementById("videoPage").style.display = "flex";
        playVideo();
    } else {
        document.getElementById(page + "Page").style.display = "block";
    }

    currentPage = page;
}

/* =========================
   Status Fetch (FIXED LOGIC)
========================= */
function fetchStatus() {
    fetch("/status")
        .then(res => res.json())
        .then(data => {

            // Initial observing state
            if (data.status === "Observing") {
                document.getElementById("statusText").innerText =
                    `Observing learner... ${data.remaining}s`;
                return;
            }

            // DISTRACTED LOGIC (IMPORTANT FIX)
            if (data.status === "Distracted" && lastStatus !== "Distracted") {
                distractionCount++;
                distractedTime += 2;
                pauseVideo();

                if (distractionCount === 1) {
                    // First distraction → stay on video
                    document.getElementById("statusText").innerText =
                        "You seem distracted. Please focus on the video.";
                }

                if (distractionCount >= 2) {
                    // Second distraction → navigate
                    navigateTo("choice");
                }
            }

            // ATTENTIVE LOGIC
            if (data.status === "Attentive") {
                attentiveTime += 2;
                document.getElementById("statusText").innerText =
                    "Status: Attentive";

                if (currentPage === "video") {
                    playVideo();
                }
            }

            lastStatus = data.status;
            updateDashboard();
        });
}

setInterval(fetchStatus, 2000);

/* =========================
   Dashboard
========================= */
function updateDashboard() {
    document.getElementById("attentiveTime").innerText = attentiveTime;
    document.getElementById("distractedTime").innerText = distractedTime;
    document.getElementById("distractionCount").innerText = distractionCount;
}

function showRecommendation() {
    const text =
        distractedTime > attentiveTime
            ? "Recommendation: Text or quiz-based learning is better."
            : "Recommendation: Video-based learning suits you.";

    document.getElementById("recommendation").innerText = text;
}

/* =========================
   Quiz
========================= */
const quizData = [
    { q: "What does AI stand for?", a: ["Artificial Intelligence", "Automated Internet"], c: 0 },
    { q: "AI is a branch of?", a: ["Computer Science", "Mechanical"], c: 0 },
    { q: "Which is AI application?", a: ["Speech Recognition", "Manual Typing"], c: 0 },
    { q: "ML is a subset of?", a: ["AI", "DBMS"], c: 0 },
    { q: "AI learns from?", a: ["Data", "Guessing"], c: 0 }
];

let qIndex = 0;

function showQuiz() {
    navigateTo("quiz");
    qIndex = 0;
    loadQuestion();
}

function loadQuestion() {
    const q = quizData[qIndex];
    document.getElementById("question").innerText = q.q;

    const optDiv = document.getElementById("options");
    optDiv.innerHTML = "";

    q.a.forEach((opt, i) => {
        const btn = document.createElement("button");
        btn.innerText = opt;
        btn.onclick = () => nextQuestion(i === q.c);
        optDiv.appendChild(btn);
    });
}

function nextQuestion(correct) {
    document.getElementById("result").innerText =
        correct ? "Correct!" : "Wrong!";

    setTimeout(() => {
        qIndex++;
        if (qIndex < quizData.length) {
            loadQuestion();
        } else {
            document.getElementById("question").innerText = "Quiz Completed!";
            document.getElementById("options").innerHTML = "";
        }
    }, 800);
}
