from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden

styled_message = """
                <html>
                <head>
                    <style>
                        body {
                            background-color: #f8f9fa;
                            font-family: Arial, sans-serif;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            height: 100vh;
                            margin: 0;
                        }
                        .error-box {
                            background: white;
                            border: 2px solid #dc3545;
                            padding: 30px;
                            border-radius: 10px;
                            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
                            text-align: center;
                        }
                        h1 {
                            color: #dc3545;
                            font-size: 28px;
                            margin-bottom: 10px;
                        }
                        p {
                            color: #333;
                            font-size: 16px;
                        }
                    </style>
                </head>
                <body>
                    <div class="error-box">
                        <h1>Access Denied</h1>
                        <p>You are not authorized to access this page.</p>
                    </div>
                </body>
                </html>
            """


def login_and_role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapprd_view(request, *args, **kwargs):
            user = request.user
            if required_role == 'customer' and not user.is_customer:
                return HttpResponseForbidden(styled_message)
            if required_role == 'seller' and not user.is_seller:
                return HttpResponseForbidden(styled_message)
            return view_func(request, *args, **kwargs)
        return _wrapprd_view
    return decorator