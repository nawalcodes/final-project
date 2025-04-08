import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Comparison from './pages/Comparison';
import MapView from './pages/MapView';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/comparison" element={<Comparison />} />
        <Route path="/map" element={<MapView />} />
      </Routes>
    </Router>
  );
}

export default App;
