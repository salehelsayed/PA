# Feature Implementation Plan: Viewing File Content in the Left Window

---

## Overview

**Objective**: Enhance the application by allowing users to click on files in the directory tree (displayed in the sidebar) and view the content of those files (specifically `.md` and `.txt` files) within the left window. When a file is selected:

- The **chat window** on the right should disappear.
- The **file content** should be displayed in its place.
- Users can return to the chat interface easily.

This plan outlines the steps and code modifications required to implement this feature without disrupting the existing functionality.

---

## Implementation Steps

### 1. **Update the Directory Tree to Handle File Click Events**

#### **1.1 Modify `directory.js`**

- **Add Event Listeners to File Items**: In the `buildDirectoryTree` function, attach a click event to each file item to handle file selection.

  ```javascript:Root/Dev_Plan/Phase1/src/static/js/directory.js
  // ... existing code ...

  function buildDirectoryTree(nodes, parentElement) {
      nodes.forEach(node => {
          const item = document.createElement('div');
          item.classList.add('directory-item');

          if (node.type === 'directory') {
              // ... existing code for directories ...
              buildDirectoryTree(node.children, childrenContainer);
          } else {
              // Create file item
              const fileItem = document.createElement('div');
              fileItem.classList.add('file-item');
              fileItem.innerHTML = `
                  <div class="file-icon">
                      <i class="fas fa-file-alt"></i>
                  </div>
                  <span class="file-name">${node.name}</span>
              `;
              // Add click event listener
              fileItem.addEventListener('click', () => {
                  viewFileContent(node.path);
              });
              item.appendChild(fileItem);
          }
          parentElement.appendChild(item);
      });
  }
  ```

- **Update Data Structure to Include File Paths**: Ensure each file node includes a relative `path` property.

#### **1.2 Update Backend Data Structure**

- **Modify the `/api/directory` Endpoint in `routes.py`**:

  ```python:Root/Dev_Plan/Phase1/src/chat/routes.py
  # ... existing code ...

  def get_directory_structure(path, base_path):
      structure = []
      try:
          with os.scandir(path) as it:
              for entry in it:
                  if entry.name.startswith('.'):
                      continue  # Skip hidden files and directories
                  relative_path = os.path.relpath(entry.path, base_path)
                  if entry.is_dir(follow_symlinks=False):
                      structure.append({
                          'type': 'directory',
                          'name': entry.name,
                          'path': relative_path,
                          'children': get_directory_structure(entry.path, base_path)
                      })
                  else:
                      structure.append({
                          'type': 'file',
                          'name': entry.name,
                          'path': relative_path
                      })
          return structure
      except PermissionError:
          return []

  # Update the route to pass base_directory
  @chat_bp.route('/api/directory', methods=['POST'])
  def get_directory():
      # ... existing code ...
      directory_structure = get_directory_structure(base_directory, base_directory)
      return jsonify(directory_structure)
  ```

---

### 2. **Create a File View Component**

#### **2.1 Modify `index.html` to Include the File View**

- **Adjust the Layout**:

  ```html:Root/Dev_Plan/Phase1/src/templates/index.html
  {% extends 'base.html' %}

  {% block content %}
  <div class="main-container">
      <!-- Sidebar -->
      {% include 'components/sidebar.html' %}

      <!-- Content Area -->
      <div class="content-area">
          <!-- Chat View -->
          <div id="chat-view">
              {% include 'components/header.html' %}
              {% include 'components/chat_area.html' %}
              {% include 'components/input_section.html' %}
          </div>
          <!-- File View -->
          <div id="file-view" style="display: none;">
              {% include 'components/file_view.html' %}
          </div>
      </div>
  </div>
  {% endblock %}
  ```

#### **2.2 Create `file_view.html` Component**

- **Create the File View Template**:

  ```html:Root/Dev_Plan/Phase1/src/templates/components/file_view.html
  <div class="file-view-container">
      <div class="file-header">
          <button id="back-to-chat" class="button">Back to Chat</button>
          <h2 id="file-name"></h2>
      </div>
      <div id="file-content" class="file-content">
          <!-- File content will be rendered here -->
      </div>
  </div>
  ```

---

### 3. **Style the File View Component**

#### **3.1 Update `styles.css`**

- **Add Styles for the File View**:

  ```css:Root/Dev_Plan/Phase1/src/static/css/styles.css
  /* ... existing code ... */

  .content-area {
      flex: 1;
      display: flex;
      flex-direction: column;
      position: relative;
      background-color: #ffffff;
      border-radius: 0 12px 12px 0;
      overflow: hidden;
  }

  /* File View Container */
  .file-view-container {
      display: flex;
      flex-direction: column;
      height: 100%;
  }

  .file-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 20px;
      border-bottom: 1px solid #eaeaea;
  }

  .file-header #back-to-chat {
      padding: 5px 12px;
      font-size: 14px;
      background-color: #f6f8fa;
      border: 1px solid rgba(27,31,36,0.15);
      border-radius: 6px;
      color: #24292e;
      cursor: pointer;
  }

  .file-content {
      flex: 1;
      padding: 20px;
      overflow-y: auto;
      background-color: #fff;
  }

  .file-content h1, .file-content h2, .file-content h3 {
      margin-top: 24px;
      margin-bottom: 16px;
      font-weight: 600;
  }

  .file-content p {
      margin-bottom: 16px;
  }

  .file-content pre, .file-content code {
      background-color: #f6f8fa;
      padding: 12px;
      border-radius: 8px;
      overflow-x: auto;
  }

  /* ... existing code ... */
  ```

