from html import escape


def render_workout_table(workout_data: dict) -> str:

    html = """
    <div class="workout-wrapper">
    """

    for day in workout_data.get("schedule", []):

        day_name = escape(day.get("day", ""))
        day_title = escape(day.get("title", ""))

        html += f"""
        <section class="workout-day">

            <div class="day-header">
                <div>
                    <div class="day-label">{day_name}</div>
                    <div class="day-title">{day_title}</div>
                </div>
            </div>

            <div class="table-container">

                <table class="workout-table">

                    <thead>
                        <tr>
                            <th>Block</th>
                            <th>Exercise</th>
                            <th>Sets</th>
                            <th>Reps</th>
                            <th>Rest</th>
                            <th>Intensity / Notes</th>
                        </tr>
                    </thead>

                    <tbody>
        """

        for block in day.get("blocks", []):

            block_name = escape(
                block.get("block", "")
            )

            for exercise in block.get("exercises", []):

                name = escape(
                    exercise.get("name", "")
                )

                sets = escape(
                    exercise.get("sets", "-")
                )

                reps = escape(
                    exercise.get("reps", "-")
                )

                rest = escape(
                    exercise.get("rest", "-")
                )

                notes = escape(
                    exercise.get("notes", "-")
                )

                html += f"""
                    <tr>

                        <td>
                            <span class="block-badge">
                                {block_name}
                            </span>
                        </td>

                        <td class="exercise-name">
                            {name}
                        </td>

                        <td class="sets">
                            {sets}
                        </td>

                        <td class="reps">
                            {reps}
                        </td>

                        <td class="rest">
                            {rest}
                        </td>

                        <td class="notes">
                            {notes}
                        </td>

                    </tr>
                """

        html += """
                    </tbody>

                </table>

            </div>

        </section>
        """

    html += """
    </div>
    """

    return html