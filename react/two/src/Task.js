function Task(props) {
    let { task, doneTask, index, deletTask } = props;

    return (
        <div className="task" style={{textDecoration: task.done ? 'line-through' : ''}}>
            {task.text}
            <div>
                <button onClick={() => doneTask(index)}>Done</button>
                <button onClick={() => deletTask(index)}>X</button>
            </div>
        </div>
    )
}

export default Task;