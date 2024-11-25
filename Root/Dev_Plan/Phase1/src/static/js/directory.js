document.addEventListener('DOMContentLoaded', function() {
    const directoryTree = document.getElementById('directory-tree');
    const browseButton = document.getElementById('browse-button');
    const directoryInput = document.getElementById('directory-input');

    // Map to store file paths to file objects
    const fileMap = {};

    // Event listener for the "Load Directory" button
    browseButton.addEventListener('click', () => {
        directoryInput.click();
    });

    directoryInput.addEventListener('change', (event) => {
        const files = event.target.files;
        const directoryData = [];

        // Convert FileList to array and sort it
        const sortedFiles = Array.from(files).sort((a, b) => {
            // Directories come first
            const aIsDir = a.webkitRelativePath.split('/').length > 2;
            const bIsDir = b.webkitRelativePath.split('/').length > 2;
            if (aIsDir && !bIsDir) return -1;
            if (!aIsDir && bIsDir) return 1;
            return a.webkitRelativePath.localeCompare(b.webkitRelativePath);
        });

        // Build directory structure and populate fileMap
        sortedFiles.forEach(file => {
            const path = file.webkitRelativePath;
            fileMap[path] = file; // Store the file object in the map

            const parts = path.split('/');
            let currentLevel = directoryData;

            parts.forEach((part, index) => {
                if (index === 0) return; // Skip the root folder name

                let existingPath = currentLevel.find(item => item.name === part);
                if (!existingPath) {
                    existingPath = {
                        name: part,
                        type: index === parts.length - 1 ? 'file' : 'directory',
                        path: path,
                        children: []
                    };
                    currentLevel.push(existingPath);
                }
                currentLevel = existingPath.children;
            });
        });

        // Clear existing directory tree
        directoryTree.innerHTML = '';
        // Build the directory tree
        buildDirectoryTree(directoryData, directoryTree);
    });

    function buildDirectoryTree(nodes, parentElement) {
        nodes.forEach(node => {
            const item = document.createElement('div');
            item.classList.add('directory-item');

            if (node.type === 'directory') {
                const header = document.createElement('div');
                header.classList.add('directory-header');
                header.innerHTML = `
                    <div class="directory-icon">
                        <i class="fas fa-chevron-right"></i>
                        <i class="fas fa-folder"></i>
                    </div>
                    <span class="directory-name">${node.name}</span>
                `;
                item.appendChild(header);

                const childrenContainer = document.createElement('div');
                childrenContainer.classList.add('children-container');
                childrenContainer.style.display = 'none';
                item.appendChild(childrenContainer);

                header.addEventListener('click', (e) => {
                    e.stopPropagation();
                    const chevron = header.querySelector('.fa-chevron-right');
                    const folder = header.querySelector('.fa-folder');
                    
                    if (childrenContainer.style.display === 'none') {
                        childrenContainer.style.display = 'block';
                        chevron.style.transform = 'rotate(90deg)';
                        folder.classList.replace('fa-folder', 'fa-folder-open');
                    } else {
                        childrenContainer.style.display = 'none';
                        chevron.style.transform = 'rotate(0deg)';
                        folder.classList.replace('fa-folder-open', 'fa-folder');
                    }
                });

                buildDirectoryTree(node.children, childrenContainer);
            } else {
                const fileItem = document.createElement('div');
                fileItem.classList.add('file-item');
                fileItem.innerHTML = `
                    <div class="file-icon">
                        <i class="fas fa-file-alt"></i>
                    </div>
                    <span class="file-name">${node.name}</span>
                `;
                fileItem.addEventListener('click', () => {
                    viewFileContent(node.path);
                });
                item.appendChild(fileItem);
            }
            parentElement.appendChild(item);
        });
    }

    function viewFileContent(filePath) {
        const file = findFileByPath(filePath);

        if (file) {
            const reader = new FileReader();
            reader.onload = function(event) {
                const content = event.target.result;
                displayFileContent(content, file.name);
            };
            reader.readAsText(file);
        } else {
            alert('File not found.');
        }
    }

    // Implement the findFileByPath function
    function findFileByPath(filePath) {
        return fileMap[filePath];
    }

    function displayFileContent(content, fileName) {
        document.getElementById('chat-view').style.display = 'none';
        document.getElementById('file-view').style.display = 'block';

        document.getElementById('file-name').textContent = fileName;

        const fileContentElement = document.getElementById('file-content');
        fileContentElement.innerHTML = marked.parse(content);
    }

    document.getElementById('back-to-chat').addEventListener('click', () => {
        document.getElementById('chat-view').style.display = 'block';
        document.getElementById('file-view').style.display = 'none';
    });
}); 