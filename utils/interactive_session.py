def is_interactive_session():
    """
    Checks if the code is being run in an interactive session 
    (e.g., Jupyter notebook or IPython terminal).
    """
    try:
        from IPython import get_ipython
        # get_ipython() returns an InteractiveShell instance if in an IPython environment,
        # otherwise it returns None.
        return get_ipython() is not None
    except (NameError, ImportError):
        # If IPython is not installed or not in the path, we can safely assume
        # it's not an interactive IPython session.
        return False