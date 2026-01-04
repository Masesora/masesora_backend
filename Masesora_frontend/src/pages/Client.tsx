export async function getDemoClient() {
  const res = await fetch("http://localhost:8000/clients/demo");
  return res.json();
}