# Requirements

## Functional Requirements
- Users can register, log in, and manage their profile.
- Users can build and manage multi-week workout programs based on mesocycle principles.
- Users can add exercises to workouts, pairing each with advanced training techniques (myo reps, dropset, superset, cluster set, pre-exhaustion).
- Users can log every workout, specifying sets and reps performed per exercise.
- A dashboard will display:
  - Recent training history—filterable by week/month, with access to previous workouts.
  - Progress graphs by muscle group: X-axis (time), Y-axis (weekly set volume).
- Users can review details of past workouts.
- The system stores and retrieves user workout data securely.

## Technical Requirements
- RESTful API backend (FastAPI).
- Relational database (e.g., PostgreSQL) storing users, programs, workouts, sets, exercises, and progress stats.
- JWT authentication for user security.
- Responsive frontend for dashboard and program management.

