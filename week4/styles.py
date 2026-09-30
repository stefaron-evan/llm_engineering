CSS = """
:root {
  --py-color: #209dd7;
  --cpp-color: #ecad0a;
  --accent:   #753991;
  --card:     #161a22;
  --text:     #e9eef5;
}

/* Full-width layout */
.gradio-container {
  max-width: 100% !important;
  padding: 0 40px !important;
}

/* Code card styling */
.card {
  background: var(--card);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 14px;
  padding: 10px;
}

/* Buttons */
.convert-btn button {
  background: var(--accent) !important;
  border-color: rgba(255,255,255,.12) !important;
  color: white !important;
  font-weight: 700;
}
.run-btn button {
  background: #202631 !important;
  color: var(--text) !important;
  border-color: rgba(255,255,255,.12) !important;
}
.run-btn.py button:hover  { box-shadow: 0 0 0 2px var(--py-color) inset; }
.run-btn.cpp button:hover { box-shadow: 0 0 0 2px var(--cpp-color) inset; }
.convert-btn button:hover { box-shadow: 0 0 0 2px var(--accent) inset; }

/* Outputs with color tint */
.py-out textarea {
  background: linear-gradient(180deg, rgba(32,157,215,.18), rgba(32,157,215,.10));
  border: 1px solid rgba(32,157,215,.35) !important;
  color: rgba(32,157,215,1) !important;
  font-weight: 600;
}
.cpp-out textarea {
  background: linear-gradient(180deg, rgba(236,173,10,.22), rgba(236,173,10,.12));
  border: 1px solid rgba(236,173,10,.45) !important;
  color: rgba(236,173,10,1) !important;
  font-weight: 600;
}

/* Align controls neatly */
.controls .wrap {
  gap: 10px;
  justify-content: center;
  align-items: center;
}

.workout-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 20px;
}


/* =========================
   DAY CARD
========================= */

.workout-day {
    background: white;
    border: 1px solid #e5e5e5;
    border-radius: 14px;
    overflow: hidden;
}


/* =========================
   DAY HEADER
========================= */

.day-header {
    padding: 16px 20px;

    background: #f7f7f7;

    border-bottom: 1px solid #e5e5e5;

    display: flex;
    align-items: center;
}

.day-label {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;

    color: #777;
}

.day-title {
    margin-top: 3px;

    font-size: 20px;
    font-weight: 700;

    color: #222;
}


/* =========================
   TABLE
========================= */

.table-container {
    width: 100%;
    overflow-x: auto;
}

.workout-table {
    width: 100%;
    min-width: 850px;

    border-collapse: collapse;

    font-size: 13px;
}

.workout-table th {
    padding: 12px 14px;

    text-align: left;

    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;

    color: #777;

    background: #fafafa;

    border-bottom: 1px solid #e5e5e5;
}

.workout-table td {
    padding: 14px;

    vertical-align: top;

    border-bottom: 1px solid #eeeeee;

    line-height: 1.5;
}

.workout-table tbody tr:last-child td {
    border-bottom: none;
}

.workout-table tbody tr:hover {
    background: #fafafa;
}


/* =========================
   BLOCK
========================= */

.block-badge {
    display: inline-block;

    padding: 5px 9px;

    border-radius: 6px;

    background: #f1f1f1;

    font-size: 11px;
    font-weight: 600;

    white-space: nowrap;
}


/* =========================
   EXERCISE
========================= */

.exercise-name {
    min-width: 180px;

    font-weight: 600;
    color: #222;
}


/* =========================
   SETS / REPS
========================= */

.sets,
.reps {
    min-width: 60px;

    font-weight: 600;

    white-space: nowrap;
}


/* =========================
   REST
========================= */

.rest {
    min-width: 90px;

    white-space: nowrap;

    color: #555;
}


/* =========================
   NOTES
========================= */

.notes {
    min-width: 250px;

    color: #666;
}


/* =========================
   MOBILE
========================= */

@media (max-width: 768px) {

    .day-header {
        padding: 14px;
    }

    .day-title {
        font-size: 17px;
    }

    .workout-table {
        min-width: 800px;
    }

}
"""
