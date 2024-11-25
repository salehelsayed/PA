document.addEventListener('DOMContentLoaded', function() {
    const directoryTree = document.getElementById('directory-tree');
    const browseButton = document.getElementById('browse-button');
    const directoryInput = document.getElementById('directory-input');

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

        // Build directory structure
        sortedFiles.forEach(file => {
            const path = file.webkitRelativePath;
            const parts = path.split('/');
            let currentLevel = directoryData;

            parts.forEach((part, index) => {
                if (index === 0) return; // Skip the root folder name

                let existingPath = currentLevel.find(item => item.name === part);
                if (!existingPath) {
                    existingPath = {
                        name: part,
                        type: index === parts.length - 1 ? 'file' : 'directory',
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
                item.innerHTML = `
                    <div class="file-item">
                        <div class="file-icon">
                            <i class="fas fa-file-alt"></i>
                        </div>
                        <span class="file-name">${node.name}</span>
                    </div>
                `;
            }
            parentElement.appendChild(item);
        });
    }
}); 