---

### 4. **Implement JavaScript Logic to Handle File Viewing**

#### **4.1 Update `directory.js`**

- **Add Functions to Handle File Content Display**:

  ```javascript:Root/Dev_Plan/Phase1/src/static/js/directory.js
  // ... existing code ...

  function viewFileContent(filePath) {
      fetch(`/api/file?file_path=${encodeURIComponent(filePath)}`)
          .then(response => response.json())
          .then(data => {
              if (data.content) {
                  // Display the file content
                  displayFileContent(data.content, filePath);
              } else {
                  alert(data.error || 'Failed to load file content.');
              }
          })
          .catch(error => {
              console.error('Error:', error);
              alert('An error occurred while loading the file content.');
          });
  }

  function displayFileContent(content, fileName) {
      // Hide chat view and show file view
      document.getElementById('chat-view').style.display = 'none';
      document.getElementById('file-view').style.display = 'block';

      // Set the file name
      document.getElementById('file-name').textContent = fileName;

      // Render the content (supports Markdown)
      const fileContentElement = document.getElementById('file-content');
      fileContentElement.innerHTML = marked.parse(content);
  }

  // Event listener for 'Back to Chat' button
  document.getElementById('back-to-chat').addEventListener('click', () => {
      // Show chat view and hide file view
      document.getElementById('chat-view').style.display = 'block';
      document.getElementById('file-view').style.display = 'none';
  });
  ```

---

### 5. **Enhance Backend to Serve File Content**

#### **5.1 Ensure Safe File Access in `routes.py`**

- **Modify the `/api/file` Endpoint**:

  ```python:Root/Dev_Plan/Phase1/src/chat/routes.py
  @chat_bp.route('/api/file', methods=['GET'])
  def read_file():
      file_path = request.args.get('file_path')
      base_directory = session.get('selected_directory')

      if not file_path or not base_directory:
          return jsonify({'error': 'File path not provided.'}), 400

      # Resolve the absolute path
      absolute_path = os.path.abspath(os.path.join(base_directory, file_path))

      # Security check to prevent access outside the base directory
      if not absolute_path.startswith(base_directory):
          return jsonify({'error': 'Access to the specified file is not allowed.'}), 403

      if not os.path.exists(absolute_path):
          return jsonify({'error': 'File not found.'}), 404

      try:
          with open(absolute_path, 'r', encoding='utf-8') as file:
              content = file.read()
      except Exception as e:
          current_app.logger.error(f"Error reading file {absolute_path}: {e}")
          return jsonify({'error': 'An error occurred while reading the file.'}), 500

      return jsonify({'content': content})
  ```

---

### 6. **Update the Directory Structure Data**

#### **6.1 Include Relative Paths for Files and Directories**

- **Ensure `path` is Relative**:

  In `get_directory_structure` function:

  ```python
  relative_path = os.path.relpath(entry.path, base_path)
  ```

- **Pass the `base_path` when Recursing**:

  ```python
  'children': get_directory_structure(entry.path, base_path)
  ```

---

### 7. **Ensure Dependencies are Included**

#### **7.1 Confirm Marked.js is Loaded**

- **In `base.html` or `index.html`**:

  ```html
  <!-- Include Marked.js -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  ```

#### **7.2 Ensure Font Awesome is Available**

- **Icons for Files and Directories**:

  ```html
  <!-- Include Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  ```

---

## Additional Considerations

### **Error Handling and User Feedback**

- **Loading Indicators**: Consider adding a loading spinner when fetching file content.
- **Error Messages**: Provide user-friendly error messages in case of failures.

### **Security Measures**

- **Prevent Directory Traversal**: Always validate and sanitize file paths on the server side.
- **Session Management**: Ensure the user's selected directory is securely stored and accessed.

### **File Types Support**

- **Supported Formats**: Currently supports `.md` and `.txt` files.
- **Unsupported Files**: Handle unsupported file types gracefully (e.g., display a message).

### **User Experience Enhancements**

- **Remember Scroll Positions**: Maintain the scroll position of the directory tree and file content when switching views.
- **Responsive Design**: Ensure the new components are responsive and work well on different screen sizes.

---

## Conclusion

By carefully following this implementation plan, you can add the new feature without disrupting the existing application. The plan ensures that:

- The directory tree remains functional.
- The chat functionality is preserved.
- Users can seamlessly view file contents and return to the chat interface.

--- 