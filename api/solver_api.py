import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route("/solve")
def solve():
  A = np.matrix("7, 1, 5; 4, 3, 5; 6, 1, 2")
  c = np.matrix("27; 21; 9")
  print(np.matmul(np.linalg.inv(A), c).round(4))

  return float(const[:slash])/float(const[slash+1:])

