import React from 'react';
import '../styles/indexstyle.css'; 

// import images
import logo from '.../public/logo.png';

const NavBar = () => {
      
    return (
        <div className="container">
            <div className="sidebar">
                <h2>Civics Analytics Platform</h2>
                <ul>
                    <li><Link to="/">Dashboard</Link></li>
                    <li><Link to="/nationalsentiments">National Sentiments</Link></li>
                    <li><Link to="/nationaldisasters">National Disasters</Link></li>
                    <li><Link to="/economicdeficits">Economic Deficits</Link></li>
                </ul>
            </div>
            <div className="content">
                
            </div>
        </div>
    );
}

export default NavBar;
