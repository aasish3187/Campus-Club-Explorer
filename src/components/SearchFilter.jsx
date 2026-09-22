import React from "react";

function SearchFilter({
  searchQuery,
  onSearchChange,
  selectedCategory,
  onSelectCategory,
  categories,
  totalCount
}) {
  return (
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
            onChange={(e) => onSearchChange(e.target.value)}
          />
          {searchQuery && (
            <button
              type="button"
              className="clear-btn"
              onClick={() => onSearchChange("")}
            >
              Clear
            </button>
          )}
        </div>
      </div>

      <div className="category-group">
        <span className="category-label">Filter by Interest:</span>
        <div className="category-buttons">
          {categories.map((category) => {
            const isSelected = selectedCategory === category;
            return (
              <button
                key={category}
                type="button"
                className={`category-btn ${isSelected ? "selected" : ""}`}
                onClick={() => onSelectCategory(category)}
              >
                {category}
              </button>
            );
          })}
        </div>
      </div>

      <div className="count-info">
        Available Clubs: <strong>{totalCount}</strong>
      </div>
    </div>
  );
}

export default SearchFilter;
