// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/dashboard/dashboard.js';
import NationalDisasters from './pages/nationaldisasters/nationaldisasters.js';
import EconomicDeficits from './pages/economicdeficits/economicdeficits.js';
import NationalSentiments from './pages/nationalsentiments/nationalsentiments.js';
import './styles/styles.css'; // Import your styles
import './styles/indexstyle.css';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" exact component={Dashboard} />
                <Route path="/nationaldisasters" component={NationalDisasters} />
                <Route path="/economicdeficits" component={EconomicDeficits} />
                <Route path="/nationalsentiments" component={NationalSentiments} />
            </Routes>
        </Router>
    );
};

export default App;