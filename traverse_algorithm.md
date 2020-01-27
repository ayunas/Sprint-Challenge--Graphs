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


'''
old room_traverse algorithm:
    -get old_room_id, old_room_exits.
    -log_room(room_id, None) to Traversal() if no way chosen, None sets all ways to '?'
    -randomly choose an exit
    -travel to the exit
    -add room_id to visited
    -get the new_room_id, new_room_exits
    -log_room(new_room_id, (way, way_room_id)) 
    -update old_room: log_room(old_room_id, (way,way_room_id))

get id of current room.
create a new traversal entry of current room.

go out an exit. store the direction travelled
create a new entry for the new room id, the opposite direction is the prev_room_id.
update the previous room id entry.  the exit taken == id of current room
player.travel(exits[0])
player.current_room.id
'''