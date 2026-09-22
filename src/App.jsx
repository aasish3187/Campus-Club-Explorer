import React, { useState } from "react";
import "./App.css";
import { clubsData } from "./ClubsData";
import Navbar from "./components/Navbar";
import SearchFilter from "./components/SearchFilter";
import ClubCard from "./components/ClubCard";
import ClubModal from "./components/ClubModal";

function App() {
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [selectedClub, setSelectedClub] = useState(null);
  const [joinedClubIds, setJoinedClubIds] = useState([]);
  const [popupMessage, setPopupMessage] = useState("");

  const categories = ["All", "Coding", "Sports", "Arts", "Entrepreneurship"];

  const filteredClubs = clubsData.filter((club) => {
    const matchesCategory =
      selectedCategory === "All" || club.category === selectedCategory;

    const matchesSearch =
      club.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      club.description.toLowerCase().includes(searchQuery.toLowerCase());

    return matchesCategory && matchesSearch;
  });

  const showPopup = (msg) => {
    setPopupMessage(msg);
    setTimeout(() => {
      setPopupMessage("");
    }, 3000);
  };

  const handleToggleJoin = (club) => {
    if (joinedClubIds.includes(club.id)) {
      setJoinedClubIds(joinedClubIds.filter((id) => id !== club.id));
      showPopup("You have left " + club.name);
    } else {
      setJoinedClubIds([...joinedClubIds, club.id]);
      showPopup("Success: You have joined " + club.name + "!");
    }
  };

  const handleOpenDetails = (club) => {
    setSelectedClub(club);
  };

  const handleCloseDetails = () => {
    setSelectedClub(null);
  };

  const handleReset = () => {
    setSearchQuery("");
    setSelectedCategory("All");
  };

  return (
    <div className="app">
      {popupMessage && (
        <div className="popup-toast">
          <span>{popupMessage}</span>
          <button
            type="button"
            className="popup-toast-close"
            onClick={() => setPopupMessage("")}
          >
            ✕
          </button>
        </div>
      )}

      <Navbar />

      <main className="content">
        <SearchFilter
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          selectedCategory={selectedCategory}
          onSelectCategory={setSelectedCategory}
          categories={categories}
          totalCount={filteredClubs.length}
        />

        {filteredClubs.length > 0 ? (
          <div className="club-grid">
            {filteredClubs.map((club) => (
              <ClubCard
                key={club.id}
                club={club}
                isJoined={joinedClubIds.includes(club.id)}
                onViewDetails={handleOpenDetails}
              />
            ))}
          </div>
        ) : (
          <div className="no-results">
            <h3>No clubs found</h3>
            <p>No club matches your search criteria.</p>
            <button
              type="button"
              className="reset-btn"
              onClick={handleReset}
            >
              Reset Filters
            </button>
          </div>
        )}
      </main>

      <ClubModal
        club={selectedClub}
        isJoined={selectedClub ? joinedClubIds.includes(selectedClub.id) : false}
        onToggleJoin={handleToggleJoin}
        onClose={handleCloseDetails}
      />

      <footer className="footer-bar">
        <div className="footer-container">
          <span>Campus Club Explorer • Vignan University</span>
          <span>College Training Assessment Project</span>
        </div>
      </footer>
    </div>
  );
}

export default App;
