function loadNotes() {

    window.pywebview.api.get_notes().then(function (notes) {

        var notesDiv = document.getElementById('notes');
        if (!notesDiv) {
            alert("Element with id 'notes' not found!");
            return;
        }
        
        notesDiv.innerHTML = '';
        notes.forEach(function (note) {
            var noteDiv = document.createElement('div');
            noteDiv.className = 'note';
            noteDiv.innerText = note.content;
            notesDiv.appendChild(noteDiv);
        });
    });
}
function addNote() {
    var content = document.getElementById('noteContent').value;
    if (content.trim() === '') {
        alert('Please enter a note.');
        return;
    }
    window.pywebview.api.add_note(content).then(function (response) {
        if (response.error) {
            alert(response.error);
        } else {
            alert("noteContent");
            document.getElementById('noteContent').value = '';
            loadNotes();
        }
    });
}
window.addEventListener('pywebviewready', function () {
    loadNotes();
});

function navigateToAllNotes() {
        location.href = 'all-notes.html';
}
function navigateToHome() {
        location.href = 'index.html';
}
