

from helpers import can_be_int, valid_number_of_params
from safe_send import safe_send
from datetime import datetime, timezone
import zoneinfo

CREW_FIELDS = ['casters', 'admins']

def epoch_to_year_month(epoch: int):
    # Convert epoch to UTC datetime with timezone awareness
    dt_utc = datetime.fromtimestamp(epoch, tz=timezone.utc)
    
    # Convert to Eastern Time (handles both EST and EDT automatically)
    et_tz = zoneinfo.ZoneInfo("America/New_York")
    dt_et = dt_utc.astimezone(et_tz)
    
    year = dt_et.year
    month = dt_et.month
    return year, month


async def month_payouts_handler(db, message):

    valid_params, params = valid_number_of_params(message, 4)

    month = params[1]
    year = params[2]
    money = params[3]

    if not valid_params:
        await safe_send(message.channel, "Invalid number of parameters. Please provide a valid command.")
        return

    if not can_be_int(month):
        await safe_send(message.channel, "Invalid month parameter. Please provide a valid month (1-12).")
        return
    month = int(month)
    
    if not can_be_int(year):
        await safe_send(message.channel, "Invalid year parameter. Please provide a valid year (e.g., 2024).")
        return
    year = int(year)

    money = float(money)
    
    matchup_history = db['matchup_history']
    all_past_matchups = matchup_history.find()

    matchups_during_month = []
    for matchup in all_past_matchups:
        matchup_epoch = matchup['match_epoch']
        matchup_year, matchup_month = epoch_to_year_month(matchup_epoch)
        if matchup_year == year and matchup_month == month:
            matchups_during_month.append(matchup)


    crew_points_array = {}

    for matchup in matchups_during_month:

        crew_record = matchup['crew_record']

        for crew_field in CREW_FIELDS:

            users_in_crew_group = crew_record.get(crew_field, [])

            for crew_member in users_in_crew_group:

                if crew_member not in crew_points_array:
                    crew_points_array[crew_member] = 1
                else:
                    crew_points_array[crew_member] += 1


    total_points = sum(crew_points_array.values())

    output_string = ''
    for crew_member, points in crew_points_array.items():

        payout = (points / total_points) * money if total_points > 0 else 0
        payout = round(payout, 2)

        output_string += f'{crew_member}: {points} points. Payout: ${payout} Command: !pay {crew_member} {payout}\n'

    await safe_send(message.channel, f'Monthly Payouts for {month}/{year}:\n{output_string}')

