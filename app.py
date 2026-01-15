from flask import Flask, render_template, request, redirect, make_response
import csv
import io

app = Flask(__name__)

# Temporary data storage (In a real app, you'd use a database)
expenses = []

@app.route('/')
def index():
    total = sum(item['amount'] for item in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add_expense():
    meal_type = request.form.get('meal_type')
    item_name = request.form.get('item_name')
    amount = float(request.form.get('amount', 0))
    
    if item_name and amount > 0:
        expenses.append({
            'meal_type': meal_type,
            'item_name': item_name,
            'amount': amount
        })
    
    return redirect('/')

@app.route('/download_csv')
def download_csv():
    # Create a string buffer to write CSV data
    si = io.StringIO()
    cw = csv.DictWriter(si, fieldnames=['meal_type', 'item_name', 'amount'])
    
    # Write header and rows
    cw.writeheader()
    cw.writerows(expenses)
    
    # Create the response
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=expenses.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route('/clear')
def clear():
    expenses.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')