from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

NAVBAR = """
<div style="
width:250px;
height:100vh;
background:#1e293b;
position:fixed;
color:white;
padding:20px;
">

<h2>CS/Math Admin</h2>

<hr>

<p><a href="/" style="color:white;text-decoration:none;">Dashboard</a></p>
<p><a href="/budgets" style="color:white;text-decoration:none;">Budgets</a></p>
<p><a href="/faculty" style="color:white;text-decoration:none;">Faculty Requests</a></p>
<p><a href="/inventory" style="color:white;text-decoration:none;">Inventory</a></p>
<p><a href="/reports" style="color:white;text-decoration:none;">Reports</a></p>

</div>
"""


@app.get("/", response_class=HTMLResponse)
def dashboard():

    return f"""
    <html>

    <head>

    <title>Department Budget Tool</title>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    </head>

    <body style="margin:0;background:#f4f6f9;font-family:Arial;">

    {NAVBAR}

    <div style="margin-left:280px;padding:30px;">

    <h1>Department Dashboard</h1>

    <div style="display:flex;gap:20px;">

        <div style="
        background:white;
        padding:20px;
        width:220px;
        border-radius:15px;
        ">
            <h2>$250,000</h2>
            <p>Total Budget</p>
        </div>

        <div style="
        background:white;
        padding:20px;
        width:220px;
        border-radius:15px;
        ">
            <h2>$175,000</h2>
            <p>Total Spent</p>
        </div>

        <div style="
        background:white;
        padding:20px;
        width:220px;
        border-radius:15px;
        ">
            <h2>$75,000</h2>
            <p>Remaining</p>
        </div>

    </div>

    <br>

    <canvas id="budgetChart"></canvas>

    <script>

    new Chart(
        document.getElementById('budgetChart'),
        {{
            type:'bar',

            data:{{
                labels:[
                'Equipment',
                'Travel',
                'Payroll',
                'Research'
                ],

                datasets:[{{
                    label:'Budget Allocation',
                    data:[
                    50000,
                    30000,
                    120000,
                    50000
                    ]
                }}]
            }}
        }}
    )

    </script>

    </div>

    </body>

    </html>
    """


@app.get("/budgets", response_class=HTMLResponse)
def budgets():

    return f"""
    <html>

    <body style="margin:0;background:#f4f6f9;font-family:Arial;">

    {NAVBAR}

    <div style="margin-left:280px;padding:30px;">

    <h1>Budget Management</h1>

    <table border="1" cellpadding="10">

        <tr>
            <th>Department</th>
            <th>Allocated</th>
            <th>Spent</th>
            <th>Remaining</th>
        </tr>

        <tr>
            <td>Computer Science</td>
            <td>$120,000</td>
            <td>$70,000</td>
            <td>$50,000</td>
        </tr>

        <tr>
            <td>Mathematics</td>
            <td>$80,000</td>
            <td>$35,000</td>
            <td>$45,000</td>
        </tr>

    </table>

    </div>

    </body>

    </html>
    """


@app.get("/faculty", response_class=HTMLResponse)
def faculty():

    return f"""
    <html>

    <body style="margin:0;background:#f4f6f9;font-family:Arial;">

    {NAVBAR}

    <div style="margin-left:280px;padding:30px;">

    <h1>Faculty Funding Requests</h1>

    <table border="1" cellpadding="10">

        <tr>
            <th>Faculty</th>
            <th>Purpose</th>
            <th>Amount</th>
            <th>Status</th>
        </tr>

        <tr>
            <td>Dr. Rosenberg</td>
            <td>Conference Travel</td>
            <td>$1,500</td>
            <td>Approved</td>
        </tr>

        <tr>
            <td>Dr. Smith</td>
            <td>Research Equipment</td>
            <td>$3,000</td>
            <td>Pending</td>
        </tr>

    </table>

    </div>

    </body>

    </html>
    """


@app.get("/inventory", response_class=HTMLResponse)
def inventory():

    return f"""
    <html>

    <body style="margin:0;background:#f4f6f9;font-family:Arial;">

    {NAVBAR}

    <div style="margin-left:280px;padding:30px;">

    <h1>Equipment Inventory</h1>

    <table border="1" cellpadding="10">

        <tr>
            <th>Item</th>
            <th>Quantity</th>
            <th>Location</th>
        </tr>

        <tr>
            <td>GPU Workstation</td>
            <td>10</td>
            <td>Lab 302</td>
        </tr>

        <tr>
            <td>Projector</td>
            <td>5</td>
            <td>Department Office</td>
        </tr>

    </table>

    </div>

    </body>

    </html>
    """


@app.get("/reports", response_class=HTMLResponse)
def reports():

    return f"""
    <html>

    <body style="margin:0;background:#f4f6f9;font-family:Arial;">

    {NAVBAR}

    <div style="margin-left:280px;padding:30px;">

    <h1>Reports Center</h1>

    <ul>
        <li>January Budget Report</li>
        <li>February Budget Report</li>
        <li>March Budget Report</li>
        <li>Annual Department Summary</li>
    </ul>

    </div>

    </body>

    </html>
    """