from coinbase import jwt_generator

api_key = "391476e6-d534-4ae3-9993-da994e065e29"
api_secret = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIG9hHQxiA+wsHTmppd3LDUiCXc6YIAk6icOxe0Cn72CAoAoGCCqGSM49
AwEHoUQDQgAEGUdoUyZ4GrDAy1pV2QY5XcEfw/LZlWj8JIbloY+1EaD0ZATV36Dj
CFJr4xkpT1QnJKI+5Hhr2vNQlM1FRXaAXQ==
-----END EC PRIVATE KEY-----"""

request_method = "GET"
request_path = "/api/v3/brokerage/products"

jwt_uri = jwt_generator.format_jwt_uri(request_method, request_path)
jwt_token = jwt_generator.build_rest_jwt(jwt_uri, api_key, api_secret)
print(jwt_token)
