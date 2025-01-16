import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'start_auto_theorie.settings')  # Ensure this matches your settings module.

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc

    execute_from_command_line(sys.argv)

# The main block should not be indented inside the `main()` function.
if __name__ == '__main__':
    main()
