document.addEventListener('DOMContentLoaded', function() {
    const directoryTree = document.getElementById('directory-tree');
    const browseButton = document.getElementById('browse-button');
    const directoryInput = document.getElementById('directory-input');

    // Load directory structure from localStorage if available
    const storedDirectoryData = localStorage.getItem('directoryData');
    if (storedDirectoryData) {
        const directoryData = JSON.parse(storedDirectoryData);
        buildDirectoryTree(directoryData, directoryTree);
    }

    // Set up event listener for the "Load Directory" button
    browseButton.addEventListener('click', () => {
        directoryInput.click();
    });

    directoryInput.addEventListener('change', (event) => {
        const files = event.target.files;
        const directoryData = [];

        [...files].forEach(file => {
            const path = file.webkitRelativePath || file.relativePath || file.name;
            const parts = path.split('/');
            let currentLevel = directoryData;

            parts.forEach((part, index) => {
                let existingPath = currentLevel.find(item => item.name === part);
                if (!existingPath) {
                    existingPath = {
                        name: part,
                        type: (index === parts.length - 1 && file.type) ? 'file' : 'directory',
                        children: []
                    };
                    currentLevel.push(existingPath);
                }
                currentLevel = existingPath.children;
            });
        });

        // Store directory data in localStorage
        localStorage.setItem('directoryData', JSON.stringify(directoryData));

        // Clear existing directory tree
        directoryTree.innerHTML = '';
        // Build the directory tree
        buildDirectoryTree(directoryData, directoryTree);
    });

    // Function to build the directory tree recursively
    function buildDirectoryTree(nodes, parentElement) {
        nodes.forEach(node => {
            const item = document.createElement('div');
            item.classList.add('directory-item');

            if (node.type === 'directory') {
                item.innerHTML = `
                    <div class="directory-header">
                        <i class="fas fa-folder"></i>
                        <span class="directory-name">${node.name}</span>
                    </div>
                `;
                parentElement.appendChild(item);

                const childrenContainer = document.createElement('div');
                childrenContainer.classList.add('children-container');
                childrenContainer.style.display = 'none';
                parentElement.appendChild(childrenContainer);

                item.querySelector('.directory-header').addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (childrenContainer.style.display === 'none') {
                        childrenContainer.style.display = 'block';
                    } else {
                        childrenContainer.style.display = 'none';
                    }
                });

                buildDirectoryTree(node.children, childrenContainer);

            } else if (node.type === 'file') {
                item.innerHTML = `
                    <div class="file-item">
                        <i class="fas fa-file"></i>
                        <span class="file-name">${node.name}</span>
                    </div>
                `;
                parentElement.appendChild(item);
            }
        });
    }
}); 