from flask import Flask, request, jsonify, render_template
from nqueens_solver import NQueensSolver

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Serve N-Queens frontend

@app.route("/solve_nqueens", methods=["POST"])
def solve_nqueens():
    data = request.get_json()
    N = int(data.get("N", 8))
    solver = NQueensSolver(N)
    solutions = solver.solve()
    return jsonify({
        "N": N,
        "total_solutions": len(solutions),
        "solutions": solutions
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)













