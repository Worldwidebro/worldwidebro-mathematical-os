import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import BankingVerticalPage from './pages/BankingVerticalPage';

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/verticals/banking" element={<BankingVerticalPage />} />
    </Routes>
  );
}

export default App;
