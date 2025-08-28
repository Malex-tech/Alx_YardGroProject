from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("<h1>Welcome to YardGro API</h1><p>Use /admin/ or /api/…</p>")

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head><title>YardGro API</title></head>
            <body style="font-family: sans-serif; padding: 2rem;">
                <h1>🌱 Welcome to YardGro API</h1>
                <p>This backend powers YardGro. Key endpoints:</p>
                <ul>
                    <li><b>Authentication:</b> <code>/api/users/</code> — Sign up and log in securely</li>
                    <li><b>Products:</b> <code>/api/produce/</code> — Add, view, or update food inventory</li>
                    <li><b>Orders:</b> <code>/api/logistics/</code> — Track distribution and sales</li>
                    <li><b>Reports:</b> <code>/api/reports/</code> — Get structured data for dashboards</li>
                </ul>
            </body>
        </html>
    """)
