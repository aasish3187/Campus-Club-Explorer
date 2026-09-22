import React from "react";

function ClubModal({ club, isJoined, onToggleJoin, onClose }) {
  if (!club) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-top">
          <div>
            <span className={`category-tag tag-${club.category.toLowerCase()}`}>
              {club.category}
            </span>
            <h2 className="modal-title">{club.name}</h2>
          </div>
          <button
            type="button"
            className="modal-x-btn"
            onClick={onClose}
          >
            Close
          </button>
        </div>

        <div className="modal-body">
          {isJoined && (
            <div className="joined-status-banner">
              You have joined this club
            </div>
          )}

          <p className="modal-description">{club.description}</p>

          <div className="details-list">
            <div className="detail-item">
              <strong>Meeting Schedule:</strong>
              <span>{club.meetingDay}</span>
            </div>
            <div className="detail-item">
              <strong>Faculty Advisor:</strong>
              <span>{club.advisor}</span>
            </div>
            <div className="detail-item">
              <strong>Total Members:</strong>
              <span>{isJoined ? club.membersCount + 1 : club.membersCount} students</span>
            </div>
          </div>

          <div className="activities-block">
            <h4>Key Activities:</h4>
            <ul>
              {club.activities.map((act, index) => (
                <li key={index}>{act}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className="modal-bottom">
          <button
            type="button"
            className={`join-btn ${isJoined ? "active" : ""}`}
            onClick={() => onToggleJoin(club)}
          >
            {isJoined ? "Leave Club" : "Join Club"}
          </button>
          <button
            type="button"
            className="cancel-btn"
            onClick={onClose}
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}

export default ClubModal;
