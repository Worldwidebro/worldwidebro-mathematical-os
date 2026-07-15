import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import WhoIAm from './pages/WhoIAm';
import Services from './pages/Services';
import Proof from './pages/Proof';
import Ventures from './pages/Ventures';
import VentureDetail from './pages/VentureDetail';
import Sectors from './pages/Sectors';
import SectorPage from './pages/SectorPage';
import Contact from './pages/Contact';
import Privacy from './pages/Privacy';
import Terms from './pages/Terms';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/who-i-am" element={<WhoIAm />} />
      <Route path="/services" element={<Services />} />
      <Route path="/proof" element={<Proof />} />
      <Route path="/ventures" element={<Ventures />} />
      <Route path="/ventures/:id" element={<VentureDetail />} />
      <Route path="/sectors" element={<Sectors />} />
      <Route path="/sectors/:sectorId" element={<SectorPage />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/privacy" element={<Privacy />} />
      <Route path="/terms" element={<Terms />} />
    </Routes>
  );
}

export default App;
