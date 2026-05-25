# Configuration
# Secrets are managed via environment variables
# Never hardcode credentials in source code

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
STRIPE_KEY = os.environ.get("STRIPE_KEY")
