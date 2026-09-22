import React from "react";

function ClubCard({ club, isJoined, onViewDetails }) {
  return (
    <div className="club-card">
      <div className="card-top">
        <span className={`category-tag tag-${club.category.toLowerCase()}`}>
          {club.category}
        </span>
        {isJoined && <span className="joined-badge">Joined</span>}
      </div>

      <h3 className="club-name">{club.name}</h3>
      <p className="club-desc">{club.description}</p>

      <div className="card-bottom">
        <span className="member-info">
          Members: {isJoined ? club.membersCount + 1 : club.membersCount}
        </span>
        <button
          type="button"
          className="view-btn"
          onClick={() => onViewDetails(club)}
        >
          View Details
        </button>
      </div>
    </div>
  );
}

export default ClubCard;
