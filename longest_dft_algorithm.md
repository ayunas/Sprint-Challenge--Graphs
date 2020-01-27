<h1>Longest Depth First Search Algorithm</h1>
<h2>Traverse the entire graph by getting the longest one from start_room to end_room</h2>
<ol>
    <li>Create a Stack</li>
    <li>Push a path array with start_room in it to the stack</li>
    <li>Initialize Visited Set</li>
    <li>While stack.size > 0</li>
        <ul>
            <li>pop the latest path off the stack</li>
            <li>choose a valid direction to travel to</li>
            <li>check to to see if the room has <strong>NOT</strong> been visited</li>
                <ul>
                    <li>Check IF the room == target_room:</li>
                        <ul>
                            <li>if it is, return the latest path popped off the stack</li>
                        </ul>
                    <li>else the room is not ==  target_room, so add the room to visited</li>
                </ul>
            <li>Grab the exits of the new_room</li>
                <ul>
                    <li>for each exit of the new room</li>
                        <ul>
                            <li>move to the new room</li>
                            <li>create a new copy of the current path</li>
                            <li>Add the new_room to the fresh copy of the path </li>
                            <li>push the new path to the stack</li>
                        </ul>
                </ul>
        </ul>
    <li>The longest path is the one that visits all of the rooms</li>

</ol>
