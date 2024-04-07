const table = document.getElementById("table");
let [carbs, proteins, fats, calories] = [0, 0, 0, 0];
const GOAL_CALORIE = 2000;

// grabing html elems
const totalCarbsEl = document.getElementById("totalCarbs");
const totalProteinsEl = document.getElementById("totalProteins");
const totalFatsEl = document.getElementById("totalFats");
const totalCaloriesEl = document.getElementById("totalCalories");
const progressBarEl = document.querySelector(".progress-bar");

for (let i = 1; i < table.rows.length - 1; i++) {
  carbs += parseFloat(table.rows[i].cells[1].innerText);
  proteins += parseFloat(table.rows[i].cells[2].innerText);
  fats += parseFloat(table.rows[i].cells[3].innerText);
  calories += parseFloat(table.rows[i].cells[4].innerText);
}

totalCarbsEl.innerText = carbs.toFixed(2);
totalProteinsEl.innerText = proteins.toFixed(2);
totalFatsEl.innerText = fats.toFixed(2);
totalCaloriesEl.innerText = calories.toFixed(2);

// calculating calorie progress
const calPer = ((calories / GOAL_CALORIE) * 100).toFixed(2);
progressBarEl.style.width = `${calPer}%`;

// breakdown chart generation
const total_macros = carbs + proteins + fats;
const ctx = document.getElementById("myChart");

const data = {
  labels: ["Carbs", "Proteins", "Fats"],
  datasets: [
    {
      label: "Breakdown",
      data: [
        Math.round((carbs / total_macros) * 100),
        Math.round((proteins / total_macros) * 100),
        Math.round((fats / total_macros) * 100),
      ],
      backgroundColor: [
        "rgb(255, 99, 132)",
        "rgb(54, 162, 235)",
        "rgb(255, 205, 86)",
      ],
      hoverOffset: 4,
    },
  ],
};

new Chart(ctx, {
  type: "pie",
  data: data,
});
