# Main Screen UI Detailed Description

## Overview

The main screen of the application features a responsive user interface divided into two primary sections:

1. **Sidebar**: Located on the left, displaying a directory tree structure.
2. **Chat Window**: On the right, providing an interactive chat interface with the AI assistant.

The layout is built using CSS Flexbox to ensure responsiveness and adaptability across various screen sizes.

---

## Layout Structure

### Main Container

- **Element**: `<div class="main-container">`
- **Description**: Serves as the primary wrapper encompassing both the sidebar and chat window.
- **Styles**:
  - **Display**: `flex`
  - **Flex Direction**: `row` (default)
  - **Width**: `100%`
  - **Height**: `100%`
  - **Background Color**: `#f5f5f5`
  - **Font Family**: `Arial, sans-serif`
  - **Border Radius**: `0`
  - **Box Shadow**: `none`

---

### Sidebar

- **Element**: `<div class="sidebar">`
- **Description**: Contains the directory navigation and controls.
- **Styles**:
  - **Width**: `250px`
  - **Background Color**: `#ffffff`
  - **Padding**: `20px`
  - **Border Right**: `1px solid #eaeaea`
  - **Border Radius**: `12px 0 0 12px`

#### Sidebar Header

- **Element**: `<div class="sidebar-header">`
- **Description**: Header containing the title and directory loading button.
- **Components**:
  - **Title**: `<h5>Directory</h5>`
    - **Font Size**: `14px`
    - **Font Weight**: `600`
    - **Color**: `#24292e`
    - **Margin**: `0`
  - **Load Directory Button**: `<button id="browse-button" class="button">Load Directory</button>`
    - **Padding**: `5px 12px`
    - **Font Size**: `12px`
    - **Font Weight**: `500`
    - **Border Radius**: `6px`
    - **Background Color**: `#f6f8fa`
    - **Border**: `1px solid rgba(27,31,36,0.15)`
    - **Color**: `#24292e`
    - **Hover Effect**: Background changes to `#f3f4f6`

#### Directory Tree

- **Element**: `<div id="directory-tree" class="directory-tree">`
- **Description**: Displays the hierarchical file and directory structure.
- **Styles**:
  - **Font Size**: `14px`
  - **Color**: `#24292e`
  - **Padding**: `10px 0`

---

### Chat Window

- **Element**: `<div class="chat-window">`
- **Description**: Contains the chat interface components.
- **Styles**:
  - **Flex**: `1` (fills the remaining space)
  - **Display**: `flex`
  - **Flex Direction**: `column`
  - **Position**: `relative`
  - **Background Color**: `#ffffff`
  - **Border Radius**: `0 12px 12px 0`

#### Header

- **Element**: `<div class="header">`
- **Description**: Fixed header displaying the application name.
- **Content**: `PA` (Replace with actual application name)
- **Styles**:
  - **Height**: `60px`
  - **Background Color**: `#ffffff`
  - **Border Bottom**: `1px solid #eaeaea`
  - **Display**: `flex`
  - **Align Items**: `center`
  - **Justify Content**: `center`
  - **Font Size**: `18px`
  - **Font Weight**: `600`
  - **Position**: `sticky`
  - **Top**: `0`
  - **Z-Index**: `10`

#### Chat Area

- **Element**: `<div class="chat-area" id="chat-container">`
- **Description**: Scrollable area where messages are displayed.
- **Styles**:
  - **Flex**: `1`
  - **Overflow-Y**: `auto` (enables vertical scrolling)
  - **Padding**: `20px`
  - **Display**: `flex`
  - **Flex Direction**: `column`
  - **Background Color**: `#f5f5f5`

#### Input Section

- **Element**: `<div class="input-section">`
- **Description**: Contains the message input field and send button.
- **Styles**:
  - **Height**: `70px`
  - **Background Color**: `#ffffff`
  - **Border Top**: `1px solid #eaeaea`
  - **Padding**: `12px 20px`
  - **Position**: `sticky` (fixed at the bottom)
  - **Bottom**: `0`

##### Chat Form

