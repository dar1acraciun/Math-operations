from pydantic import BaseModel, ValidationError
from typing import List

class PowerRequest(BaseModel):
    base: float
    exponent: float

class PowerResponse(BaseModel):
    result: str

class FibonacciRequest(BaseModel):
    n: int

class FibonacciResponse(BaseModel):
    result: str
    sequence: List[int]

class FactorialRequest(BaseModel):
    n: int

class FactorialResponse(BaseModel):
    result: str
