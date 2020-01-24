<h1>Room Traverse Algorithm</h1>
<ol>
        <li>get current_room_id</li>
        <li>room = player.current_room</li>
        <li>while the self.graph[room.id] has any key/val of question mark:</li>
                     <li>randomly pick one of the question marks</li>
                     <li>move in that direction</li>
                         <li>if "cant move message"</li>
                                 <li>-update_rooms()</li>
                                            <li>-log_room(new_room_id, (fpped_way, old_room_id) )</li>
                                            <li>-log_room(old_room_id, (way , None) )</li>
                          <li>-else:</li>
                                 <li>add new_room to visited</li>
                                 <li>update_rooms()</li>
                                         <li>-log_room(new_room_id, (fpped_way, old_room_id)</li>
                                         <li>-log_room(old_room_id, (way, new_room_id)</li>
                                 <li>room = new_room</li>
</ol>

