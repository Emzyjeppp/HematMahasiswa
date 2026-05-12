async function saveExpense() {
  const desc = document.getElementById("desc").value;
  const amount = document.getElementById("amount").value;

  if (!desc || !amount) {
    alert("Isi dulu dong datanya!");
    return;
  }

  const response = await fetch("/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      desc: desc,
      amount: parseInt(amount),
      date: new Date().toISOString(),
    }),
  });

  if (response.ok) {
    location.reload(); // Refresh buat update tampilan
  }
}
