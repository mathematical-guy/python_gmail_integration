import json


class QueryBuilder:
    BASE_QUERY = f"SELECT * FROM emails"

    def __init__(self):
        self.rules = None
        self.operator = ''
        self.selected_rules = []
        self.selected_rule_ids = []

        with open("rules.json", 'r') as file:
            self.rules = json.load(file)['rules']

        if self.rules is None:
            print("No Rules are configured")
            return

        self.__display_rules()
        self.__get_inputs_from_user()
        self.__get_rules()

    def __display_rules(self):
        print("Available filters:\n")
        for rule in self.rules:
            print(f"{rule['rule_id']}: {rule['description']}")

    def __get_inputs_from_user(self):
        try:
            selected_rules = input("\nEnter the rule numbers you want to apply, separated by commas: ")
            self.selected_rule_ids = [int(rule_id.strip()) for rule_id in selected_rules.split(",") if
                                      rule_id.strip().isdigit()]

            if len(self.selected_rule_ids) > 1:
                self.operator = input(
                    "Choose an operator to apply (AND/OR) or leave blank for default: ").strip().upper()

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return

    def __get_rules(self):
        self.selected_rules = [rule for rule in self.rules if rule['rule_id'] in self.selected_rule_ids]

        if not self.selected_rules:
            print("No such rule exists. Please try again.")
            return

    def build_sql_query(self) -> str:
        conditions = []
        operator = ''

        for rule in self.selected_rules:
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

        if condition_str != '':
            result_query = self.BASE_QUERY + " WHERE " + condition_str + ";"
        else:
            result_query = self.BASE_QUERY + ";"

        return result_query
