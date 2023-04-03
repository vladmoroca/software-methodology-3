import numpy
from fastapi import APIRouter

router = APIRouter()

@router.get('/matrixMult')
def matrixMult() -> dict:
    matrix_a = numpy.random.rand(10, 10)
    matrix_b = numpy.random.rand(10, 10)
    product = numpy.dot(matrix_a, matrix_b)
    return  {
            "matrix_a": matrix_a.tolist(),
            "\n matrix_b": matrix_b.tolist(),
            "\n product": product.tolist(),
            }