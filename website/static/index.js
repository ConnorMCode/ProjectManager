function deleteProject(projectId){
    fetch('/delete-project', {
        method: 'POST',
        body: JSON.stringify({ projectId: projectId})
    }).then((_res) => {
        window.location.href = "/";
    })
}

function deleteToDo(todoId){
    fetch('/delete-todo', {
        method: 'POST',
        body: JSON.stringify({ todoId: todoId})
    }).then((_res) => {
        if ( window.history.replaceState ) {
            window.history.replaceState( null, null, window.location.href );
          }
        window.history.go(0)
    })
}