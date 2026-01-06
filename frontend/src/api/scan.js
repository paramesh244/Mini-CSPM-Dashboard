export async function scanAWS(payload) {
  const response = await fetch("http://localhost:8000/api/v1/scan", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || "Scan failed");
  }

  return response.json();
}
