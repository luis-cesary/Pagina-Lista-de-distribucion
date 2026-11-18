importScripts("https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js");

self.onmessage = async (e) => {
  const { url, hojaIndex } = e.data;

  try {
    const response = await fetch(url);
    const buffer = await response.arrayBuffer();

    const wb = XLSX.read(buffer, { type: "array" });
    const hoja = wb.Sheets[wb.SheetNames[hojaIndex]];

    // ⚡ CSV es MUCHO más rápido de transferir
    const csv = XLSX.utils.sheet_to_csv(hoja);

    self.postMessage(csv);
  } catch (err) {
    console.error("Worker error:", err);
    self.postMessage("");
  }
};
