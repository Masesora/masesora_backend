import { useState } from "react";

export default function ScannerFormPage() {
  const [email, setEmail] = useState("");
  const [codigo, setCodigo] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // 1. Guardamos el código para la siguiente pantalla
      localStorage.setItem("scanner_codigo", codigo);

      // 2. Redirigimos directamente a la página de resultados
      window.location.href = "/scanner-result";

    } catch (err: any) {
      setError("Error inesperado");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", maxWidth: "600px", margin: "0 auto" }}>
      <h1 style={{ color: "#1E2444" }}>Acceso al Diagnóstico Inicial</h1>
      <p>Introduce tu email y el código que te hemos enviado.</p>

      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: "15px" }}>
          <label>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ width: "100%", padding: "8px" }}
            required
          />
        </div>

        <div style={{ marginBottom: "15px" }}>
          <label>Código</label>
          <input
            type="text"
            value={codigo}
            onChange={(e) => setCodigo(e.target.value)}
            style={{ width: "100%", padding: "8px" }}
            required
          />
        </div>

        {error && (
          <p style={{ color: "red", marginTop: "10px" }}>
            {error}
          </p>
        )}

        <button
          type="submit"
          disabled={loading}
          style={{
            marginTop: "20px",
            padding: "10px 20px",
            background: "#1E2444",
            color: "white",
            borderRadius: "8px",
            border: "none",
            cursor: "pointer",
          }}
        >
          {loading ? "Accediendo…" : "Acceder al diagnóstico"}
        </button>
      </form>
    </div>
  );
}