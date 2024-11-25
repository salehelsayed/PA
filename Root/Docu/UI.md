# Frontend Layout

## 1. Chat Window Container
- **Positioning:** Centered on the page, both vertically and horizontally.
- **Size:**
  - Width: 60% of the viewport width (responsive).
  - Height: 80% of the viewport height (responsive).
- **Background:** Light gray (`#f5f5f5`).
- **Border:** Subtle shadow for depth, e.g., `box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1)`.
- **Border Radius:** Rounded corners with 12px.
- **Padding:** Internal padding of 20px.

## 2. Header Section
- **Position:** Fixed at the top of the chat window.
- **Height:** 60px.
- **Background:** White (`#ffffff`).
- **Border:** Bottom border with a soft gray line (`1px solid #eaeaea`).
- **Content:** Centered text showing "PA" (or another customizable title).
- **Font Size:** 18px.
- **Font Weight:** 600.
- **Text Alignment:** Centered.
- **Icons (Optional):** Add a settings icon or a menu dropdown on the right corner.

## 3. Chat Area (Message Display)
- **Position:** Below the header, taking up most of the container height.
- **Scrolling:** Enable vertical scrolling for messages.
  - CSS: `overflow-y: auto;`.
- **Background:** Inherit from the container.

### Messages Layout:
- **User Message:**
  - **Alignment:** Right-aligned.
  - **Background:** Blue (`#007bff`) with white text.
  - **Padding:** 10px 15px.
  - **Border Radius:** Rounded corners (15px for all sides, except bottom-right: 5px).
  - **Margin:** 10px.
  - **Maximum Width:** 60% of the container width.
  - **Font Size:** 14px.

- **AI Response:**
  - **Alignment:** Left-aligned.
  - **Background:** White (`#ffffff`) with black text.
  - **Padding:** Same as user messages.
  - **Border Radius:** Rounded corners (15px for all sides, except bottom-left: 5px).
  - **Margin:** Same as user messages.
  - **Maximum Width:** Same as user messages.
  - **Border:** Subtle border (`1px solid #eaeaea`).
  - **Font Size:** 14px.

## 4. Input Section
- **Position:** Fixed at the bottom of the chat window.
- **Height:** 70px.
- **Background:** White (`#ffffff`).
- **Border:** Top border with a soft gray line (`1px solid #eaeaea`).

### Content:
- **Input Box:**
  - **Type:** Multiline text box (textarea).
  - **Width:** 85% of the container.
  - **Height:** 45px.
  - **Border:** Subtle border (`1px solid #eaeaea`).
  - **Border Radius:** 8px.
  - **Padding:** 10px.
  - **Font Size:** 14px.
  - **Placeholder Text:** "Type your message here..."

- **Send Button:**
  - **Position:** Aligned to the right of the input box.
  - **Shape:** Rounded rectangle.
  - **Size:** 50px x 45px.
  - **Background:** Green (`#28a745`).
  - **Icon:** Send icon (use a paper plane icon from a library like Font Awesome or a simple arrow).

### Interaction:
- **Hover Effect:** Slightly darker green background.
- **Click Effect:** Subtle shrinking animation.

## Functionality

### Backend
- Use Flask to define an endpoint `/chat` to handle AJAX or WebSocket requests for sending and receiving messages. or User `/routes.py`


### Frontend
- Use JavaScript (preferably Vanilla JS or a lightweight framework like Alpine.js) for handling input submission and rendering responses dynamically.
- Add an event listener to:
  - Detect the "Enter" keypress to submit the message.
  - Clear the input field after a message is sent.
- Use AJAX (or WebSocket) to fetch AI responses and render them in the chat area.

### Styling
- Use CSS or a preprocessor like SCSS for consistent styles.
- Include responsive design using media queries for mobile devices:
  - On smaller screens, reduce the width of the chat window to 90% and increase the height to fit content.