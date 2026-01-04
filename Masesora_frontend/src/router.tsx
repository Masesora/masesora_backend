import { BrowserRouter, Routes, Route } from "react-router-dom";
import ScannerFormPage from "./pages/ScannerFormPage";
import ScannerResultPage from "./pages/ScannerResultPage";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/scanner-form" element={<ScannerFormPage />} />
        <Route path="/scanner-result" element={<ScannerResultPage />} />
      </Routes>
    </BrowserRouter>
  );
}