import json
from database import DatabaseClient
from query_builder import QueryBuilder

"""

SELECT * FROM emails WHERE;


sender='VALUE'            -> Exact sender email
sender LIKE '%VALUE%'     -> Contains sender email

snippet LIKE '%VALUE%'     -> Contains body


DATE(date_received) > 'VALUE'     -> Greater than particular date
DATE(date_received) < 'VALUE'     -> Lesser than particular date
TIME(date_received) < 'VALUE'     -> Greater than particular time
TIME(date_received) < 'VALUE'     -> Lesser than particular date


"""


def get_rules_from_user():
    rules = None
    with open("rules.json", 'r') as file:
        rules = json.load(file)['rules']
    if rules is None:
        print("No Rules are configured")
        return

    print("Available filters:\n")
    for rule in rules:
        print(f"{rule['rule_id']}: {rule['description']}")

    try:
        selected_rules = input("\nEnter the rule numbers you want to apply, separated by commas: ")
        selected_rule_ids = [int(rule_id.strip()) for rule_id in selected_rules.split(",") if rule_id.strip().isdigit()]

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    selected_rules = [rule for rule in rules if rule['rule_id'] in selected_rule_ids]

    if not selected_rules:
        print("No such rule exists. Please try again.")
        return

    return selected_rules


def build_sql_query(rules: list[dict]):
    conditions = []
    operator = ''

    if len(rules) > 1:
        operator = input("Choose an operator to apply (AND/OR) or leave blank for default: ").strip().upper()

    for rule in rules:
        if rule.get('rule_id') in [1, 2]:
            start = input("Enter From Value: ")
            end = input("Enter To Value: ")
            condition_filter = {
                "from": start,
                "to": end,
            }
        else:
            value = input("Enter Value: ")
            condition_filter = {
                "value": value
            }

        condition = rule['query'].format(**condition_filter)
        conditions.append(condition)

    if operator == 'AND':
        condition_str = " AND ".join(conditions)
    elif operator == 'OR':
        condition_str = " OR ".join(conditions)
    else:
        condition_str = conditions[0]

    return condition_str


if __name__ == "__main__":
    database = DatabaseClient()
    BASE_QUERY = f"SELECT * FROM emails"

    # rules = get_rules_from_user()
    # if not rules:
    #     print("You have not selected correct rules")
    #     exit()

    # query = build_sql_query(rules=rules)

    # result_query = BASE_QUERY + " WHERE " + query + ";"

    result_query = QueryBuilder().build_sql_query()

    emails_list = database.cursor.execute(result_query).fetchall()
    for email in emails_list:
        print(email)
        print('-'*30)
