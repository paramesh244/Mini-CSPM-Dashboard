import { useState } from "react";

export default function ConnectForm({ onScan }) {
  const [form, setForm] = useState({
    access_key: "",
    secret_key: "",
    region: "ap-south-1"
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const submit = (e) => {
    e.preventDefault();
    onScan(form);
  };

  return (
    <form onSubmit={submit} className="card">
      <h2>Connect AWS Account</h2>

      <input
        name="access_key"
        placeholder="Access Key ID"
        onChange={handleChange}
        required
      />

      <input
        name="secret_key"
        type="password"
        placeholder="Secret Access Key"
        onChange={handleChange}
        required
      />

      <input
        name="region"
        placeholder="Region (ap-south-1)"
        onChange={handleChange}
        value={form.region}
      />

      <button type="submit">Start Scan</button>
    </form>
  );
}
