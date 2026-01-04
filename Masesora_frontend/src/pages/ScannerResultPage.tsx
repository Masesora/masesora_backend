import { useEffect, useState } from "react";
import { getScannerResult } from "../api/scanner";

export default function ScannerResultPage() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const codigo = localStorage.getItem("scanner_codigo");

    if (!codigo) {
      setError("No se encontró el código. Vuelve al formulario.");
      setLoading(false);
      return;
    }

    getScannerResult(codigo)
      .then((res) => {
        setData(res);
      })
      .catch(() => {
        setError("Código incorrecto o diagnóstico no disponible.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p style={{ padding: 40 }}>Cargando diagnóstico…</p>;
  }

  if (error) {
    return (
      <div style={{ padding: 40 }}>
        <h2 style={{ color: "red" }}>{error}</h2>
        <a href="/scanner-form">Volver al formulario</a>
      </div>
    );
  }

  return (
    <div style={{ padding: "40px", maxWidth: "900px", margin: "0 auto" }}>
      <h1 style={{ color: "#1E2444" }}>
        Diagnóstico Inicial — {data.empresa}
      </h1>

      <p><strong>Código:</strong> {data.codigo}</p>
      <p><strong>Facturación:</strong> {data.facturacion} €</p>

      <h2 style={{ marginTop: "30px" }}>Especialidades Enriquecidas</h2>
      <ul>
        {data.especialidades_enriquecidas?.map((esp: string, i: number) => (
          <li key={i}>{esp}</li>
        ))}
      </ul>

      <h2 style={{ marginTop: "30px" }}>Narrativa</h2>
      <p>{data.narrativa}</p>

      <h2 style={{ marginTop: "30px" }}>Síntomas</h2>
      <ul>
        {data.sintomas?.map((s: string, i: number) => (
          <li key={i}>{s}</li>
        ))}
      </ul>

      <h2 style={{ marginTop: "30px" }}>Presupuesto</h2>
      <pre>{JSON.stringify(data.presupuesto, null, 2)}</pre>

      <a
        href={`http://localhost:8000/onboarding/scanner-result/${data.codigo}/pdf`}
        target="_blank"
        rel="noopener noreferrer"
        style={{
          display: "inline-block",
          marginTop: "30px",
          padding: "12px 20px",
          background: "#1E2444",
          color: "white",
          borderRadius: "8px",
          textDecoration: "none",
        }}
      >
        Descargar PDF
      </a>
    </div>
  );
}