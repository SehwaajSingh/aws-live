const cloudStatus = document.getElementById("cloudStatus");
const pipelineStatus = document.getElementById("pipelineStatus");
const serverHealth = document.getElementById("serverHealth");
const deployMessage = document.getElementById("deployMessage");

function randomStatus() {
  const statuses = ["Healthy ✅", "Warning ⚠️", "Down ❌"];
  return statuses[Math.floor(Math.random() * statuses.length)];
}

// Simulate live monitoring
setInterval(() => {
  cloudStatus.textContent = randomStatus();
  pipelineStatus.textContent = "Build ✔️ Test ✔️ Deploy ✔️";
  serverHealth.textContent = `${Math.floor(Math.random() * 40) + 60}% CPU Usage`;
}, 3000);

function deployApp() {
  deployMessage.textContent = "Deploying application...";
  deployMessage.style.color = "#ffd700";

  setTimeout(() => {
    deployMessage.textContent = "Deployment Successful ✅";
    deployMessage.style.color = "#00ff9d";
  }, 3000);
}
