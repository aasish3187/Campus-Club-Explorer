import React, { useState } from "react";
import "./App.css";
import ClubCard from "./components/ClubCard";

const clubsData = [
  {
    id: 1,
    name: "Code Crafters Club",
    category: "Coding",
    description: "A community for programmers, web developers, and coding enthusiasts.",
    membersCount: 140,
    meetingDay: "Wednesday, 5:00 PM",
    advisor: "Dr. K. Srinivas",
    activities: [
      "Weekly Web Development & DSA workshops",
      "College coding contests & hackathons",
      "Open source project guidance"
    ]
  },
  {
    id: 2,
    name: "AI & Robotics Club",
    category: "Coding",
    description: "Hands-on projects exploring Machine Learning and Arduino robotics.",
    membersCount: 95,
    meetingDay: "Friday, 4:30 PM",
    advisor: "Prof. P. Lakshmi",
    activities: [
      "Robotics design and hardware interfacing",
      "Machine learning models with Python",
      "Technical paper discussions"
    ]
  },
  {
    id: 3,
    name: "Strikers Sports Club",
    category: "Sports",
    description: "Promoting physical fitness, team spirit, and competitive sports on campus.",
    membersCount: 180,
    meetingDay: "Tuesday & Thursday, 6:00 AM",
    advisor: "Mr. R. Narayana",
    activities: [
      "Inter-department cricket and football tournaments",
      "Daily fitness and conditioning sessions",
      "University sports meet participation"
    ]
  },
  {
    id: 4,
    name: "Badminton & Table Tennis League",
    category: "Sports",
    description: "Indoor sports enthusiasts gathering for matches and tournaments.",
    membersCount: 75,
    meetingDay: "Saturday, 7:00 AM",
    advisor: "Mr. V. Mahesh",
    activities: [
      "Weekend knockout singles and doubles matches",
      "Court technique and fitness training",
      "Annual campus racket sports tournament"
    ]
  },
  {
    id: 5,
    name: "Fine Arts & Drama Guild",
    category: "Arts",
    description: "Expressing creativity through painting, theater, and cultural performances.",
    membersCount: 110,
    meetingDay: "Thursday, 4:00 PM",
    advisor: "Dr. Ananya Roy",
    activities: [
      "Annual cultural fest stage plays",
      "Campus art exhibitions and live sketching",
      "Short film and photography projects"
    ]
  },
  {
    id: 6,
    name: "Music & Band Society",
    category: "Arts",
    description: "Vocalists, instrumentalists, and band members practicing music together.",
    membersCount: 85,
    meetingDay: "Monday & Friday, 5:00 PM",
    advisor: "Prof. S. Balasubrahmanyam",
    activities: [
      "Acoustic jam sessions",
      "College fest musical performances",
      "Instrumental practice and sound mixing basics"
    ]
  },
  {
    id: 7,
    name: "Entrepreneurship Cell (E-Cell)",
    category: "Entrepreneurship",
    description: "Fostering startup ideas, business plans, and student innovations.",
    membersCount: 120,
    meetingDay: "Saturday, 3:00 PM",
    advisor: "Dr. M. Venkat Rao",
    activities: [
      "Campus idea pitching sessions",
      "Guest lectures from successful startup founders",
      "Business model canvas and validation workshops"
    ]
  },
  {
    id: 8,
    name: "Social Innovation Club",
    category: "Entrepreneurship",
    description: "Building sustainable projects to solve local and campus challenges.",
    membersCount: 65,
    meetingDay: "Tuesday, 4:30 PM",
    advisor: "Dr. G. Radhika",
    activities: [
      "Campus sustainability and recycling initiatives",
      "Community outreach programs",
      "Project ideation for social good"
    ]
  }
];

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

      <header className="navbar">
        <div className="navbar-container">
          <div className="header-brand">
            <span className="campus-icon">🏛️</span>
            <div>
              <h1 className="navbar-title">Campus Club Explorer</h1>
              <p className="navbar-subtitle">Vignan University • Discover and connect with student clubs</p>
            </div>
          </div>
        </div>
      </header>

      <main className="content">
        <div className="filter-panel">
          <div className="search-group">
            <label htmlFor="search-input" className="search-label">
              Search Clubs:
            </label>
            <div className="search-input-wrapper">
              <input
                id="search-input"
                type="text"
                className="search-input"
                placeholder="Type club name or topic..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
              {searchQuery && (
                <button
                  type="button"
                  className="clear-btn"
                  onClick={() => setSearchQuery("")}
                >
                  Clear
                </button>
              )}
            </div>
          </div>

          <div className="category-group">
            <span className="category-label">Filter by Interest:</span>
            <div className="category-buttons">
              {categories.map((category) => (
                <button
                  key={category}
                  type="button"
                  className={`category-btn ${selectedCategory === category ? "selected" : ""}`}
                  onClick={() => setSelectedCategory(category)}
                >
                  {category}
                </button>
              ))}
            </div>
          </div>

          <div className="count-info">
            Available Clubs: <strong>{filteredClubs.length}</strong> | Joined Clubs:{" "}
            <strong>{joinedClubIds.length}</strong>
          </div>
        </div>

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

      {selectedClub && (
        <div className="modal-overlay" onClick={handleCloseDetails}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-top">
              <div>
                <span className={`category-tag tag-${selectedClub.category.toLowerCase()}`}>
                  {selectedClub.category}
                </span>
                <h2 className="modal-title">{selectedClub.name}</h2>
              </div>
              <button
                type="button"
                className="modal-x-btn"
                onClick={handleCloseDetails}
              >
                Close
              </button>
            </div>

            <div className="modal-body">
              {joinedClubIds.includes(selectedClub.id) && (
                <div className="joined-status-banner">
                  ✓ You have joined this club
                </div>
              )}

              <p className="modal-description">{selectedClub.description}</p>

              <div className="details-list">
                <div className="detail-item">
                  <strong>Meeting Schedule:</strong>
                  <span>{selectedClub.meetingDay}</span>
                </div>
                <div className="detail-item">
                  <strong>Faculty Advisor:</strong>
                  <span>{selectedClub.advisor}</span>
                </div>
                <div className="detail-item">
                  <strong>Total Members:</strong>
                  <span>
                    {joinedClubIds.includes(selectedClub.id)
                      ? selectedClub.membersCount + 1
                      : selectedClub.membersCount}{" "}
                    students
                  </span>
                </div>
              </div>

              <div className="activities-block">
                <h4>Key Activities:</h4>
                <ul>
                  {selectedClub.activities.map((act, index) => (
                    <li key={index}>{act}</li>
                  ))}
                </ul>
              </div>
            </div>

            <div className="modal-bottom">
              <button
                type="button"
                className={`join-btn ${joinedClubIds.includes(selectedClub.id) ? "active" : ""}`}
                onClick={() => handleToggleJoin(selectedClub)}
              >
                {joinedClubIds.includes(selectedClub.id) ? "Leave Club" : "Join Club"}
              </button>
              <button
                type="button"
                className="cancel-btn"
                onClick={handleCloseDetails}
              >
                Done
              </button>
            </div>
          </div>
        </div>
      )}

      <footer className="footer-bar">
        <div className="footer-container">
          <span>Campus Club Explorer</span>
          <span>College Training Assessment Project</span>
        </div>
      </footer>
    </div>
  );
}

export default App;
