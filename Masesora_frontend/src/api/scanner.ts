export async function getScannerResult(codigo: string) {
  const res = await fetch(`http://localhost:8000/onboarding/scanner-result/${codigo}`);

  if (!res.ok) {
    throw new Error("Código no encontrado");
  }

  return res.json();
}