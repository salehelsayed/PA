# Test Cases

---

## Feature 1: Chat Interface

---

### Description

Allows users to interact with the AI assistant by sending messages and receiving responses.

### Test Cases

#### Positive Tests

1. **Sending a Valid Message**

   - **Steps**:
     - Enter "Hello, how are you?" into the input field.
     - Press Enter or click the Send button.
   - **Expected Result**: The message appears in the chat; the AI responds appropriately.

2. **Handling Markdown Content**

   - **Steps**:
     - Enter a message containing Markdown, e.g., "Can you explain `code`?"
   - **Expected Result**: The AI's response renders any Markdown correctly.

#### Negative Tests

1. **Empty Message Submission**

   - **Steps**:
     - Press Enter without typing a message.
   - **Expected Result**: Message is not sent; possibly an alert prompts the user to enter text.

2. **Excessive Message Length**

   - **Steps**:
     - Paste a very long text (e.g., 10,000 characters) into the input field.
     - Attempt to send.
   - **Expected Result**: The application handles it gracefully, possibly truncating the message or showing an error.

#### Boundary Tests

1. **Maximum Allowed Characters**

   - **Steps**:
     - Input text at the character limit (e.g., 500 characters).
     - Send the message.
   - **Expected Result**: Message is sent successfully.

---

## Feature 2: Directory Loading and Navigation

---

### Description

Enables users to load a local directory and navigate its structure.

### Test Cases

#### Positive Tests

1. **Loading a Directory**

   - **Steps**:
     - Click "Load Directory".
     - Select a folder containing subfolders and files.
   - **Expected Result**: Directory tree displays correctly with all folders and files.

2. **Navigating Folders**

   - **Steps**:
     - Click on folder icons to expand and collapse them.
   - **Expected Result**: Folders expand/collapse smoothly; child items are shown/hidden.

#### Negative Tests

1. **Unsupported Browser**

   - **Steps**:
     - Use a browser that doesn't support `webkitdirectory` (e.g., Internet Explorer).
     - Try to load a directory.
   - **Expected Result**: The "Load Directory" button is disabled or an informative message is displayed.

2. **Cancelling Directory Selection**

   - **Steps**:
     - Click "Load Directory" but cancel the selection dialog.
   - **Expected Result**: No changes occur; application remains stable.

#### Boundary Tests

1. **Large Number of Files**

   - **Steps**:
     - Load a directory with thousands of files.
   - **Expected Result**: Application remains responsive; directory tree is built correctly.

---

## Feature 3: File Content Viewing

---

### Description

Displays the content of selected files, replacing the chat interface.

### Test Cases

#### Positive Tests

1. **Viewing a Markdown File**

   - **Steps**:
     - Click on a `.md` file in the directory tree.
   - **Expected Result**: File content is displayed with proper Markdown rendering.

2. **Using "Back to Chat"**

   - **Steps**:
     - After viewing a file, click "Back to Chat".
   - **Expected Result**: Chat interface is restored with previous messages intact.

#### Negative Tests

1. **Viewing an Unsupported File Type**

   - **Steps**:
     - Click on a file with an unsupported extension (e.g., `.exe`).
   - **Expected Result**: Application ignores the click or shows a message indicating unsupported file type.

2. **File Not Found**

   - **Steps**:
     - Delete a file from the directory after loading it in the app.
     - Attempt to view the deleted file.
   - **Expected Result**: An error message indicates the file cannot be found.

#### Boundary Tests

1. **Large File Size**

   - **Steps**:
     - Open a text file larger than 10MB.
   - **Expected Result**: Application handles the file gracefully, possibly with a loading indicator.

---

## Feature 4: Responsive Design

---

### Description

Ensures the application functions well on various screen sizes.

### Test Cases

#### Positive Tests

1. **Mobile Portrait Mode**

   - **Steps**:
     - Open the application on a mobile device in portrait orientation.
   - **Expected Result**: Layout adjusts; all features remain accessible.

2. **Tablet Landscape Mode**

   - **Steps**:
     - Open the application on a tablet in landscape orientation.
   - **Expected Result**: Layout utilizes wider screen effectively.

#### Negative Tests

1. **Very Small Screen Size**

   - **Steps**:
     - Resize the browser to a very small window (e.g., 300px width).
   - **Expected Result**: Application displays a minimal viable interface or prompts to enlarge the window.

---

## Feature 5: User Experience Enhancements

---

### Description

Enhances usability through keyboard shortcuts and visual feedback.

### Test Cases

#### Positive Tests

1. **Submitting with Enter Key**

   - **Steps**:
     - Type a message and press Enter.
   - **Expected Result**: Message is sent without needing to click the Send button.

2. **Hover Effects on Buttons**

   - **Steps**:
     - Hover over interactive elements like buttons and links.
   - **Expected Result**: Visual feedback indicates interactivity (e.g., color change).

#### Negative Tests

1. **Keyboard Navigation**

   - **Steps**:
     - Navigate the application using only the keyboard (Tab key).
   - **Expected Result**: Focus indicators are visible; interactive elements are accessible.

--- 