# Campus Club Explorer - Lab Evaluation Explanation Guide

This guide provides simple, direct, human-written explanations for each concept covered in this project. You can speak these exact points during your evaluation/viva.

---

## 1. Project Overview
> *"This project is a React web application called **Campus Club Explorer**. It allows college students to discover clubs, search by keyword, filter clubs by categories (Coding, Sports, Arts, Entrepreneurship), and view full club details in a popup modal."*

---

## 2. Core Concepts Explained (In Simple Terms)

### A. Props
- **Where it is used:** 
  - In `ClubCard.jsx` (`club`, `onViewDetails`).
  - In `ClubModal.jsx` (`club`, `onClose`).
  - In `SearchFilter.jsx` (`searchQuery`, `onSearchChange`, `selectedCategory`, `onSelectCategory`, etc.).
- **How to explain:**
  > *"Props are used to pass data from a parent component down to a child component. For example, `App.jsx` passes the club data object and a click handler function to `ClubCard` as props."*

### B. Lists & Keys
- **Where it is used:**
  - In `App.jsx`: `filteredClubs.map((club) => <ClubCard key={club.id} ... />)`
  - In `SearchFilter.jsx`: `categories.map((cat) => ...)`
  - In `ClubModal.jsx`: `club.activities.map((act, index) => ...)`
- **How to explain:**
  > *"To display a list of clubs, we use JavaScript's `.map()` method to loop through the array and return a card for each item. React requires a unique `key` prop (here `club.id`) so it can efficiently track and re-render only the items that change."*

### C. Search and Filter UI
- **Where it is used:**
  - `SearchFilter.jsx` and the filtering logic in `App.jsx`.
- **How to explain:**
  > *"We use `useState` to store the search query and the selected category. The `filteredClubs` array is computed by checking if the club's category matches the active button and if the club name contains the search text using `.toLowerCase().includes()`."*

### D. Conditional Rendering
- **Where it is used:**
  1. **Empty State:** If `filteredClubs.length > 0`, we render the club grid; otherwise, we display a *"No clubs found"* message.
  2. **Modal Dialog:** `{selectedClub && <ClubModal ... />}` — the modal only renders when a user clicks on a club to select it.
- **How to explain:**
  > *"Conditional rendering means showing different UI elements based on state conditions. We use a ternary operator to show the club cards if available, or an empty state if no clubs match. We also use the `&&` operator to render the modal only when `selectedClub` is not null."*

### E. Component Reuse
- **Where it is used:**
  - `<ClubCard />` component is written once and reused for all 8 clubs.
- **How to explain:**
  > *"Instead of repeating the same card markup multiple times, we created a single reusable `ClubCard` component. It receives different data via props and renders consistently."*

---

## 3. Project Structure
```text
src/
├── data/
│   └── clubsData.js       -> Array of 8 club objects
├── components/
│   ├── Navbar.jsx         -> Top header bar
│   ├── SearchFilter.jsx   -> Search box + category buttons
│   ├── ClubCard.jsx       -> Reusable card for a club
│   └── ClubModal.jsx      -> Details popup dialog
├── App.jsx                -> Main parent component managing state
├── App.css                -> Solid color styling (no gradients)
├── index.css              -> Base CSS reset
└── main.jsx               -> React DOM entry point
```
