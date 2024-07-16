// make some classrooms

import { Classroom } from './0-classroom';

export default function initializeRooms() {
  const rooms = [19, 20, 34];
  return Array.map((room) => new Classroom(room));
}
