import { useState } from "react";
import { scanAWS } from "./api/scan";
import ConnectForm from "./components/ConnectForm";
import SummaryCards from "./components/SummaryCards";
import AssetTable from "./components/AssetTable";
import "./App.css";

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const startScan = async (payload) => {
    setError("");
    setLoading(true);
    try {
      const res = await scanAWS(payload);
      setData(res);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Mini CSPM Dashboard</h1>

      {!data && <ConnectForm onScan={startScan} />}

      {loading && <p>Scanning AWS resources...</p>}
      {error && <p className="error">{error}</p>}

      {data && (
        <>
          <SummaryCards
            total={data.total_assets}
            highRisk={data.high_risk_assets}
          />
          <AssetTable resources={data.resources} />
        </>
      )}
    </div>
  );
}

export default App;
