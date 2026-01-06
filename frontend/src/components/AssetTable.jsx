import { useState } from "react";

export default function AssetTable({ resources }) {
  const [showHighRisk, setShowHighRisk] = useState(false);

  const filtered = showHighRisk
    ? resources.filter(r => r.risk === "High Risk")
    : resources;

  return (
    <div className="table-container">
      <label className="filter-label">
        <input
          type="checkbox"
          onChange={() => setShowHighRisk(!showHighRisk)}
        />Show High Risk Only
      </label>

      <table>
        <thead>
          <tr>
            <th>Name / ID</th>
            <th>Type</th>
            <th>Status</th>
            <th>Risk</th>
          </tr>
        </thead>
        <tbody className="table-body">
          {filtered.map((r, i) => (
            <tr key={i}>
              <td>{r.id || r.name}</td>
              <td>{r.type}</td>
              <td>{r.status || "-"}</td>
              <td className={r.risk === "High Risk" ? "risk-high" : "risk-low"}>
                {r.risk}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
