import numpy as np
from flask import Flask, request
from typing import *
import json

app = Flask(__name__)

@app.get("/solve")
def solve_controller():
  A = build_matrix(request.json['coefficients'])
  c = build_matrix(request.json['constants'])
  b = np.matmul(np.linalg.inv(A), c).round(4)
  return json.dumps({"solutions": b[:,0].tolist()})

#creates a matrix string from a 
def build_matrix(vals: List[str]):
  out = ""
  for i in vals:
    out += (i + ";")
  return np.matrix(out[:len(out)-1])

if __name__ == "__main__":
  app.run()
