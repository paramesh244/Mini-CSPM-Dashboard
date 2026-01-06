export default function SummaryCards({ total, highRisk }) {
  return (
    <div className="summary">
      <div className="summary-card">
        <h3>Total Assets</h3>
        <p>{total}</p>
      </div>

      <div className="summary-card high">
        <h3>High Risk</h3>
        <p>{highRisk}</p>
      </div>
    </div>
  );
}
