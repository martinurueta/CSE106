
document.addEventListener('DOMContentLoaded', () => {
    const addUserButton = document.getElementById('add-user-button');
    const addUserModal = document.getElementById('add-user-modal');
    const addUserForm = document.getElementById('add-user-form');

    // Open the Add User modal
    addUserButton.addEventListener('click', () => {
        addUserModal.style.display = 'block';
    });


    // Handle the Add User form submission
    addUserForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(event.target);
        fetch('/add_user', {
            method: 'POST',
            body: formData,
        }).then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Error adding user');
            }
        });
    });
    const deleteButtons = document.querySelectorAll('[id^="delete-user-"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', () => {
            const userId = button.getAttribute('data-id');
            const formData = new FormData();
            formData.append('user_id', userId);

            fetch('/delete_user', {
                method: 'POST',
                body: formData,
            }).then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Error deleting user');
                }
            });
        });
    });

    // Close the Add User and Edit User modals when clicking outside the modal content
    window.addEventListener('click', (event) => {
        const addUserModal = document.getElementById('add-user-modal');
        const editUserModal = document.getElementById('edit-user-modal');
        if (event.target === addUserModal || event.target === editUserModal) {
            event.target.style.display = 'none';
        }
    });  


    const addClassButton = document.getElementById('add-class-button');
    const addClassModal = document.getElementById('add-class-modal');
    const addClassForm = document.getElementById('add-class-form');

    addClassButton.addEventListener('click', () => {
        addClassModal.style.display = 'block';
    });

    // Handle the Add Class form submission
    addClassForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(event.target);
        fetch('/add_class', {
            method: 'POST',
            body: formData,
        }).then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Error adding class');
            }
        });
    });

    // delete class
    const deleteClassButtons = document.querySelectorAll('[id^="delete-class-"]');
    deleteClassButtons.forEach(button => {
        button.addEventListener('click', () => {
            const classId = button.getAttribute('data-id');
            const formData = new FormData();
            formData.append('class_id', classId);

            fetch('/delete_class', {
                method: 'POST',
                body: formData,
            }).then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Error deleting class');
                }
            });
        });
    });

});

function enroll(classId) {
    fetch('/enroll', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ class_id: classId }),
    })
        .then((response) => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Error enrolling in class.');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function unenroll(classId) {
    fetch('/unenroll', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ class_id: classId }),
    })
        .then((response) => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Error unenrolling from class.');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function fetchStudentsAndGrades(classId) {
    fetch('/get_students_and_grades', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ class_id: classId })
    })
        .then(response => response.json())
        .then(data => {
            const studentsTable = document.getElementById('studentsTable');
            let tableBody = studentsTable.getElementsByTagName('tbody')[0];
            tableBody.innerHTML = '';

            for (const student of data) {
                let row = tableBody.insertRow();

                let idCell = row.insertCell();
                idCell.textContent = student.id;

                let nameCell = row.insertCell();
                nameCell.textContent = student.name;

                let gradeCell = row.insertCell();
                gradeCell.textContent = student.grade;
                gradeCell.contentEditable = "true";
                gradeCell.classList.add("grade-cell");

                gradeCell.addEventListener('focusout', function () {
                    const newGrade = gradeCell.textContent;
                    updateStudentGrade(student.id, classId, newGrade);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching students and grades:', error);
        });
}

  function updateStudentGrade(student_id, class_id, new_grade) {
    fetch('/update_student_grade', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            student_id: student_id,
            class_id: class_id,
            new_grade: new_grade
        })
    })
    .then(response => {
        if (response.ok) {
            fetchStudentsAndGrades(class_id);
        } else {
            console.error('Error updating student grade:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Error updating student grade:', error);
    });
}

  