- **Element**: `<form id="chat-form">`
- **Description**: Form containing the input and submit elements.
- **Styles**:
  - **Display**: `flex`
  - **Gap**: `10px`
  - **Height**: `100%`

###### User Input

- **Element**: `<textarea id="user-input" placeholder="Type your message here..." autocomplete="off" required></textarea>`
- **Styles**:
  - **Flex**: `1`
  - **Padding**: `10px`
  - **Border**: `1px solid #eaeaea`
  - **Border Radius**: `8px`
  - **Font Size**: `14px`
  - **Resize**: `none`

###### Send Button

- **Element**: `<button type="submit" class="button"><i class="fas fa-paper-plane"></i></button>`
- **Styles**:
  - **Width**: `50px`
  - **Height**: `45px`
  - **Background Color**: `#28a745` (green)
  - **Border**: `none`
  - **Border Radius**: `8px`
  - **Display**: `flex`
  - **Align Items**: `center`
  - **Justify Content**: `center`
  - **Cursor**: `pointer`
  - **Transition**: `background-color 0.2s, transform 0.1s`
  - **Hover Effect**: Background changes to `#218838`
  - **Active Effect**: Scales down slightly (`transform: scale(0.95)`)

---

## Message Styling

### Message Container

- **Element**: `<div class="message [user|ai]">`
- **Description**: Wrapper for individual messages. Use `user` or `ai` class to differentiate.
- **Common Styles**:
  - **Max Width**: `60%` (of chat area)
  - **Margin**: `10px`
  - **Padding**: `10px 15px`
  - **Font Size**: `14px`
  - **Border Radius**: `15px`
  - **White Space**: `pre-wrap` (preserves whitespace)
  - **Line Height**: `1.5`

#### User Messages

- **Class**: `message user`
- **Styles**:
  - **Align Self**: `flex-end` (right side)
  - **Background Color**: `#007bff` (blue)
  - **Color**: `#ffffff` (white text)
  - **Border Bottom Right Radius**: `5px` (sharper corner)

#### AI Messages

- **Class**: `message ai`
- **Styles**:
  - **Align Self**: `flex-start` (left side)
  - **Background Color**: `#ffffff`
  - **Color**: `#000000`
  - **Border**: `1px solid #eaeaea`
  - **Border Bottom Left Radius**: `5px` (sharper corner)

### Message Content

- **Element**: `<div class="message-content">`
- **Description**: Contains the text, supports Markdown formatting.
- **Styles**:
  - **Font Size**: `14px`
  - **Line Height**: `1.5`

#### Code Blocks in Messages

- **Elements**: `<pre>`, `<code>`
- **Styles**:
  - **`<pre>`**:
    - **Background Color**: `#f6f8fa`
    - **Padding**: `12px`
    - **Border Radius**: `8px`
    - **Overflow-X**: `auto` (horizontal scrolling)
    - **Margin**: `8px 0`
  - **`<code>`**:
    - **Background Color**: `#f6f8fa`
    - **Padding**: `2px 4px`
    - **Border Radius**: `4px`
    - **Font Family**: `monospace`

---

## Directory Tree

### Structure

- **Element**: `<div class="directory-tree">`
- **Description**: Represents the file system hierarchy.
- **Styles**:
  - **Font Size**: `14px`
  - **Color**: `#24292e`

### Directory Item

- **Element**: `<div class="directory-item">`
- **Description**: Each item can be a file or a directory.
- **Styles**:
  - **Position**: `relative`

### Directory Header

- **Element**: `<div class="directory-header">`
- **Description**: Represents a directory with expandable functionality.
- **Components**:
  - **Chevron Icon**: `<i class="fas fa-chevron-right">`
    - **Font Size**: `12px`
    - **Transition**: `transform 0.2s`
  - **Folder Icon**: `<i class="fas fa-folder">` or `<i class="fas fa-folder-open">`
    - **Color**: `#54aeff`
  - **Directory Name**: `<span class="directory-name">`

### File Item

- **Element**: `<div class="file-item">`
- **Components**:
  - **File Icon**: `<i class="fas fa-file-alt">`
    - **Color**: `#6a737d`
  - **File Name**: `<span class="file-name">`

