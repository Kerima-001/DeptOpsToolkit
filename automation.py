def budget_alerts(budgets):

    alerts = []

    for budget in budgets:

        if budget["spent"] > budget["allocated"]:

            alerts.append(
                f"{budget['department']} exceeded budget"
            )

    return alerts
