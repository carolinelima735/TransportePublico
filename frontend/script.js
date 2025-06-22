document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const fileInput = document.getElementById("csvFile");
  const file = fileInput.files[0];

  if (!file) return alert("Selecione um arquivo .CSV");

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://localhost:8000/api/analisar/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    exibirTabela(data.resultado);
    desenharGrafico(data.resultado);
  } catch (error) {
    console.error(error);
    alert("Erro ao enviar o arquivo.");
  }
});

function exibirTabela(dados) {
  const container = document.getElementById("resultado");
  let html = "<h3>Resultado da Classificação:</h3>";
  html += "<table><thead><tr><th>Linha</th><th>Passageiros</th><th>Classificação</th></tr></thead><tbody>";

  dados.forEach((item) => {
    html += `<tr>
      <td>${item.linha}</td>
      <td>${item.quantidade_passageiros}</td>
      <td>${item.classificacao}</td>
    </tr>`;
  });

  html += "</tbody></table>";
  container.innerHTML = html;
}

function desenharGrafico(dados) {
  const ctx = document.getElementById("grafico").getContext("2d");

  const contagem = { Alta: 0, Média: 0, Baixa: 0 };
  dados.forEach((item) => {
    contagem[item.classificacao]++;
  });

  new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Alta", "Média", "Baixa"],
      datasets: [{
        label: "Linhas por Demanda",
        data: [contagem.Alta, contagem.Média, contagem.Baixa],
        backgroundColor: ["#f87171", "#facc15", "#4ade80"],
      }],
    },
  });
}