### Interaction

- **Expandable Directories**:
  - Clicking on a directory header toggles the display of its children.
  - **Animation**: Chevron rotates 90 degrees upon expansion.
  - **Folder Icon Change**: Swaps between `fa-folder` and `fa-folder-open`.

---

## Responsive Design

- **Media Query**: `@media (max-width: 768px)`
- **Adjustments**:
  - **Main Container**:
    - **Width**: `90vw`
    - **Height**: `90vh`
    - **Flex Direction**: `column`
  - **Sidebar**:
    - **Width**: `100%`
    - **Height**: `auto`
    - **Border Radius**: `12px 12px 0 0`
    - **Border Right**: `none`
    - **Border Bottom**: `1px solid #eaeaea`
  - **Chat Window**:
    - **Border Radius**: `0 0 12px 12px`
  - **Message Max Width**:
    - **Adjusts to**: `80%` (wider messages)

---

## Fonts and Icons

- **Font Family**: Applied globally as `Arial, sans-serif`.
- **Icon Library**: Font Awesome (used via CDN).
  - **Usage**:
    - **Navigation Icons**: Folders, files, chevrons.
    - **Button Icons**: Paper plane icon for the send button.

---

## JavaScript Functionality

### Chat Interaction (`chat.js`)

- **File**: `static/js/chat.js`
- **Features**:
  - Captures user input and sends it to the server via a POST request to `/chat`.
  - Displays both user and AI messages in the chat area.
  - Supports submitting messages on pressing Enter (without Shift) or clicking the send button.
  - Utilizes the Marked.js library to render AI responses with Markdown formatting.

### Directory Tree Interaction (`directory.js`)

- **File**: `static/js/directory.js`
- **Features**:
  - Allows users to load a directory using the "Load Directory" button.
  - Builds a hierarchical directory structure from the selected directory.
  - Handles expanding and collapsing of directories with smooth transitions.
  - Implements sorting to display directories before files.

---

## Template Structure

- **Base Template**: `templates/base.html`
  - Includes links to external CSS and JS resources (Bootstrap, Marked.js).
  - Sets up the basic HTML structure with `{% block %}` tags for extension.

- **Index Page**: `templates/index.html`
  - Extends the base template.
  - Incorporates the main UI components via `{% include %}`:
    - **Sidebar**: `components/sidebar.html`
    - **Header**: `components/header.html`
    - **Chat Area**: `components/chat_area.html`
    - **Input Section**: `components/input_section.html`

---

## Color Scheme and Styling

- **Primary Colors**:
  - **Backgrounds**: `#ffffff` (white), `#f5f5f5` (light gray), `#f0f2f5`
  - **Borders**: `#eaeaea` (light border), `#e1e4e8`
  - **Text**: `#24292e` (dark gray), `#000000` (black)
  - **Buttons**: `#28a745` (green), `#007bff` (blue for user messages)

- **Button States**:
  - **Hover**: Slight change in background color for interactive feedback.
  - **Active**: Visual indication when buttons are pressed.

---

## Accessibility Considerations

- **Keyboard Navigation**:
  - Input field focuses on page load.
  - Users can navigate using the `Tab` key.
- **ARIA Roles and Attributes**:
  - Ensure that interactive elements are properly labeled for assistive technologies.
- **Contrast Ratios**:
  - Text and background colors chosen to meet accessibility standards.

---

## Additional Notes

- **Session Management**:
  - User-selected directories are stored in the session for persistence.
- **Security**:
  - Server-side validation to prevent unauthorized file access.
  - Sanitization of user inputs to prevent XSS attacks.
- **Dependencies**:
  - **Flask**: Python web framework.
  - **OpenAI API**: For AI assistant responses.
  - **Font Awesome**: Icon library.
  - **Marked.js**: Markdown parsing in the chat messages.

---

## Conclusion

This detailed description provides all the necessary information for a developer to recreate the main screen UI exactly as specified. It covers the structure, styling, interactivity, and functionalities of each component within the interface.
