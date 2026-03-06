#for question 7
import time

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        print(f"[REQUEST] {request.method} {request.path}")
        response = self.get_response(request)
        duration = time.time() - start
        print(f"[RESPONSE] {request.path} took {duration:.4f} seconds")
        return response
    
