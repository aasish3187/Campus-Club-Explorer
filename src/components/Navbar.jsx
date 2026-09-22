import React from "react";

function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-container">
        <div className="header-brand">
          <span className="campus-icon">🏛️</span>
          <div>
            <h1 className="navbar-title">Campus Club Explorer</h1>
            <p className="navbar-subtitle">Discover and connect with college student clubs</p>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Navbar;
